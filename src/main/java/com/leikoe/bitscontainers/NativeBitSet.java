package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

import java.util.BitSet;

public class NativeBitSet implements IBitsContainer {
    BitSet bits;

    public NativeBitSet(int capacity) {
        bits = new BitSet(capacity);
    }

    @Override
    public void set(int i, boolean b) {
        bits.set(i, b);
    }

    @Override
    public boolean get(int i) {
        return bits.get(i);
    }

    @Override
    public int size() {
        return bits.size();
    }
}
