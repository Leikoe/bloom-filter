package com.leikoe;

import com.leikoe.bitscontainers.BlockBitSet;
import com.leikoe.hash.Murmur64;

import static com.leikoe.NaiveBloomFilter.getOptimalNumberOfHashFunctions;
import static com.leikoe.NaiveBloomFilter.getOptimalSize;

public class BloomFilter<T> implements IBloomFilter<T> {

    IBitsBlocksContainer bits;
    private int n;
    private final int k;

    /**
     * Constructor
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param expectedInsertCount the expected number of add() calls
     */
    public BloomFilter(int expectedInsertCount) {
        int m = getOptimalSize(expectedInsertCount);
        this.k = getOptimalNumberOfHashFunctions(expectedInsertCount, m);
        this.bits = new BlockBitSet(m, k);
        assert (bits.size() >= getOptimalSize(expectedInsertCount));
        this.n = 0;
    }

    /**
     * Main hash function
     * implementation of the fast hash used in google guava's bloomfilter
     * from "Less Hashing, Same Performance: Building a Better Bloom Filter" by Adam Kirsch
     *
     * @param seed seed for the hash
     * @param hash1 first hash
     * @param hash2 second hash
     * @return IntVector of hash1 + seed * hash2
     */
    private int hash(int seed, int hash1, int hash2) {
        return seed * hash2 + hash1;
    }

    /**
     * inserts a generic value into the filter
     * this was implemented using the whitepaper "Ultra-Fast Bloom Filters using SIMD Techniques" by Jianyuan Lu
     * (this is the scalar implementation of the hashing technique, see UFBF class for vector implementation)
     *
     * @param value
     */
    public void add(T value) {
        long hash64 = Murmur64.hash(value.hashCode());
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);

        // hash1 needs to be positive, this could be achieved by either bitwise not or abs()
        hash1 = Math.abs(hash1);

        // get the block of k ints
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        for (int i=0; i<k; i++) {
            int pos = hash(i+1, hash1, hash2);
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

        // hash1 needs to be positive, this could be achieved by either bitwise not or abs()
        hash1 = Math.abs(hash1);

        // get the block of k ints
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        for (int i=0; i<k; i++) {
            int pos = hash(i+1, hash1, hash2);
            // same as for hash1
            pos = Math.abs(pos);
            // if the bit at pos in block[i] is not set, return false
            if ((block[i] & 1 << pos) == 0) {
                return false;
            }
        }

        return true;
    }

    @Override
    public int size() {
        return n;
    }
}
