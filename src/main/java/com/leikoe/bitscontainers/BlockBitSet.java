package com.leikoe.bitscontainers;

import com.leikoe.IBitsBlocksContainer;

public class BlockBitSet implements IBitsBlocksContainer {
    final int[][] data;
    private long bitCount;
    private final int BLOCK_SIZE;
    private final int BLOCK_BIT_SIZE;
    private final int WORD_SIZE = 32;

    public BlockBitSet(long size, int blockSize) {
        assert (size > 0); // data length is zero!
        assert (size % blockSize == 0);
        this.BLOCK_SIZE = blockSize;
        this.BLOCK_BIT_SIZE = WORD_SIZE * this.BLOCK_SIZE;
        this.data = new int[(int) Math.ceil(size/((float) this.BLOCK_BIT_SIZE))][blockSize];
        this.bitCount = 0;
    }

    /** Returns true if the bit changed value. */
    boolean set(int bitIndex) {
        if (get(bitIndex)) {
            return false;
        }

        int blockIndex = bitIndex / BLOCK_BIT_SIZE;
        int intIndex = (bitIndex >>> 5) % BLOCK_BIT_SIZE;
        data[blockIndex][intIndex] |= (1 << bitIndex); // from java's BitSet

        // We turned the bit on, so increment bitCount.
        bitCount += 1;
        return true;
    }

    @Override
    public boolean get(int i) {
        int blockIndex = i / BLOCK_BIT_SIZE;
        int intIndex = (i >>> 5) % BLOCK_BIT_SIZE;

        System.out.println("BlockBitSet.length = " + data.length);
        System.out.println("blockIndex = " + blockIndex);
        System.out.println("intIndex = " + intIndex);

        int word = data[blockIndex][intIndex];
        return (word & (1 << i)) != 0;
    }


    /** Number of bits */
    long bitSize() {
        return (long) data.length * Long.SIZE;
    }

    /**
     * Number of set bits (1s).
     */
    long bitCount() {
        return bitCount;
    }


    /** Returns the number of {@code long}s in the underlying long[]. */
    int dataLength() {
        return data.length;
    }

    @Override
    public void set(int i, boolean b) {
        set(i);
    }

    @Override
    public int size() {
        return dataLength() * 64;
    }

    @Override
    public int[] getBlock(int i) {
        return data[i];
    }

    @Override
    public void setBlock(int i, int[] block) {
        data[i] = block;
    }
}
