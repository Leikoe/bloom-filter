package com.leikoe;

// TODO: javadoc
public interface IBloomFilter<T> {
    /**
     * Insert a value in the filter
     *
     * @param value the value to add to the filter
     */
    void add(T value);

    /**
     * Membership check function
     *
     * @param value the value to check membership for
     * @return whether the value is in the filter or not
     */
    boolean mightContain(T value);

    /**
     * Get the size of the filter
     *
     * @return the number of elements in the filter
     */
    int size();
}
