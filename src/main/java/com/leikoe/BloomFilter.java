package com.leikoe;

import java.util.List;
import java.util.function.ToIntFunction;

public class BloomFilter<T> implements IBloomFilter<T> {
    List<Boolean> bits;
    List<ToIntFunction<T>> hashFunctions;
    int size;

    public BloomFilter(List<Boolean> bitsContainer, List<ToIntFunction<T>> hashFunctions) {
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
}