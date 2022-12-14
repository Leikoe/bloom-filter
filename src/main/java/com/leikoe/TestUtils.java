package com.leikoe;

import com.leikoe.bitscontainers.*;

import java.util.ArrayList;
import java.util.List;
import java.util.function.ToIntFunction;


public class TestUtils {
    /**
     * Fills up a bloom filter with a given array of values
     *
     * @param bloomFilter the bloom filter to fill up
     * @param values an array of values
     */
     public static <T> void fillBloomFilter(IBloomFilter<T> bloomFilter, T[] values) {
        for (T i: values) {
            bloomFilter.add(i);
        }
    }

    public static <T> BloomFilter<T> makeExampleBloomFilter(int expectedInsertCount) {
        return new BloomFilter<>(expectedInsertCount);
    }

    public static <T> UFBF<T> makeExampleUFBF(int expectedInsertCount) {
        return new UFBF<>(expectedInsertCount);
    }

    public static <T> NaiveBloomFilter<T> makeExampleArrayBloomFilter(int expectedInsertCount) {
        int optimalSize = NaiveBloomFilter.getOptimalSize(expectedInsertCount);
        BitArray bc = new BitArray(optimalSize);

        return new NaiveBloomFilter<>(bc, expectedInsertCount);
    }

    public static <T> NaiveBloomFilter<T> makeExampleNativeBitSetBloomFilter(int expectedInsertCount) {
        int optimalSize = NaiveBloomFilter.getOptimalSize(expectedInsertCount);
        NativeBitSet bc = new NativeBitSet(optimalSize);

        return new NaiveBloomFilter<>(bc, expectedInsertCount);
    }

    public static <T> NaiveBloomFilter<T> makeExampleArrayListBloomFilter(int expectedInsertCount) {
        int optimalSize = NaiveBloomFilter.getOptimalSize(expectedInsertCount);
        BitArray bc = new BitArray(optimalSize);

        return new NaiveBloomFilter<>(bc, expectedInsertCount);
    }


    public static <T> NaiveBloomFilter<T> makeExampleGuavaLockFreeBitArrayBloomFilter(int expectedInsertCount) {
        int optimalSize = NaiveBloomFilter.getOptimalSize(expectedInsertCount);
        GuavaLockFreeBitArray bc = new GuavaLockFreeBitArray(optimalSize);

        return new NaiveBloomFilter<>(bc, expectedInsertCount);
    }
    public static <T> NaiveBloomFilter<T> makeExampleLinkedListBloomFilter(int expectedInsertCount) {
        int optimalSize = NaiveBloomFilter.getOptimalSize(expectedInsertCount);
        BitLinkedList bc = new BitLinkedList(optimalSize);

        return new NaiveBloomFilter<>(bc, expectedInsertCount);
    }
}
