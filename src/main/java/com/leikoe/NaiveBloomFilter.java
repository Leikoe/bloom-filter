package com.leikoe;

import static com.leikoe.hash.Utils.positiveMod;


public class NaiveBloomFilter<T> implements IBloomFilter<T> {


    // we wish to have 1% or less false positives
    public static final double FALSE_POSITIVE_RATE = 0.01;

    IBitsContainer bits;
    int n;
    int k;

    long[] hashes;

    /**
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param bitsContainer user provided bits container, all initialized to 0, must implement IBitsContainer
     */
    public NaiveBloomFilter(IBitsContainer bitsContainer, int expectedInsertCount) {
        this.bits = bitsContainer;
        assert (bits.size() >= getOptimalSize(expectedInsertCount));
        this.n = 0;
        this.k = getOptimalNumberOfHashFunctions(expectedInsertCount, bits.size());
        hashes = new long[]{0, 0};
    }


    @Override
    public void add(T value) {
        for (int i=0; i<k; i++) {
            long pos = hash(value, i);
            bits.set((int) positiveMod(pos, bits.size()), true);
        }
        this.n++;
    }

    @Override
    public boolean mightContain(T value) {
        boolean all_true = true;

        for (int i=0; all_true && i<this.k; i++) {
            long pos = hash(value, i);
            all_true = bits.get((int) positiveMod(pos, bits.size()));
        }

        return all_true;
    }

    // from https://github.com/jedisct1/rust-bloom-filter/blob/master/src/lib.rs bloom_hash function
    long hash(T value, int k) {
        if (k == 0) {
            return (hashes[0] = value.hashCode());
        } else if (k == 1) {
            // inlined HashMapHash using object::hashcode from k == 1 (last hash() call)
            return hashes[1] = (hashes[1] = hashes[0]) ^ (hashes[0] >> 16);
        } else {
                return hashes[0] + (k * hashes[1]) % 0xffffffc5;
        }
    }

    /**
     * Formulas from <a href="https://andybui01.github.io/bloom-filter/#implementation-and-benchmark">this paper</a>
     * we use the ceil function because it's worse to have a smaller container than a bigger one for collisions
     *
     * @param n the number of elements to be inserted in the filter
     * @param e the false positive rate
     * @return the optimal bits container size
     */
    public static int getOptimalSize(int n, double e) {
        return (int) Math.ceil((-n * Math.log(e)) / Math.pow(Math.log(2), 2));
    }

    /**
     * Formulas from <a href="https://andybui01.github.io/bloom-filter/#implementation-and-benchmark">this paper</a>
     * we use the ceil function because it's worse to have a smaller container than a bigger one for collisions
     *
     * @param n the number of elements to be inserted in the filter
     * @return the optimal bits container size
     */
    public static int getOptimalSize(int n) {
        double size = -(n * Math.log(FALSE_POSITIVE_RATE)) / Math.pow(Math.log(2.), 2.);
        return (int) Math.ceil(size);
    }

    /**
     * Formulas from <a href="https://andybui01.github.io/bloom-filter/#implementation-and-benchmark">this paper</a>
     * we use the ceil function because in case of a 0. result, we need to get atleast one hash function
     *
     * @param n the number of elements to be inserted in the filter
     * @param m the size of the bits container
     * @return the optimal number of hash functions
     */
    public static int getOptimalNumberOfHashFunctions(int n, int m) {
        return (int) Math.ceil((m/(double) n) * Math.log(2));
    }

    @Override
    public int size() {
        return n;
    }
}
