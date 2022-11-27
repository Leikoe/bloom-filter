package com.leikoe.bitscontainers;

import com.leikoe.IBitsBlocksContainer;

public class BlockBitSet implements IBitsBlocksContainer {
    final int[][] data;
    private final int BLOCK_SIZE;
    private final int BLOCK_BIT_SIZE;
    private final int WORD_SIZE = 32;

    public BlockBitSet(long size, int blockSize) {
        assert (size > 0); // data length is zero!
//        assert (size % blockSize == 0);
        this.BLOCK_SIZE = blockSize;
        this.BLOCK_BIT_SIZE = WORD_SIZE * this.BLOCK_SIZE;
        this.data = new int[(int) Math.ceil(size/((float) this.BLOCK_BIT_SIZE))][blockSize];
    }

    @Override
    public void set(int bitIndex, boolean v) {
        int blockIndex = bitIndex / BLOCK_BIT_SIZE;
        int intIndex = (bitIndex % BLOCK_BIT_SIZE) / WORD_SIZE;
        data[blockIndex][intIndex] |= (1 << bitIndex); // from java's BitSet
    }

    @Override
    public boolean get(int i) {
        int blockIndex = i / BLOCK_BIT_SIZE;
        int intIndex = (i % BLOCK_BIT_SIZE) / WORD_SIZE;

        int word = data[blockIndex][intIndex];
        return (word & (1 << i)) != 0;
    }


    /** Number of bits */
    long bitSize() {
        return (long) data.length * Long.SIZE;
    }

    @Override
    public int size() {
        return data.length * BLOCK_SIZE * WORD_SIZE;
    }

    @Override
    public int[] getBlock(int i) {
        return data[i / BLOCK_BIT_SIZE];
    }

    @Override
    public void setBlock(int i, int[] block) {
        data[i] = block;
    }

    /** Returns the number of {@code long}s in the underlying long[]. */
    @Override
    public int blockCount() {
        return data.length;
    }

    @Override
    public int blockSize() {
        return BLOCK_SIZE;
    }
}
