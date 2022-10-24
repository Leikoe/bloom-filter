package com.leikoe;

import com.leikoe.hash.MurmurHash2;

import java.util.ArrayList;
import java.util.LinkedList;
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

    public static BloomFilter<Integer> makeExampleArrayListBloomFilter(int capacity, int[] values) {
        List<Boolean> boolArrayList = new ArrayList<>(capacity);
        for (int i=0; i<capacity; i++)
            boolArrayList.add(false);

        BloomFilter<Integer> arrayListBloomFilter = new BloomFilter<>(boolArrayList, makeExampleHashFunctionArrayList());
        for (int i: values) {
            arrayListBloomFilter.add(i);
        }
        return arrayListBloomFilter;
    }

    public static BloomFilter<Integer> makeExampleLinkedListBloomFilter(int capacity, int[] values) {
        List<Boolean> boolArrayList = new LinkedList<>();
        for (int i=0; i<capacity; i++)
            boolArrayList.add(false);

        List<ToIntFunction<Integer>> hashFunctions = new ArrayList<>();
        hashFunctions.add(new MurmurHash2<Integer>(23792387));

        BloomFilter<Integer> arrayListBloomFilter = new BloomFilter<>(boolArrayList, makeExampleHashFunctionArrayList());
        for (int i: values) {
            arrayListBloomFilter.add(i);
        }
        return arrayListBloomFilter;
    }

    // TODO: make this work
//    public static BloomFilter<Integer> makeExampleArrayBloomFilter(int capacity, int[] values) {
//        List<Boolean> boolArrayList = new int[capacity];
//        for (int i=0; i<500; i++)
//            boolArrayList.add(false);
//
//        List<ToIntFunction<Integer>> hashFunctions = new ArrayList<>();
//        hashFunctions.add(new MurmurHash2<Integer>(23792387));
//
//        BloomFilter<Integer> arrayListBloomFilter = new BloomFilter<>(boolArrayList, hashFunctions);
//        for (int i: values) {
//            arrayListBloomFilter.add(i);
//        }
//        return arrayListBloomFilter;
//    }
}
