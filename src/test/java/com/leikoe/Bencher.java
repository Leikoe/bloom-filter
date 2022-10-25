package com.leikoe;

import org.junit.Test;
import org.openjdk.jmh.annotations.*;

import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
@Threads(1)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@Warmup(iterations = 0, time = 1)
@Measurement(iterations = 1, time = 1)
@BenchmarkMode(Mode.All)
public class Bencher {

    @Param({"232","193","22", "12", "372", "90", "3972"})
    public int value;

    BloomFilter<Integer> arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(500, values);
    BloomFilter<Integer> linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(500, values);
    BloomFilter<Integer> arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(500, values);
    static int[] values = {12, 372, 3972};
    static int[] testValues = {232, 193, 22, 12, 372, 90, 3972};

    @Benchmark
    public void arrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        bh.consume(arrayListBloomFilter.mightContain(value));
    }

    @Benchmark
    public void linkedListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        bh.consume(linkedListBloomFilter.mightContain(value));
    }

    @Benchmark
    public void arrayBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        bh.consume(arrayBloomFilter.mightContain(value));
    }

    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration
    }

    @Test
    public void benchmark() throws Exception {
        String[] argv = {};
        org.openjdk.jmh.Main.main(argv);
    }
}
