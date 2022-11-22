package com.leikoe;

public interface IBitsBlocksContainer extends IBitsContainer {
    int[] getBlock(int i);
    void setBlock(int i, int[] block);
    int blockCount();
    int blockSize();
}
