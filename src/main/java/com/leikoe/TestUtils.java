package com.leikoe;

import com.leikoe.bitscontainers.*;
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
//        hashFunctions.add(new MurmurHash2<T>(23792387));
//        if (n > 1) {
//            hashFunctions.add(new JavaHash<>());
//        }
//        if (n > 2) {
//            hashFunctions.add(new djb33Hash<>());
//        }
//        if (n > 3) {
//            hashFunctions.add(new Fnv32Hash<>());
//        }
        hashFunctions.add(Object::hashCode);

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

    public static <T> VectorizedBloomFilter<T> makeExampleVectorizedArrayBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        BitArray bc = new BitArray(optimalSize);

        return new VectorizedBloomFilter<>(bc, expectedInsertCount);
    }

    public static <T> UFBF<T> makeExampleUFBF(int expectedInsertCount) {
        return new UFBF<>(expectedInsertCount);
    }

    public static <T> BloomFilter<T> makeExampleArrayBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        BitArray bc = new BitArray(optimalSize);

        return new BloomFilter<>(bc, expectedInsertCount);
    }

    public static <T> BloomFilter<T> makeExampleNativeBitSetBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        NativeBitSet bc = new NativeBitSet(optimalSize);

        return new BloomFilter<>(bc, expectedInsertCount);
    }

    public static <T> BloomFilter<T> makeExampleArrayListBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        BitArray bc = new BitArray(optimalSize);

        return new BloomFilter<>(bc, expectedInsertCount);
    }


    public static <T> BloomFilter<T> makeExampleGuavaLockFreeBitArrayBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        GuavaLockFreeBitArray bc = new GuavaLockFreeBitArray(optimalSize);

        return new BloomFilter<>(bc, expectedInsertCount);
    }
    public static <T> BloomFilter<T> makeExampleLinkedListBloomFilter(int expectedInsertCount) {
        int optimalSize = BloomFilter.getOptimalSize(expectedInsertCount);
        BitLinkedList bc = new BitLinkedList(optimalSize);

        return new BloomFilter<>(bc, expectedInsertCount);
    }
}
