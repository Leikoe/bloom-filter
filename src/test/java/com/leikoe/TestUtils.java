package com.leikoe;

import com.leikoe.bitscontainers.BitArray;
import com.leikoe.bitscontainers.BitArrayList;
import com.leikoe.bitscontainers.BitLinkedList;
import com.leikoe.hash.MurmurHash2;

import java.util.ArrayList;
import java.util.List;
import java.util.function.ToIntFunction;


public class TestUtils {
    /**
     * Creates and returns a Hashfunction arrayList
     *
     * @return an example arrayList of hashFunctions
     */
    private static <T> List<ToIntFunction<T>> makeExampleHashFunctionArrayList() {
        List<ToIntFunction<T>> hashFunctions = new ArrayList<>();
        hashFunctions.add(new MurmurHash2<T>(23792387));
        hashFunctions.add(new MurmurHash2<T>(4256894));
        hashFunctions.add(new MurmurHash2<T>(99623));

        return hashFunctions;
    }

    /**
     * Fills up a bloom filter with a given array of values
     *
     * @param bloomFilter the bloom filter to fill up
     * @param values an array of values
     */
    private static <T> void fillBloomFilter(BloomFilter<T> bloomFilter, T[] values) {
        for (T i: values) {
            bloomFilter.add(i);
        }
    }

    public static <T> BloomFilter<T> makeExampleArrayListBloomFilter(int capacity, T[] values) {
        BloomFilter<T> arrayListBloomFilter = new BloomFilter<>(new BitArrayList(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(arrayListBloomFilter, values);

        return arrayListBloomFilter;
    }


    public static <T> BloomFilter<T> makeExampleLinkedListBloomFilter(int capacity, T[] values) {
        BloomFilter<T> linkedListBloomFilter = new BloomFilter<>(new BitLinkedList(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(linkedListBloomFilter, values);

        return linkedListBloomFilter;
    }

    public static <T> BloomFilter<T> makeExampleArrayBloomFilter(int capacity, T[] values) {
        BloomFilter<T> arrayBloomFilter = new BloomFilter<>(new BitArray(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(arrayBloomFilter, values);

        return arrayBloomFilter;
    }
}
