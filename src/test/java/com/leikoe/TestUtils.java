package com.leikoe;

import com.leikoe.bitscontainers.BitArray;
import com.leikoe.bitscontainers.BitArrayList;
import com.leikoe.bitscontainers.BitLinkedList;
import com.leikoe.hash.MurmurHash2;

import java.util.ArrayList;
import java.util.List;
import java.util.function.ToIntFunction;


public class TestUtils {
    private static List<ToIntFunction<Integer>> makeExampleHashFunctionArrayList() {
        List<ToIntFunction<Integer>> hashFunctions = new ArrayList<>();
        hashFunctions.add(new MurmurHash2<Integer>(23792387));
        hashFunctions.add(x -> (int) (Math.pow(x, 2) - 6));
        hashFunctions.add(x -> (int) (Math.abs(x + 7) / 3));

        return hashFunctions;
    }

    private static void fillBloomFilter(BloomFilter<Integer> bloomFilter, int[] values) {
        for (int i: values) {
            bloomFilter.add(i);
        }
    }

    public static BloomFilter<Integer> makeExampleArrayListBloomFilter(int capacity, int[] values) {
        BloomFilter<Integer> arrayListBloomFilter = new BloomFilter<>(new BitArrayList(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(arrayListBloomFilter, values);
        return arrayListBloomFilter;
    }


    public static BloomFilter<Integer> makeExampleLinkedListBloomFilter(int capacity, int[] values) {
        BloomFilter<Integer> linkedListBloomFilter = new BloomFilter<>(new BitLinkedList(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(linkedListBloomFilter, values);
        return linkedListBloomFilter;
    }

    public static BloomFilter<Integer> makeExampleArrayBloomFilter(int capacity, int[] values) {
        BloomFilter<Integer> arrayBloomFilter = new BloomFilter<>(new BitArray(capacity), makeExampleHashFunctionArrayList());
        fillBloomFilter(arrayBloomFilter, values);
        return arrayBloomFilter;
    }
}
