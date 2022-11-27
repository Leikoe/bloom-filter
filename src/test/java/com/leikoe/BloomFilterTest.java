package com.leikoe;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;

import static org.junit.Assert.*;

public class BloomFilterTest {

    NaiveBloomFilter<Integer> arrayBloomFilter;
    NaiveBloomFilter<Integer> arrayListBloomFilter;
    NaiveBloomFilter<Integer> linkedListBloomFilter;

    BloomFilter<Integer> bloomFilter;
    UFBF<Integer> ufbf;

    Random rnd = new Random();

    @org.junit.Before
    public void setUp() throws Exception {
        Integer[] nums = new Integer[]{12, 87, 43, 22, 8, 97};

        arrayBloomFilter = TestUtils.makeExampleArrayBloomFilter(12000);
        TestUtils.fillBloomFilter(arrayBloomFilter, nums);
        arrayListBloomFilter = TestUtils.makeExampleArrayListBloomFilter(12000);
        TestUtils.fillBloomFilter(arrayListBloomFilter, nums);
        linkedListBloomFilter = TestUtils.makeExampleLinkedListBloomFilter(12000);
        TestUtils.fillBloomFilter(linkedListBloomFilter, nums);

        bloomFilter = TestUtils.makeExampleBloomFilter(12000);
        TestUtils.fillBloomFilter(bloomFilter, nums);
        ufbf = TestUtils.makeExampleUFBF(12000);
        TestUtils.fillBloomFilter(ufbf, nums);
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
        if (!bloomFilter.mightContain(78)) {
            bloomFilter.add(78);
            assertTrue(bloomFilter.mightContain(78));
        }
        if (!ufbf.mightContain(78)) {
            ufbf.add(78);
            assertTrue(ufbf.mightContain(78));
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
    public void testUFBF() {
        UFBF<Integer> ufbf = TestUtils.makeExampleUFBF(100);
        for (int i=0; i<100000; i++) {
            int x = rnd.nextInt();
            ufbf.add(x);
            assertTrue(ufbf.mightContain(x));
        }
    }

    @org.junit.Test
    public void testError() {
        int[] testCases = {
                250_000,
                500_000,
                750_000,
                1_000_000,
                1_250_000,
                1_500_000,
                1_750_000,
                2_000_000,
                2_250_000,
                2_500_000,
                2_750_000,
                3_000_000
        };

        System.out.println("n   false-positives   false-positive-rate");
        for (int n: testCases) {
            int falsePositives = getObservedFalsePositives(n);
            double observedFalsePositiveRate = falsePositives / (double) n;
//            System.out.format("%1$10d %1$10d %1$10d", n, falsePositives, observedFalsePositiveRate);
            System.out.println(n + "   " + falsePositives + "   " + observedFalsePositiveRate);
        }
    }

    public int getObservedFalsePositives(int n) {
        Random random = new Random();
        IBloomFilter<Integer> bloomFilter = TestUtils.makeExampleBloomFilter(n);

        HashSet<Integer> addedItems = new HashSet<>();
        for (int i=0; i<n; i++) {
            Integer rndInt = random.nextInt();
            addedItems.add(rndInt);
            bloomFilter.add(rndInt);
        }

        ArrayList<Integer> notAddedItems = new ArrayList<>();
        for (int i=0; i<n; i++) {
            int rndInt = random.nextInt();
            while (addedItems.contains(rndInt)) {
                rndInt = random.nextInt();
            }
            notAddedItems.add(rndInt);
        }

        int false_postives = 0;
        for (Integer i: notAddedItems) {
            if (bloomFilter.mightContain(i)) {
                false_postives++;
            }
        }

        return false_postives;
    }

}