package com.leikoe.bitscontainers;

import com.leikoe.IBitsContainer;

import java.util.LinkedList;

public class BitLinkedList implements IBitsContainer {

    LinkedList<Boolean> bits;

    public BitLinkedList(int capacity) {
        bits = new LinkedList<>();

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
