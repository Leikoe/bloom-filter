package com.leikoe;

import org.openjdk.jmh.annotations.*;

import java.util.concurrent.TimeUnit;

@State(Scope.Benchmark)
public class Bencher {

    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    public void measureArrayListBloomFilterContains(org.openjdk.jmh.infra.Blackhole bh) {
        int a = 1;
        int b = 2;
        int c = a + b;
        bh.consume(c);
    }
}
