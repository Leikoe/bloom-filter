package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

public class BitArray implements IBitsContainer {
    boolean[] bits;

    public BitArray(int capacity) {
        bits = new boolean[capacity];
    }

    @Override
    public void set(int i, boolean b) {
        bits[i] = b;
    }

    @Override
    public boolean get(int i) {
        return bits[i];
    }

    @Override
    public int size() {
        return bits.length;
    }
}
