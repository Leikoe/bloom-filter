package com.leikoe;

import org.openjdk.jmh.annotations.*;

import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
@Threads(1)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@Warmup(iterations = 0, time = 1)
@Measurement(iterations = 1, time = 1)
@BenchmarkMode(Mode.AverageTime)
public class Bencher {

    @Param({"10", "100", "500", "1000", "10000", "250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000"})
    public int size;

    BloomFilter<Integer> arrayListBloomFilter;
    BloomFilter<Integer> linkedListBloomFilter;
    BloomFilter<Integer> arrayBloomFilter;
    static Integer[] values = {12, 372, 3972};
    static Integer[] testValues = {232, 193, 22, 12, 372, 90, 3972};

    @Benchmark
    public void arrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayListBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void linkedListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(linkedListBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void arrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void arrayListBloomFilterAdd() {
        for (int i: testValues) {
            arrayListBloomFilter.add(i);
        }
    }

    @Benchmark
    public void linkedListBloomFilterAdd() {
        for (int i: testValues) {
            linkedListBloomFilter.add(i);
        }
    }

    @Benchmark
    public void arrayBloomFilterAdd() {
        for (int i: testValues) {
            arrayBloomFilter.add(i);
        }
    }

    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration

        if (arrayBloomFilter == null || arrayListBloomFilter.size() != values.length) {
            arrayBloomFilter = TestUtils.makeExampleArrayListBloomFilter(size, values);
        }
        if (arrayListBloomFilter == null || arrayListBloomFilter.size() != values.length) {
            arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(size, values);
        }
        if (linkedListBloomFilter == null || linkedListBloomFilter.size() != values.length) {
            linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(size, values);
        }
    }

    public void benchmark() throws Exception {
        String[] argv = {};
        org.openjdk.jmh.Main.main(argv);
    }
}
