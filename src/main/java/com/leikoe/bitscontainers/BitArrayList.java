package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

import java.util.ArrayList;

public class BitArrayList implements IBitsContainer {
    ArrayList<Boolean> bits;

    BitArrayList(int capacity) {
        bits = new ArrayList<>(capacity);

        for (int i=0; i<capacity; i++) {
            bits.add(false);
        }
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
