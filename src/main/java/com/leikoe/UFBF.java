package com.leikoe;

import com.leikoe.bitscontainers.BlockBitSet;
import com.leikoe.hash.Murmur64;
import jdk.incubator.vector.*;

public class UFBF<T> extends BloomFilter<T> {

    VectorSpecies<Integer> SPECIES = IntVector.SPECIES_PREFERRED;

    // species bound
    int upperBound;

    int[] ks;
    IBitsBlocksContainer bits;
    IntVector vr_unit;

    /**
     * Constructor
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param expectedInsertCount the expected number of add() calls
     */
    public UFBF(int expectedInsertCount) {
        super(
                new BlockBitSet(
                        getOptimalSize(expectedInsertCount),
                        getOptimalNumberOfHashFunctions(expectedInsertCount, getOptimalSize(expectedInsertCount))
                ),
                expectedInsertCount
        );
        k = ((IBitsBlocksContainer) super.bits).blockSize();
        ks = new int[k];
        for (int i=1; i<=k; i++) {
            ks[i-1] = i;
        }

        upperBound = SPECIES.loopBound(k);
        this.bits = (IBitsBlocksContainer) super.bits;


        vr_unit = IntVector.broadcast(SPECIES, 1);
    }

    /**
     * Main hash function
     * vector implementation of the fast hash used in google guava's bloomfilter

     * from "Less Hashing, Same Performance: Building a Better Bloom Filter" by Adam Kirsch
     *
     * @param seeds IntVector of the seeds
     * @param hash1 first hash
     * @param hash2 second hash
     * @return IntVector of hash1 + seed * hash2
     */
    private IntVector hash(IntVector seeds, int hash1, int hash2) {
        return seeds.mul(hash2).add(hash1);
    }

    /**
     * inserts a generic value into the filter
     * this was implemented using the whitepaper "Ultra-Fast Bloom Filters using SIMD Techniques" by Jianyuan Lu
     *
     * @param value
     */
    @Override
    public void add(T value) {
        long hash64 = Murmur64.hash(value.hashCode());
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);

        // hash1 needs to be positive, this could be achieved by either bitwise not or abs()
        hash1 = Math.abs(hash1);

        // get the block of k ints
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        int i = 0;
        for (; i + SPECIES.length() <= upperBound; i += SPECIES.length()) {
            // get the values of k as the seeds for hashing
            IntVector z = IntVector.fromArray(SPECIES, ks, i);

            // hash the seeds using hash1 and hash2 and get a positive result
            IntVector vr_val = hash(z, hash1, hash2).abs();

            // this is the vector equivalent of vr_a[k] = 1 << hash(k, hash1, hash2).abs()
            IntVector vr_a = vr_unit.lanewise(VectorOperators.LSHL, vr_val);

            // store the hashes back into the bits block
            vr_a.intoArray(block, i);
        }

        // process the rest in scalar code
        for (; i<k; i++) {
            int pos = hash1 + ((i+1) * hash2);
            // same as for hash1
            pos = Math.abs(pos);
            // set the bit at pos in block[i] to true
            block[i] |= 1 << pos;
        }

        this.n++;
    }

    /**
     * Membership check function
     *
     * @param value the value to check membership for
     * @return whether the value is in the bloomfilter or not
     */
    @Override
    public boolean mightContain(T value) {
        long hash64 = Murmur64.hash(value.hashCode());
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);


        hash1 = Math.abs(hash1);
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        int i = 0;
        for (; i + SPECIES.length() <= upperBound; i += SPECIES.length()) {
            // get the values of k as the seeds for hashing
            IntVector z = IntVector.fromArray(SPECIES, ks, i);

            // hash the seeds using hash1 and hash2 and get a positive result
            IntVector vr_val = hash(z, hash1, hash2).abs();

            // this is the vector equivalent of vr_a[k] = 1 << hash(k, hash1, hash2).abs()
            IntVector vr_a = vr_unit.lanewise(VectorOperators.LSHL, vr_val);

            // compare with block
            IntVector vr_b = IntVector.fromArray(SPECIES, block, i);
            vr_b = vr_b.not();

            IntVector vr_test = vr_a.and(vr_b);
            // if each bit set int vr_a isn't set in vr_b, it will return false
            if (vr_test.reduceLanes(VectorOperators.ADD) != 0) {
                return false;
            }
        }

        // process the rest in scalar code
        for (; i<k; i++) {
            int pos = hash1 + ((i+1) * hash2);
            // same as for hash1
            pos = Math.abs(pos);
            // if the bit at pos in block[i] is not set, return false
            if ((block[i] & 1 << pos) == 0) {
                return false;
            }
        }

        return true;
    }
}
