package com.leikoe;

import com.leikoe.bitscontainers.BlockBitSet;
import com.leikoe.hash.Murmur64;

import static com.leikoe.NaiveBloomFilter.getOptimalNumberOfHashFunctions;
import static com.leikoe.NaiveBloomFilter.getOptimalSize;

public class BloomFilter<T> implements IBloomFilter<T> {
    protected IBitsBlocksContainer bits;
    protected int n;
    protected final int k;

    /**
     * Constructor
     * This creates a BloomFilter instance using the provided expected insert count
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
     * Constructor
     * This creates a BloomFilter instance using the provided expected insert count and the multiple of k to round k to (eg: 8)
     *
     * @param km multiple of k to round k to
     * @param expectedInsertCount the expected number of add() calls
     */
    public BloomFilter(int expectedInsertCount, int km) {
        int m = getOptimalSize(expectedInsertCount);
        int k1 = Math.floorDiv(getOptimalNumberOfHashFunctions(expectedInsertCount, m), km) * km;
        this.k = Math.max(k1, km);
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
        return hash1 + (seed * hash2);
    }

    /**
     * Insert a value in the filter
     * this was implemented using the white paper "Ultra-Fast Bloom Filters using SIMD Techniques" by Jianyuan Lu
     * (this is the scalar implementation of the hashing technique, see UFBF class for vector implementation)
     *
     * @param value the value to add to the filter
     */
    public void add(T value) {
        long hash64 = Murmur64.hash(value.hashCode());

        // get the 32 high bits and the 32 low bits
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);

        // hashes needs to be positive, this could be achieved by either bitwise not or abs()
        // TODO: fix comment under
        // if h1 & h2 > 0 then For any k > 0, h2 + k * h1 > 0, and no need for an expensive abs call
        hash1 = Math.abs(hash1);

        // get the block of k ints
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        for (int i=0; i<k; i++) {
            int pos = hash(i+1, hash1, hash2);
            // set the bit at pos in block[i] to true
            block[i] |= 1 << pos;
        }

        // no need to call bits.setBlock() because block is a reference
        this.n++;
    }

    /**
     * Membership check function
     *
     * @param value the value to check membership for
     * @return whether the value is in the filter or not
     */
    @Override
    public boolean mightContain(T value) {
        long hash64 = Murmur64.hash(value.hashCode());

        // get the 32 high bits and the 32 low bits
        int hash1 = (int) hash64;
        int hash2 = (int) (hash64 >>> 32);

        // hashes needs to be positive, this could be achieved by either bitwise not or abs()
        // TODO: fix comment under
        // if h1 & h2 > 0 then For any k > 0, h2 + k * h1 > 0, and no need for an expensive abs call
        hash1 = Math.abs(hash1);

        // get the block of k ints
        int[] block = bits.getBlock(hash1 % bits.blockCount());

        for (int i=0; i<k; i++) {
            int pos = hash(i+1, hash1, hash2);
            // if the bit at pos in block[i] is not set, return false
            int b = ~block[i];
            int test = (1 << pos) & b;
            if (test != 0) {
                return false;
            }
        }

        return true;
    }

    /**
     * Main function used to create a filter and add i > JIT_THRESHOLD elements, to extract machine code (asm) of the add method
     * note: the jit compiler won't compile a function into machine code unless it runs more than JIT_THRESHOLD times
     *
     * @param args cli args
     */
    public static void main(String[] args) {
        IBloomFilter<Integer> filter = new BloomFilter<>(200_000);
        for (int i = 0; i < 200_000; i++) {
            filter.add(69);
        }
    }

    /**
     * Get the size of the filter
     *
     * @return the number of elements in the filter
     */
    @Override
    public int size() {
        return n;
    }
}
