package com.leikoe;

import java.util.List;
import java.util.function.ToIntFunction;


public class BloomFilter<T> implements IBloomFilter<T> {
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
            bits.set(pos% bits.size(), true);
        }
        this.size++;
    }

    @Override
    public boolean mightContain(T value) {
        boolean all_true = true;
        for (ToIntFunction<T> hashFunction: this.hashFunctions) {
            int pos = hashFunction.applyAsInt(value);
            boolean v = bits.get(pos % bits.size());
            all_true = all_true && v;
        }

        return all_true;
    }

    @Override
    public int size() {
        return size;
    }
}
