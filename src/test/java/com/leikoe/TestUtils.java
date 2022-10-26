package com.leikoe;

import com.leikoe.bitscontainers.BitArray;
import com.leikoe.bitscontainers.BitArrayList;
import com.leikoe.bitscontainers.BitLinkedList;
import com.leikoe.hash.Fnv32Hash;
import com.leikoe.hash.JavaHash;
import com.leikoe.hash.MurmurHash2;
import com.leikoe.hash.djb33Hash;

import java.util.ArrayList;
import java.util.List;
import java.util.function.ToIntFunction;


public class TestUtils {
    /**
     * Creates and returns a Hashfunction arrayList
     *
     * @return an example arrayList of hashFunctions
     */
    private static <T> List<ToIntFunction<T>> makeExampleHashFunctionArrayList(int n) {
        List<ToIntFunction<T>> hashFunctions = new ArrayList<>();
        hashFunctions.add(new MurmurHash2<T>(23792387));
        if (n > 1) {
            hashFunctions.add(new JavaHash<>());
        }
        if (n > 2) {
            hashFunctions.add(new djb33Hash<>());
        }
        if (n > 3) {
            hashFunctions.add(new Fnv32Hash<>());
        }

        return hashFunctions;
    }

    /**
     * Fills up a bloom filter with a given array of values
     *
     * @param bloomFilter the bloom filter to fill up
     * @param values an array of values
     */
     public static <T> void fillBloomFilter(BloomFilter<T> bloomFilter, T[] values) {
        for (T i: values) {
            bloomFilter.add(i);
        }
    }

    public static <T> BloomFilter<T> makeExampleArrayBloomFilter(int capacity) {
        int optimalSize = BloomFilter.getOptimalSize(capacity);
        BitArray bc = new BitArray(optimalSize);
        BloomFilter<T> arrayBloomFilter = new BloomFilter<>(bc, makeExampleHashFunctionArrayList(
                BloomFilter.getOptimalNumberOfHashFunctions(capacity, optimalSize)
        ));

        return arrayBloomFilter;
    }

    public static <T> BloomFilter<T> makeExampleArrayListBloomFilter(int capacity) {
        int optimalSize = BloomFilter.getOptimalSize(capacity);
        BitArray bc = new BitArray(optimalSize);
        BloomFilter<T> arrayListBloomFilter = new BloomFilter<>(bc, makeExampleHashFunctionArrayList(
                BloomFilter.getOptimalNumberOfHashFunctions(capacity, optimalSize)
        ));

        return arrayListBloomFilter;
    }

    public static <T> BloomFilter<T> makeExampleLinkedListBloomFilter(int capacity) {
        int optimalSize = BloomFilter.getOptimalSize(capacity);
        BitLinkedList bc = new BitLinkedList(optimalSize);
        BloomFilter<T> linkedListBloomFilter = new BloomFilter<>(bc, makeExampleHashFunctionArrayList(
                BloomFilter.getOptimalNumberOfHashFunctions(capacity, optimalSize)
        ));

        return linkedListBloomFilter;
    }
}
