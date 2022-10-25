package com.leikoe.hash;

import java.nio.ByteBuffer;
import java.util.Arrays;
import java.util.function.ToIntFunction;


public class MurmurHash2<T> implements ToIntFunction<T> {

    private final int seed;

    public MurmurHash2(int seed) {
        this.seed = seed;
    }

    public int hash(byte[] data) {
        int m = 0x5db1e995;
        int r = 24;

        int data_len = data.length;
        int h = seed ^ data_len;

        int i = 0;
        while (data_len >= 4) {
            // convert 4 bytes to an int
            int k = data[i]
                    + data[i+1] << 8
                    + data[i+2] << 16
                    + data[i+3] << 24;

            k *= m;
            k ^= k >> r;
            k *= m;

            h *= m;
            h ^= k;

            i += 4;
            data_len -= 4;
        }

        // Handle the last few bytes of the input array
        switch(data_len)
        {
            case 3: h ^= data[2] << 16;
            case 2: h ^= data[1] << 8;
            case 1: h ^= data[0];
                h *= m;
        };

        // Do a few final mixes of the hash to ensure the last few
        // bytes are well-incorporated.

        h ^= h >> 13;
        h *= m;
        h ^= h >> 15;

        return h;
    }

    @Override
    public int applyAsInt(T value) {
        byte[] data = Utils.objectToBytes(value);
        return hash(data);
    }
}
