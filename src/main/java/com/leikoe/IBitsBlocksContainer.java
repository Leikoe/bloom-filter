package com.leikoe;

// TODO: javadoc
public interface IBitsBlocksContainer extends IBitsContainer {
    int[] getBlock(int i);
    void setBlock(int i, int[] block);
    int blockCount();
    int blockSize();
}
