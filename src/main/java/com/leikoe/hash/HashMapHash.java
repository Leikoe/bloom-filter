package com.leikoe.hash;

import java.util.function.ToIntFunction;

public class HashMapHash<T> implements ToIntFunction<T> {

    /**
     * This is from Java's HashMap implementation
     *
     * @param key the object to hash
     * @return the hashed object value
     */
    static int hash(Object key) {
        int h;
        return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }

    /**
     * Applies this function to the given argument.
     *
     * @param value the function argument
     * @return the function result
     */
    @Override
    public int applyAsInt(T value) {
        return hash(value);
    }
}
