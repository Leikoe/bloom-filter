package com.leikoe;

import org.openjdk.jmh.annotations.*;

import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
@Threads(Threads.MAX)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@Warmup(iterations = 0, time = 1)
@Measurement(iterations = 1, time = 1)
@BenchmarkMode(Mode.AverageTime)
@Timeout(time = 10, timeUnit = TimeUnit.SECONDS)
public class Bencher {

    @Param({"10", "100", "500", "1000", "10000", "100000"})
    public int size;

    static Random random = new Random();

    BloomFilter<Integer> arrayListBloomFilter;
    BloomFilter<Integer> linkedListBloomFilter;
    BloomFilter<Integer> arrayBloomFilter;

    BloomFilter<Integer> arrayListBloomFilterEmpty;
    BloomFilter<Integer> linkedListBloomFilterEmpty;
    BloomFilter<Integer> arrayBloomFilterEmpty;
    static Integer[] values = {12, 372, 3972};
    ArrayList<Integer> testValues;


    @Benchmark
    public void arrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayBloomFilter.mightContain(i));
        }
    }

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
    public void arrayBloomFilterAdd() {
        for (int i: testValues) {
            arrayBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void arrayListBloomFilterAdd() {
        for (int i: testValues) {
            arrayListBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void linkedListBloomFilterAdd() {
        for (int i: testValues) {
            linkedListBloomFilterEmpty.add(i);
        }
    }


    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark

        // clear all arrays Which are supposed to be empty (only if they're not clean)
        if (arrayBloomFilterEmpty == null || arrayBloomFilterEmpty.size() != 0) {
            arrayBloomFilterEmpty = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(size), values);
        }
        if (arrayListBloomFilterEmpty == null || arrayListBloomFilterEmpty.size() != 0) {
            arrayListBloomFilterEmpty = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(size), values);
        }
        if (linkedListBloomFilterEmpty == null || linkedListBloomFilterEmpty.size() != 0) {
            linkedListBloomFilterEmpty = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(size), values);
        }
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration

        // add test values
        testValues = new ArrayList<>();
        for(int i=0; i<size; i++) {
            testValues.add(random.nextInt());
        }

        // clear all arrays (only if they don't only contain the test values) and add half the values so half correct checks
        if (arrayBloomFilter == null || arrayBloomFilter.size() != size) {
           arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(size), values);
           for (int i = 0; i<testValues.size(); i++) {
                arrayBloomFilter.add(testValues.get(i));
           }
        }
        if (arrayListBloomFilter == null || arrayListBloomFilter.size() != size) {
            arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(size), values);
            for (int i = 0; i<testValues.size(); i++) {
                arrayListBloomFilter.add(testValues.get(i));
            }
        }
        if (linkedListBloomFilter == null || linkedListBloomFilter.size() != size) {
            linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(size), values);
            for (int i = 0; i<testValues.size(); i++) {
                linkedListBloomFilter.add(testValues.get(i));
            }
        }


    }

    public void benchmark() throws Exception {
        String[] argv = {};
        org.openjdk.jmh.Main.main(argv);
    }
}
