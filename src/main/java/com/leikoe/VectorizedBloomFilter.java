package com.leikoe;

import static com.leikoe.hash.Utils.positiveMod;

import com.leikoe.hash.Utils;
import jdk.incubator.vector.*;

import java.util.Set;

/**
 * WARNING: REQUIRES JAVA 18+
 */

public class VectorizedBloomFilter<T> extends BloomFilter<T> {

    VectorSpecies<Integer> SPECIES = IntVector.SPECIES_PREFERRED;

    // species bound
    int upperBound;

    int[] ks;
    IntVector v_m;

    /**
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param bitsContainer user provided bits container, all initialized to 0, must implement IBitsContainer
     * @param capacity
     */
    public VectorizedBloomFilter(IBitsContainer bitsContainer, int capacity) {
        super(bitsContainer, capacity);
//        assert(isPowerof2(bitsContainer.size()));
        ks = new int[k];

        // init array with k values except for the 2 first elements
        for (int i=0; i<k; i++) {
            ks[i] = i;
        }

        upperBound = SPECIES.loopBound(k);
        v_m = IntVector.broadcast(SPECIES, bits.size());
    }

    public static boolean isPowerof2(int v) {
        return v != 0 && ((v & (v - 1)) == 0);
    }



    // this is too slow, switching to fast range
    public static IntVector modulus(IntVector x, IntVector m) {
        IntVector v_q = x.div(m);
        return x.sub(m.mul(v_q));
    }

    // fast range by daniel lemire https://lemire.me/blog/2016/06/27/a-fast-alternative-to-the-modulo-reduction/
//    int reduce(uint32_t x, uint32_t N) {
//        return ((uint64_t) x * (uint64_t) N) >> 32 ;
//    }


    /**
     * from "Less Hashing, Same Performance: Building a Better Bloom Filter" by Adam Kirsch
     *
     * @param value
     */
    @Override
    public void add(T value) {
        long hash64 = murmur64(value.hashCode());
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
                bits.set(pos, true);
            }
        }

        // process the rest
        for (; i<=k; i++) {
            int pos = hash1 + (i * hash2);
            if (pos < 0) {
                pos = ~pos;
            }
            bits.set(pos % bits.size(), true);
        }
        this.n++;
    }

    // boilerplate murmur64 hash implementation from https://www.sderosiaux.com/articles/2017/08/26/the-murmur3-hash-function--hashtables-bloom-filters-hyperloglog/
    private static long murmur64(long k) {
        k ^= k >>> 33;
        k *= 0xff51afd7ed558ccdL;
        k ^= k >>> 33;
        k *= 0xc4ceb9fe1a85ec53L;
        k ^= k >>> 33;
        return k;
    }

    @Override
    public boolean mightContain(T value) {
        long hash64 = murmur64(value.hashCode());
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

    /**
     * wrapper of BloomFilter.getOptimalSize(int n), which returns the next power of 2 optimal size
     *
     * @param n the number of elements to be inserted in the filter
     * @return the optimal bits container size
     */
    public static int getOptimalSize(int n) {
        return Utils.nextPowerOf2(BloomFilter.getOptimalSize(n));
    }
}
