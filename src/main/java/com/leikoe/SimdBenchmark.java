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
    int[] test;

    @Benchmark
    public IntVector vectorLt() {
        VectorMask<Integer> mask = vr_test.lt(0);
        return vr_test.blend(vr_test.not(), mask);
    }

    @Benchmark
    public IntVector vectorAbs() {
        return vr_test.abs();
    }

    @Benchmark
    public int[] scalarAbs() {
        int[] abss = new int[test.length];
        for (int i=0; i<test.length; i++) {
            abss[i] = Math.abs(test[i]);
        }

        return abss;
    }

    @Benchmark
    public int[] scalarLt() {
        int[] lts = new int[test.length];
        for (int i=0; i<test.length; i++) {
            lts[i] = Math.abs(test[i]);
            if (test[i] < 0) {
                lts[i] = ~lts[i];
            }
        }

        return lts;
    }

    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark
//        System.out.println("Invokation");

        test = new int[]{random.nextInt(), random.nextInt(), random.nextInt(), random.nextInt()};
        vr_test = IntVector.fromArray(SPECIES, test, 0);
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration
//        System.out.println("Iteration");
    }
}