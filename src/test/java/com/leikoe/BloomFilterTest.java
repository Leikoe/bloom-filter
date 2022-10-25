package com.leikoe;

import static org.junit.Assert.*;

public class BloomFilterTest {

    BloomFilter<Integer> arrayBloomFilter;
    BloomFilter<Integer> arrayListBloomFilter;
    BloomFilter<Integer> linkedListBloomFilter;

    @org.junit.Before
    public void setUp() throws Exception {
        arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(12000), new Integer[]{12, 87, 43, 22, 8, 97});
        arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(12000), new Integer[]{12, 87, 43, 22, 8, 97});
        linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(12000), new Integer[]{12, 87, 43, 22, 8, 97});
    }

    @org.junit.After
    public void tearDown() throws Exception {
    }

    @org.junit.Test
    public void add() {
        if (!arrayBloomFilter.mightContain(78)) {
            arrayBloomFilter.add(78);
            assertTrue(arrayBloomFilter.mightContain(78));
        }
        if (!arrayListBloomFilter.mightContain(78)) {
            arrayListBloomFilter.add(78);
            assertTrue(arrayListBloomFilter.mightContain(78));
        }
        if (!linkedListBloomFilter.mightContain(78)) {
            linkedListBloomFilter.add(78);
            assertTrue(linkedListBloomFilter.mightContain(78));
        }
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

    @org.junit.Test
    public void runBenchmarks() throws Exception {
        new Bencher().benchmark();
    }

}