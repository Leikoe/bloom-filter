package com.leikoe;

import org.openjdk.jmh.annotations.*;

import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
public class Bencher {

    BloomFilter<Integer> arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(500, values);
    BloomFilter<Integer> linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(500, values);
    static int[] values = {12, 372, 3972};
    static int[] testValues = {232, 193, 22, 12, 372, 90, 3972};


    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }

    @Benchmark
    @Fork(value = 1, warmups = 0)
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.MICROSECONDS)
    public void measureArrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayListBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    @Fork(value = 1, warmups = 0)
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.MICROSECONDS)
    public void measureLinkedListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(linkedListBloomFilter.mightContain(i));
        }
    }
}
