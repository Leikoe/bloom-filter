package com.leikoe;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;
import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
@Threads(1)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@Warmup(iterations = 0, time = 1)
@Measurement(iterations = 1, time = 1)
@BenchmarkMode(Mode.AverageTime)
@Timeout(time = 10, timeUnit = TimeUnit.SECONDS)
public class Bencher {

    // n is the number of elements in the filter
    @Param({"2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192"})
    public int items;

    static Random random = new Random();

    BloomFilter<Integer> arrayListBloomFilter;
    BloomFilter<Integer> linkedListBloomFilter;
    BloomFilter<Integer> arrayBloomFilter;
    BloomFilter<Integer> nativeBitSetBloomFilter;

    BloomFilter<Integer> arrayListBloomFilterEmpty;
    BloomFilter<Integer> linkedListBloomFilterEmpty;
    BloomFilter<Integer> arrayBloomFilterEmpty;
    BloomFilter<Integer> nativeBitSetBloomFilterEmpty;

    HashSet<Integer> hashsetEmpty;
    HashSet<Integer> hashset;
    ArrayList<Integer> testValues;


    @Benchmark
    public void arrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void nativeBitSetBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(nativeBitSetBloomFilter.mightContain(i));
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
    public void hashsetContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(hashset.contains(i));
        }
    }


    @Benchmark
    public void arrayBloomFilterAdd() {
        for (int i: testValues) {
            arrayBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void nativeBitSetBloomFilterAdd() {
        for (int i: testValues) {
            nativeBitSetBloomFilterEmpty.add(i);
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

    @Benchmark
    public void hashsetAdd() {
        for (Integer i: testValues) {
            hashsetEmpty.add(i);
        }
    }

    @Benchmark
    public void hashsetAddAll() {
        hashsetEmpty.addAll(testValues);
    }


    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark

        // clear all arrays Which are supposed to be empty (only if they're not clean)
        if (arrayBloomFilterEmpty == null || arrayBloomFilterEmpty.size() != 0) {
            arrayBloomFilterEmpty = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(items));
        }
        if (nativeBitSetBloomFilterEmpty == null || nativeBitSetBloomFilterEmpty.size() != 0) {
            nativeBitSetBloomFilterEmpty = TestUtils.makeExampleNativeBitSetBloomFilter(BloomFilter.getOptimalSize(items));
        }
        if (arrayListBloomFilterEmpty == null || arrayListBloomFilterEmpty.size() != 0) {
            arrayListBloomFilterEmpty = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(items));
        }
        if (linkedListBloomFilterEmpty == null || linkedListBloomFilterEmpty.size() != 0) {
            linkedListBloomFilterEmpty = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(items));
        }

        if (hashsetEmpty == null || hashsetEmpty.size() != 0) {
            hashsetEmpty = new HashSet<>(items);
        }
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration

        // add test values
        testValues = new ArrayList<>();
        for(int i = 0; i< items; i++) {
            testValues.add(random.nextInt());
        }

        // clear all arrays (only if they don't only contain the test values) and add half the values so half correct checks
        if (arrayBloomFilter == null || arrayBloomFilter.size() != items /2) {
           arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(items));
           for (int i = 0; i<testValues.size()/2; i++) {
                arrayBloomFilter.add(testValues.get(i));
           }
        }
        if (nativeBitSetBloomFilter == null || nativeBitSetBloomFilter.size() != items /2) {
           nativeBitSetBloomFilter = TestUtils.makeExampleNativeBitSetBloomFilter(BloomFilter.getOptimalSize(items));
           for (int i = 0; i<testValues.size()/2; i++) {
                nativeBitSetBloomFilter.add(testValues.get(i));
           }
        }
        if (arrayListBloomFilter == null || arrayListBloomFilter.size() != items /2) {
            arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(items));
            for (int i = 0; i<testValues.size()/2; i++) {
                arrayListBloomFilter.add(testValues.get(i));
            }
        }
        if (linkedListBloomFilter == null || linkedListBloomFilter.size() != items /2) {
            linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(items));
            for (int i = 0; i<testValues.size()/2; i++) {
                linkedListBloomFilter.add(testValues.get(i));
            }
        }

        if (hashset == null || hashset.size() != items /2) {
            hashset = new HashSet<>(items);
            for (int i=0; i<testValues.size()/2; i++) {
                hashset.add(testValues.get(i));
            }
        }
    }

    /**
     * To run this benchmark class:
     *
     * java -cp target/benchmarks.jar com.leikoe.Bencher
     *
     * @param args
     * @throws RunnerException
     */
    public static void main(String[] args) throws RunnerException {
        Options options = new OptionsBuilder()
                .include(Bencher.class.getSimpleName())
                .forks(1)
                .build();

        new Runner(options).run();
    }
}
