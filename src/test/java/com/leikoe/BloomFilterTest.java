package com.leikoe;

import java.util.ArrayList;
import java.util.Random;

import static org.junit.Assert.*;

public class BloomFilterTest {

    BloomFilter<Integer> arrayBloomFilter;
    BloomFilter<Integer> arrayListBloomFilter;
    BloomFilter<Integer> linkedListBloomFilter;

    @org.junit.Before
    public void setUp() throws Exception {
        arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(BloomFilter.getOptimalSize(12000));
        TestUtils.fillBloomFilter(arrayBloomFilter, new Integer[]{12, 87, 43, 22, 8, 97});
        arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(BloomFilter.getOptimalSize(12000));
        TestUtils.fillBloomFilter(arrayListBloomFilter, new Integer[]{12, 87, 43, 22, 8, 97});
        linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(BloomFilter.getOptimalSize(12000));
        TestUtils.fillBloomFilter(linkedListBloomFilter, new Integer[]{12, 87, 43, 22, 8, 97});
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
    public void testError() {
        Random random = new Random();
        final int NUMBER_OF_TEST_ITEMS = 100_000;
        final int ITEM_MAX_VALUE = 1_000_000;
        BloomFilter<Integer> bloomFilter = TestUtils.makeExampleArrayListBloomFilter(NUMBER_OF_TEST_ITEMS);
        System.out.println("BloomFilter's inner BitsContainer has size m=" + bloomFilter.bits.size()
                + ", using n=" + NUMBER_OF_TEST_ITEMS + ", and e=" + BloomFilter.FALSE_POSITIVE_RATE);
        ArrayList<Integer> testNumbers = new ArrayList<>();
        for (int i=0; i<NUMBER_OF_TEST_ITEMS; i++) {
            Integer rndInt = random.nextInt(ITEM_MAX_VALUE);
            testNumbers.add(rndInt);
            bloomFilter.add(rndInt);
        }

        int false_postives = 0;
        int true_negatives = 0;
        for (Integer i=0; i<ITEM_MAX_VALUE; i++) {
            if (bloomFilter.mightContain(i)) {
                if (!testNumbers.contains(i)) {
                    false_postives++;
                }
            } else {
                true_negatives++;
            }
        }

        double observeredFalsePositiveRate = false_postives/(double) (false_postives + true_negatives);
        System.out.println("Observed a false positive rate of " + observeredFalsePositiveRate + ", expected was " + BloomFilter.FALSE_POSITIVE_RATE);
        assertTrue(observeredFalsePositiveRate < BloomFilter.FALSE_POSITIVE_RATE);
    }

}