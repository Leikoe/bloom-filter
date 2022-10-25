package com.leikoe;

import static org.junit.Assert.*;

public class BloomFilterTest {

    BloomFilter<Integer> arrayListBloomFilter;

    @org.junit.Before
    public void setUp() throws Exception {
        arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(12000, new Integer[]{12, 87, 43, 22, 8, 97});
    }

    @org.junit.After
    public void tearDown() throws Exception {
    }

    @org.junit.Test
    public void add() {
    }

    @org.junit.Test
    public void mightContainTest() {
        assertTrue(arrayListBloomFilter.mightContain(12));
        assertTrue(arrayListBloomFilter.mightContain(87));
        assertTrue(arrayListBloomFilter.mightContain(43));
        assertTrue(arrayListBloomFilter.mightContain(22));
        assertTrue(arrayListBloomFilter.mightContain(8));
        assertTrue(arrayListBloomFilter.mightContain(97));

        assertFalse(arrayListBloomFilter.mightContain(67));
        assertFalse(arrayListBloomFilter.mightContain(7));
        assertFalse(arrayListBloomFilter.mightContain(748));
        assertFalse(arrayListBloomFilter.mightContain(23));
        assertFalse(arrayListBloomFilter.mightContain(328));
    }

//    @org.junit.Test
    public void runBenchmarks() throws Exception {
        new Bencher().benchmark();
    }

}