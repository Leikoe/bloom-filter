package com.leikoe;

import java.util.List;
import java.util.function.ToIntFunction;

import static com.leikoe.hash.Utils.positiveMod;


public class BloomFilter<T> implements IBloomFilter<T> {

    // we wish to have 1% or less
    public static final double FALSE_POSITIVE_RATE = 0.01;

    IBitsContainer bits;
    List<ToIntFunction<T>> hashFunctions;
    int size;

    /**
     * @param bitsContainer user provided bits container, all initialized to 0, must implement IBitsContainer
     * @param hashFunctions a generic list of hash functions from T to int
     *
     *                      This creates a BloomFilter instance using the provided bits container and hash functions
     */
    public BloomFilter(IBitsContainer bitsContainer, List<ToIntFunction<T>> hashFunctions) {
        this.bits = bitsContainer;
        this.size = 0;
        this.hashFunctions = hashFunctions;
    }

    @Override
    public void add(T value) {
        for (ToIntFunction<T> hashFunction: this.hashFunctions) {
            int pos = hashFunction.applyAsInt(value);
            bits.set(positiveMod(pos, bits.size()), true);
        }
        this.size++;
    }

    @Override
    public boolean mightContain(T value) {
        boolean all_true = true;
        for (int i=0; all_true && i<this.hashFunctions.size(); i++) {
            ToIntFunction<T> hashFunction = this.hashFunctions.get(i);
            int pos = hashFunction.applyAsInt(value);
            all_true = bits.get(positiveMod(pos, bits.size()));
        }

        return all_true;
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
        return (int) Math.ceil((-n * Math.log(FALSE_POSITIVE_RATE)) / Math.pow(Math.log(2), 2));
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
        return size;
    }
}
