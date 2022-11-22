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

        ks = new int[k];
        for (int i=0; i<k; i++) {
            ks[i] = i;
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

        int[] block = bits.getBlock(hash1);

        System.out.println(block);

        int i = 1;
        for (; i <= upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, ks, i);
            IntVector v_combinedHash = z.mul(hash2).add(hash1);

            // Flip all the bits if it's negative (guaranteed positive number)
            VectorMask<Integer> mask = v_combinedHash.lt(0);
            v_combinedHash = v_combinedHash.blend(v_combinedHash.not(), mask);

            IntVector vr_val = v_combinedHash;
            IntVector vr_a = IntVector.broadcast(SPECIES, 1);
            vr_a = vr_a.lanewise(VectorOperators.LSHL, vr_val);

            System.out.println("\nDEBUG");
            System.out.println(vr_val);
            System.out.println(vr_a);

            vr_a.intoArray(block, i);

//
//
//            IntVector vr_b = IntVector.fromArray(SPECIES, block, i);
//            vr_b = vr_b.not();
//
//            VectorMask<Integer> vr_test = vr_a.compare(VectorOperators.EQ, vr_b);
//
//            for (int j = 0; j<; j += SPECIES.length()) {
//                int pos = v_combinedHash.lane(j) % bits.size();
//                bits.set(pos, true);
//            }
        }

        // process the rest
        for (; i<=k; i++) {
            int pos = hash1 + (i * hash2);
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

        int i = 1;
        for (; i <= upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, ks, i);
            IntVector v_combinedHash = z.mul(hash2).add(hash1);

            // Flip all the bits if it's negative (guaranteed positive number)
            VectorMask<Integer> mask = v_combinedHash.lt(0);
            v_combinedHash = v_combinedHash.blend(v_combinedHash.not(), mask);
//            v_combinedHash = modulus(v_combinedHash, v_m); // this is slow as shit don't use it

            for (int j = 0; j<SPECIES.length(); j++) {
                int pos = v_combinedHash.lane(j) % bits.size();
                if (!bits.get(pos)) {
                    return false;
                }
            }
        }

        // process the rest
        for (; i<=k; i++) {
            int pos = hash1 + (i * hash2);
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
