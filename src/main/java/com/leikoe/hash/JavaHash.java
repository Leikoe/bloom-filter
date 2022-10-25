package com.leikoe.hash;

import java.util.function.ToIntFunction;


/* I ported
 * https://gist.github.com/sgsfak/9ba382a0049f6ee885f68621ae86079b
 * to java.
 */
public class JavaHash<T> implements ToIntFunction<T> {

    public int hash(byte[] data) {
        int h = 0;
        for (int i=0; i<data.length; i++) {
            h = 31 * h + data[i];
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
       byte[] data = Utils.objectToBytes(value);
       return hash(data);
    }
}
