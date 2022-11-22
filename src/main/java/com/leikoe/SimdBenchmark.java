package com.leikoe;

import jdk.incubator.vector.*;
import org.openjdk.jmh.annotations.*;

import java.util.Random;
import java.util.concurrent.TimeUnit;


@State(Scope.Benchmark)
@Threads(1)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 5, time = 1)
@Measurement(iterations = 5, time = 1)
@Fork(2)
@BenchmarkMode(Mode.AverageTime)
@Timeout(time = 10, timeUnit = TimeUnit.SECONDS)
public class SimdBenchmark {

    final VectorSpecies<Integer> SPECIES = IntVector.SPECIES_PREFERRED;
    Random random = new Random();
    IntVector vr_test;

    @Benchmark
    public IntVector lt() {
        VectorMask<Integer> mask = vr_test.lt(0);
        return vr_test.blend(vr_test.not(), mask);
    }

    @Benchmark
    public IntVector abs() {
        return vr_test.abs();
    }

    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark
//        System.out.println("Invokation");

        int[] arr = new int[]{944675, 237898, 38823, 2324};
        vr_test = IntVector.fromArray(SPECIES, arr, 0);
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration
//        System.out.println("Iteration");
    }
}