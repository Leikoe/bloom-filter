package com.leikoe.hash;

import java.util.function.ToIntFunction;

/* I ported
 * https://gist.github.com/sgsfak/9ba382a0049f6ee885f68621ae86079b
 * to java.
 */
public class Fnv32Hash<T> implements ToIntFunction<T> {
    int hash(byte[] data) {
        /* See the FNV parameters at www.isthe.com/chongo/tech/comp/fnv/#FNV-param */
        final int FNV_32_PRIME = 0x01000193; /* 16777619 */

        int h = 0x811c9dc5; /* 2166136261 */
        for (int i= 0; i<data.length; i++) {
            /* xor the bottom with the current octet */
            h ^= data[i];
            /* multiply by the 32 bit FNV magic prime mod 2^32 */
            h *= FNV_32_PRIME;
        }

        return h;
    }

    /**
     * Applies this function to the given argument.
     *
     * @param value the function argument
     * @return the function result
     */
    @Override
    public int applyAsInt(T value) {
        byte[] data = Utils.objectToStringToBytes(value);
        return hash(data);
    }
}
