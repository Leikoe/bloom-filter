package com.leikoe;

import com.leikoe.hash.MurmurHash2;
import org.openjdk.jmh.annotations.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.TimeUnit;
import java.util.function.ToIntFunction;

@State(Scope.Benchmark)
public class Bencher {

    BloomFilter<Integer> arrayListBloomFilter = Bencher.makeExampleArrayListBloomFilter(500, values);
    static int[] values = {12, 372, 3972};
    static int[] testValues = {232, 193, 22, 12, 372, 90, 3972};

    public static BloomFilter<Integer> makeExampleArrayListBloomFilter(int capacity, int[] values) {
        List<Boolean> boolArrayList = new ArrayList<>(capacity);
        for (int i=0; i<500; i++)
            boolArrayList.add(false);

        List<ToIntFunction<Integer>> hashFunctions = new ArrayList<>();
        hashFunctions.add(new MurmurHash2<Integer>(23792387));

        BloomFilter<Integer> arrayListBloomFilter = new BloomFilter<>(boolArrayList, hashFunctions);
        for (int i: values) {
            arrayListBloomFilter.add(i);
        }
        return arrayListBloomFilter;
    }

    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    public void measureArrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: values) {
            bh.consume(arrayListBloomFilter.mightContain(i));
        }
    }
}
