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
@Fork(1)
@Warmup(iterations = 2, time = 1)
@Measurement(iterations = 5, time = 1)
@BenchmarkMode(Mode.AverageTime)
@Timeout(time = 10, timeUnit = TimeUnit.SECONDS)
public class Bencher {

    // n is the number of elements in the filter
    @Param({
//            "2",
//            "4",
//            "8",
//            "16",
//            "32",
//            "64",
//            "128",
//            "256",
//            "512",
//            "1024",
//            "2048",
//            "4096",
//            "8192",
//            "16384",
//            "32768",
//            "65536"
            "100",
            "1000",
            "10000",
            "100000",
//            "1000000",
//            "10000000"
    })
    public int items;

    static Random random = new Random();


    UFBF<Integer> ufbf;
    VectorizedBloomFilter<Integer> vectorizedArrayBloomFilter;
    NaiveBloomFilter<Integer> arrayListNaiveBloomFilter;
    NaiveBloomFilter<Integer> linkedListNaiveBloomFilter;
    NaiveBloomFilter<Integer> arrayNaiveBloomFilter;
    NaiveBloomFilter<Integer> nativeBitSetNaiveBloomFilter;

    NaiveBloomFilter<Integer> guavaLockFreeBitArrayNaiveBloomFilter;



    UFBF<Integer> ufbfEmpty;
    VectorizedBloomFilter<Integer> vectorizedArrayBloomFilterEmpty;
    NaiveBloomFilter<Integer> arrayListNaiveBloomFilterEmpty;
    NaiveBloomFilter<Integer> linkedListNaiveBloomFilterEmpty;
    NaiveBloomFilter<Integer> arrayNaiveBloomFilterEmpty;
    NaiveBloomFilter<Integer> nativeBitSetNaiveBloomFilterEmpty;

    NaiveBloomFilter<Integer> guavaLockFreeBitArrayNaiveBloomFilterEmpty;

    HashSet<Integer> hashsetEmpty;
    HashSet<Integer> hashset;
    ArrayList<Integer> testValues;

    @Benchmark
    public void ubfbContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(ufbf.mightContain(i));
        }
    }
    @Benchmark
    public void vectorizedArrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(vectorizedArrayBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void arrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayNaiveBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void nativeBitSetBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(nativeBitSetNaiveBloomFilter.mightContain(i));
        }
    }

//    @Benchmark
    public void guavaLockFreeBitArrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(guavaLockFreeBitArrayNaiveBloomFilter.mightContain(i));
        }
    }

//    @Benchmark
    public void arrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(arrayListNaiveBloomFilter.mightContain(i));
        }
    }

//    @Benchmark
    public void linkedListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(linkedListNaiveBloomFilter.mightContain(i));
        }
    }

    @Benchmark
    public void hashsetContains(org.openjdk.jmh.infra.Blackhole bh) {
        for (int i: testValues) {
            bh.consume(hashset.contains(i));
        }
    }


    @Benchmark
    public void ufbfAdd() {
        for (int i: testValues) {
            ufbfEmpty.add(i);
        }
    }
    @Benchmark
    public void vectorizedArrayBloomFilterAdd() {
        for (int i: testValues) {
            vectorizedArrayBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void arrayBloomFilterAdd() {
        for (int i: testValues) {
            arrayNaiveBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void nativeBitSetBloomFilterAdd() {
        for (int i: testValues) {
            nativeBitSetNaiveBloomFilterEmpty.add(i);
        }
    }

//    @Benchmark
    public void guavaLockFreeBitArrayBloomFilterAdd() {
        for (int i: testValues) {
            guavaLockFreeBitArrayNaiveBloomFilterEmpty.add(i);
        }
    }

//    @Benchmark
    public void arrayListBloomFilterAdd() {
        for (int i: testValues) {
            arrayListNaiveBloomFilterEmpty.add(i);
        }
    }

//    @Benchmark
    public void linkedListBloomFilterAdd() {
        for (int i: testValues) {
            linkedListNaiveBloomFilterEmpty.add(i);
        }
    }

    @Benchmark
    public void hashsetAdd() {
        for (Integer i: testValues) {
            hashsetEmpty.add(i);
        }
    }

//    @Benchmark
    public void hashsetAddAll() {
        hashsetEmpty.addAll(testValues);
    }


    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark

        // clear all arrays Which are supposed to be empty (only if they're not clean)
        if (ufbfEmpty == null || ufbfEmpty.size() != 0) {
            ufbfEmpty = TestUtils.makeExampleUFBF(items);
        }
        if (vectorizedArrayBloomFilterEmpty == null || vectorizedArrayBloomFilterEmpty.size() != 0) {
            vectorizedArrayBloomFilterEmpty = TestUtils.makeExampleVectorizedArrayBloomFilter(items);
        }

        if (arrayNaiveBloomFilterEmpty == null || arrayNaiveBloomFilterEmpty.size() != 0) {
            arrayNaiveBloomFilterEmpty = TestUtils.makeExampleArrayBloomFilter(items);
        }
        if (nativeBitSetNaiveBloomFilterEmpty == null || nativeBitSetNaiveBloomFilterEmpty.size() != 0) {
            nativeBitSetNaiveBloomFilterEmpty = TestUtils.makeExampleNativeBitSetBloomFilter(items);
        }
        if (guavaLockFreeBitArrayNaiveBloomFilterEmpty == null || guavaLockFreeBitArrayNaiveBloomFilterEmpty.size() != 0) {
            guavaLockFreeBitArrayNaiveBloomFilterEmpty = TestUtils.makeExampleGuavaLockFreeBitArrayBloomFilter(items);
        }
        if (arrayListNaiveBloomFilterEmpty == null || arrayListNaiveBloomFilterEmpty.size() != 0) {
            arrayListNaiveBloomFilterEmpty = TestUtils.makeExampleArrayListBloomFilter(items);
        }
//        if (linkedListBloomFilterEmpty == null || linkedListBloomFilterEmpty.size() != 0) {
//            linkedListBloomFilterEmpty = TestUtils.makeExampleLinkedListBloomFilter(items);
//        }

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
        if (ufbf == null || ufbf.size() != items /2) {
           ufbf = TestUtils.makeExampleUFBF(items);
           for (int i = 0; i<testValues.size()/2; i++) {
                ufbf.add(testValues.get(i));
           }
        }
        if (vectorizedArrayBloomFilter == null || vectorizedArrayBloomFilter.size() != items /2) {
           vectorizedArrayBloomFilter = TestUtils.makeExampleVectorizedArrayBloomFilter(items);
           for (int i = 0; i<testValues.size()/2; i++) {
                vectorizedArrayBloomFilter.add(testValues.get(i));
           }
        }

        if (arrayNaiveBloomFilter == null || arrayNaiveBloomFilter.size() != items /2) {
           arrayNaiveBloomFilter = TestUtils.makeExampleArrayBloomFilter(items);
           for (int i = 0; i<testValues.size()/2; i++) {
                arrayNaiveBloomFilter.add(testValues.get(i));
           }
        }
        if (nativeBitSetNaiveBloomFilter == null || nativeBitSetNaiveBloomFilter.size() != items /2) {
           nativeBitSetNaiveBloomFilter = TestUtils.makeExampleNativeBitSetBloomFilter(items);
           for (int i = 0; i<testValues.size()/2; i++) {
                nativeBitSetNaiveBloomFilter.add(testValues.get(i));
           }
        }
        if (guavaLockFreeBitArrayNaiveBloomFilter == null || guavaLockFreeBitArrayNaiveBloomFilter.size() != items /2) {
           guavaLockFreeBitArrayNaiveBloomFilter = TestUtils.makeExampleGuavaLockFreeBitArrayBloomFilter(items);
           for (int i = 0; i<testValues.size()/2; i++) {
                guavaLockFreeBitArrayNaiveBloomFilter.add(testValues.get(i));
           }
        }
        if (arrayListNaiveBloomFilter == null || arrayListNaiveBloomFilter.size() != items /2) {
            arrayListNaiveBloomFilter = TestUtils.makeExampleArrayListBloomFilter(items);
            for (int i = 0; i<testValues.size()/2; i++) {
                arrayListNaiveBloomFilter.add(testValues.get(i));
            }
        }
//        if (linkedListBloomFilter == null || linkedListBloomFilter.size() != items /2) {
//            linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(items);
//            for (int i = 0; i<testValues.size()/2; i++) {
//                linkedListBloomFilter.add(testValues.get(i));
//            }
//        }

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
