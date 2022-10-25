package com.leikoe.hash;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;


public class Utils {
    public static byte[] objectToBytes(Object object) {
        try (ByteArrayOutputStream bos = new ByteArrayOutputStream(); ObjectOutputStream oos = new ObjectOutputStream(bos)) {
            oos.writeObject(object);
            return bos.toByteArray();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static int get4(byte[] bytes, int start) {
        return bytes[start]
                    + bytes[start+1] << 8
                    + bytes[start+2] << 16
                    + bytes[start+3] << 24;
    }

    public static int positiveMod(int x, int m) {
        return (x < 0) ? ((x % m) + m) % m : x % m;
    }
}
