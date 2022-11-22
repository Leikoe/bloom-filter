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

    /**
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param capacity
     */
    public UFBF(int capacity) {
        super(
                new BlockBitSet(
                        getOptimalSize(capacity),
                        getOptimalNumberOfHashFunctions(capacity, getOptimalSize(capacity))
                ),
                capacity
        );
        k = ((IBitsBlocksContainer) super.bits).blockSize();
        ks = new int[k];
        for (int i=1; i<=k; i++) {
            ks[i-1] = i;
        }

        upperBound = SPECIES.loopBound(k);
        this.bits = (IBitsBlocksContainer) super.bits;
    }

    /**
     * from "Less Hashing, Same Performance: Building a Better Bloom Filter" by Adam Kirsch
     *
     * @param value
     */
    @Override
    public void add(T value) {
        long hash64 = Murmur64.hash(value.hashCode());
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);

        if (hash1 < 0) {
            hash1 = ~hash1;
        }
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        int i = 0;
        for (; i + SPECIES.length() <= upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, ks, i);
            IntVector v_combinedHash = z.mul(hash2).add(hash1);

            // Flip all the bits if it's negative (guaranteed positive number)
            VectorMask<Integer> mask = v_combinedHash.lt(0);
            v_combinedHash = v_combinedHash.blend(v_combinedHash.not(), mask);

            IntVector vr_val = v_combinedHash;
            IntVector vr_a = IntVector.broadcast(SPECIES, 1);
            vr_a = vr_a.lanewise(VectorOperators.LSHL, vr_val);

            vr_a.intoArray(block, i);
        }

        // process the rest
        for (; i<k; i++) {
            int pos = hash1 + ((i+1) * hash2);
            if (pos < 0) {
                pos = ~pos;
            }
            bits.set(pos % bits.size(), true);
        }

//        bits.setBlock(hash1, block); // useless
        this.n++;
    }

    @Override
    public boolean mightContain(T value) {
        long hash64 = Murmur64.hash(value.hashCode());
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);


        if (hash1 < 0) {
            hash1 = ~hash1;
        }
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        int i = 0;
        for (; i + SPECIES.length() <= upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, ks, i);
            IntVector v_combinedHash = z.mul(hash2).add(hash1);

            // Flip all the bits if it's negative (guaranteed positive number)
            VectorMask<Integer> mask = v_combinedHash.lt(0);
            v_combinedHash = v_combinedHash.blend(v_combinedHash.not(), mask);

            IntVector vr_val = v_combinedHash;
            IntVector vr_a = IntVector.broadcast(SPECIES, 1);
            vr_a = vr_a.lanewise(VectorOperators.LSHL, vr_val);

            // compare with block
            IntVector vr_b = IntVector.fromArray(SPECIES, block, i);
//            vr_b = vr_b.not();

            IntVector vr_test = vr_a.and(vr_b);
            if (!vr_test.compare(VectorOperators.EQ, vr_a).allTrue()) {
                return false;
            }
        }

        // process the rest
        for (; i<k; i++) {
            int pos = hash1 + ((i+1) * hash2);
            if (pos < 0) {
                pos = ~pos;
            }
            if (!bits.get(pos % bits.size())) {
                return false;
            }
        }

        return true;
    }
}
