package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

public class BitArray implements IBitsContainer {
    boolean[] bits;

    public BitArray(int capacity) {
        bits = new boolean[capacity];
    }

    @Override
    public void set(int i) {
        bits[i] = true;
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
