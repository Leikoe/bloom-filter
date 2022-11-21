package com.leikoe;

import static com.leikoe.hash.Utils.positiveMod;
import jdk.incubator.vector.*;

/**
 * WARNING: REQUIRES JAVA 18+
 */

public class VectorizedBloomFilter<T> extends BloomFilter<T> {

    VectorSpecies<Integer> SPECIES = IntVector.SPECIES_PREFERRED;

    // species bound
    int upperBound;

    int[] result;

    /**
     * This creates a BloomFilter instance using the provided bits container
     *
     * @param bitsContainer user provided bits container, all initialized to 0, must implement IBitsContainer
     * @param capacity
     */
    public VectorizedBloomFilter(IBitsContainer bitsContainer, int capacity) {
        super(bitsContainer, capacity);
        result = new int[k];

        // init array with k values except for the 2 first elements
        for (int i=0; i<k; i++) {
            result[i] = i;
        }

        upperBound = SPECIES.loopBound(k);
    }


    public static IntVector modulus(IntVector x, IntVector m) {
        IntVector v_q = x.div(m);
        return x.sub(m.mul(v_q));
    }

//    @Override
//    public void add(T value) {
//        result[0] = value.hashCode();
//        result[1] = (result[1] = result[0]) ^ (result[0] >> 16);
//
//        IntVector v_res0 = IntVector.broadcast(SPECIES, result[0]);
//        IntVector v_res1 = IntVector.broadcast(SPECIES, result[1]);
//
//        // init array with k values except for the 2 first elements
//        for (int i=2; i<k; i++) {
//            result[i] = i;
//        }
//
//        int i = 2;
//        int upperBound = SPECIES.loopBound(k-2);
//
//        for (; i < upperBound; i += SPECIES.length()) {
//            IntVector chunk = IntVector.fromArray(SPECIES, result, i);
//            IntVector res = chunk.mul(v_res1).add(v_res0).lanewise(VectorOperators.ASHR, 32 - 20);
//            res.intoArray(result, i);
//
//            for (int j = 0; j<SPECIES.length(); j++) {
//                int pos = result[i + j];
//                bits.set(positiveMod(pos, bits.size()), true);
//            }
//        }
//
//        // process the rest
//        for (; i<k; i++) {
//            int pos = (i*result[0]+result[1]) >> (32 - 1);
//            bits.set(positiveMod(pos, bits.size()), true);
//        }
//        this.n++;
//    }

    /**
     * PM+32 implementation of the alg described (SECTION 7) in daniel's lemire <a href="https://arxiv.org/pdf/1609.09840.pdf">paper "Regular and almost universal hashing: an efficient implementation"</a>
     *
     * @param value
     */
    @Override
    public void add(T value) {
        int base = value.hashCode();
        IntVector v_base = IntVector.broadcast(SPECIES, base);

        int i = 0;
        for (; i < upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, result, i);
            z = z.lanewise(VectorOperators.XOR, z.lanewise(VectorOperators.ASHR, 13));
            z = z.mul(0xab3be54f).mul(v_base);
            z = z.lanewise(VectorOperators.XOR, z.lanewise(VectorOperators.ASHR, 16));

            for (int j = 0; j<SPECIES.length(); j++) {
                int pos = z.lane(j);
                bits.set(positiveMod(pos, bits.size()), true);
            }
        }

        // process the rest
        for (; i<k; i++) {
            int z = base ^ (base >> 13);
            z = z * 0xab3be54f * i;
            z = z ^ (z >> 16);

            bits.set(positiveMod(z, bits.size()), true);
        }
        this.n++;
    }

    @Override
    public boolean mightContain(T value) {
        int base = value.hashCode();
        IntVector v_base = IntVector.broadcast(SPECIES, base);

        boolean all_true = true;

        int i = 0;
        for (; all_true && i < upperBound; i += SPECIES.length()) {
            IntVector z = IntVector.fromArray(SPECIES, result, i);
            z = z.lanewise(VectorOperators.XOR, z.lanewise(VectorOperators.ASHR, 13));
            z = z.mul(0xab3be54f).mul(v_base);
            z = z.lanewise(VectorOperators.XOR, z.lanewise(VectorOperators.ASHR, 16));

            for (int j = 0; all_true && j<SPECIES.length(); j++) {
                int pos = z.lane(j);
                all_true = bits.get(positiveMod(pos, bits.size()));
            }
        }

        // process the rest
        for (; all_true && i<this.k; i++) {
            int z = base ^ (base >> 13);
            z = z * 0xab3be54f * i;
            z = z ^ (z >> 16);

            all_true = bits.get(positiveMod(z, bits.size()));
        }

        return all_true;
    }
}
