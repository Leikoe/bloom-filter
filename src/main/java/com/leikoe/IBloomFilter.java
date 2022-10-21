package com.leikoe;

public interface IBloomFilter<T> {
    void add(T value);
    boolean mightContain(T value);
}
