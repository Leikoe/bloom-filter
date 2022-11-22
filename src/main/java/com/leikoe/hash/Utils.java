package com.leikoe.hash;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.nio.charset.StandardCharsets;


public class Utils {
    public static byte[] objectToBytes(Object object) {
        try (ByteArrayOutputStream bos = new ByteArrayOutputStream(); ObjectOutputStream oos = new ObjectOutputStream(bos)) {
            oos.writeObject(object);
            return bos.toByteArray();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Gets the byte array representation from an object.
     * Credits to <a href="https://github.com/sangupta/bloomfilter/blob/5c7769f7ed19cc0eb2860cc0e1d4c0159830cd9e/src/main/java/com/sangupta/bloomfilter/decompose/DefaultDecomposer.java">https://github.com/sangupta/bloomfilter</a>
     *
     * @param object the object to get the bytes representation from
     * @return the byte representation
     */
    public static byte[] objectToStringToBytes(Object object) {
        if(object == null) {
            return new byte[]{}; // null is represented by an empty byte array
        }

        // no need for .toString() when object is already a String
        if(object instanceof String) {
            return ((String) object).getBytes(StandardCharsets.UTF_8);
        }

        return object.toString().getBytes(StandardCharsets.UTF_8);
    }

    public static int get4(byte[] bytes, int start) {
        int i = 0;
        i += bytes[start]
                    + bytes[start+1] << 8
                    + bytes[start+2] << 16
                    + bytes[start+3] << 24;
        return i;
    }

    public static int positiveMod(int x, int m) {
        int r = x % m;
        return (r < 0) ? r + m : r;
    }

    public static long positiveMod(long x, int m) {
        long r;
        return (r = x % m) < 0 ? r + m : r;
    }

    public static int nextPowerOf2(int x) {
        return x == 0 ? 2 : 2 << (32 - Integer.numberOfLeadingZeros(x - 1));
    }
}
