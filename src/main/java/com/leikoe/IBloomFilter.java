package com.leikoe;

// TODO: javadoc
public interface IBloomFilter<T> {
    void add(T value);
    boolean mightContain(T value);
    int size();
}
