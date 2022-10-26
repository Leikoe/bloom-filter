package com.leikoe;

import com.leikoe.hash.Utils;
import org.openjdk.jmh.annotations.*;

import java.nio.charset.StandardCharsets;
import java.util.Random;
import java.util.concurrent.TimeUnit;


@State(Scope.Benchmark)
@Threads(1)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@Warmup(iterations = 0, time = 1)
@Measurement(iterations = 1, time = 1)
@BenchmarkMode(Mode.AverageTime)
@Timeout(time = 10, timeUnit = TimeUnit.SECONDS)
public class ObjectToByteArrayBenchmark {

    Random random = new Random();

    Integer i;
    Double d;
    String s;

    // Integer to byte[]
    @Benchmark
    public byte[] serilizationInteger() {
        return Utils.objectToBytes(i);
    }

    @Benchmark
    public byte[] stringGetBytesInteger() {
        return Utils.objectToStringToBytes(i);
    }

    // Double to byte[]
    @Benchmark
    public byte[] serilizationDouble() {
        return Utils.objectToBytes(d);
    }

    @Benchmark
    public byte[] stringGetBytesDouble() {
        return Utils.objectToStringToBytes(d);
    }

    // String to byte[]
    @Benchmark
    public byte[] serilizationString() {
        return Utils.objectToBytes(s);
    }

    @Benchmark
    public byte[] stringGetBytesString() {
        return Utils.objectToStringToBytes(s);
    }

    @Setup(Level.Invocation)
    public void setupInvokation() throws Exception {
        // executed before each invocation of the benchmark

        i = random.nextInt();
        d = random.nextDouble();

        // https://www.baeldung.com/java-random-string random string implementation
        byte[] array = new byte[7]; // length is bounded by 7
        new Random().nextBytes(array);
        s = new String(array, StandardCharsets.UTF_8);
    }

    @Setup(Level.Iteration)
    public void setupIteration() throws Exception {
        // executed before each invocation of the iteration
    }

    public void benchmark() throws Exception {
        String[] argv = {};
        org.openjdk.jmh.Main.main(argv);
    }
}
