package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

import java.math.RoundingMode;
import java.util.concurrent.atomic.AtomicLongArray;

/**
 * From Google's guava source code // <a href="https://github.com/google/guava/blob/master/guava/src/com/google/common/hash/BloomFilterStrategies.java">...</a>
 *
 * Models a lock-free array of bits.
 *
 * <p>We use this instead of java.util.BitSet because we need access to the array of longs and we
 * need compare-and-swap.
 */
public final class GuavaLockFreeBitArray implements IBitsContainer {
    private static final int LONG_ADDRESSABLE_BITS = 6;
    final AtomicLongArray data;
    private long bitCount;

    public GuavaLockFreeBitArray(long bits) {
        assert (bits > 0); // data length is zero!
        // Avoid delegating to this(long[]), since AtomicLongArray(long[]) will clone its input and
        // thus double memory usage.
        this.data =
                new AtomicLongArray((int) Math.ceil(bits/64.0));
        this.bitCount = 0;
    }

    // Used by serialization
    GuavaLockFreeBitArray(long[] data) {
        assert (data.length > 0); // data length is zero!
        this.data = new AtomicLongArray(data);
        this.bitCount = 0;
        long bitCount = 0;
        for (long value : data) {
            bitCount += Long.bitCount(value);
        }
        this.bitCount += bitCount;
    }

    /** Returns true if the bit changed value. */
    boolean set(long bitIndex) {
        if (get(bitIndex)) {
            return false;
        }

        int longIndex = (int) (bitIndex >>> LONG_ADDRESSABLE_BITS);
        long mask = 1L << bitIndex; // only cares about low 6 bits of bitIndex

        long oldValue;
        long newValue;
        do {
            oldValue = data.get(longIndex);
            newValue = oldValue | mask;
            if (oldValue == newValue) {
                return false;
            }
        } while (!data.compareAndSet(longIndex, oldValue, newValue));

        // We turned the bit on, so increment bitCount.
        bitCount += 1;
        return true;
    }

    boolean get(long i) {
        return (data.get((int) (i >>> LONG_ADDRESSABLE_BITS)) & (1L << i)) != 0;
    }


    /** Number of bits */
    long bitSize() {
        return (long) data.length() * Long.SIZE;
    }

    /**
     * Number of set bits (1s).
     *
     * <p>Note that because of concurrent set calls and uses of atomics, this bitCount is a (very)
     * close *estimate* of the actual number of bits set. It's not possible to do better than an
     * estimate without locking. Note that the number, if not exactly accurate, is *always*
     * underestimating, never overestimating.
     */
    long bitCount() {
        return bitCount;
    }


    /** Returns the number of {@code long}s in the underlying {@link AtomicLongArray}. */
    int dataLength() {
        return data.length();
    }

    @Override
    public void set(int i) {
        set(i);
    }

    @Override
    public boolean get(int i) {
        return get((long) i);
    }

    @Override
    public int size() {
        return dataLength() * 64;
    }
}