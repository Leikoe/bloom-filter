# Simple Bloom Filter implementation in java
## References:
- https://fr.wikipedia.org/wiki/Filtre_de_Bloom
- https://llimllib.github.io/bloomfilter-tutorial/
- https://fr.wikipedia.org/wiki/Fonction_de_hachage
- https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
- https://andybui01.github.io/bloom-filter/#implementation-and-benchmarks // for formulas
- https://github.com/andybui01/Bloom/blob/main/include/bloom/bloom.h
- https://github.com/eugenp/tutorials/blob/master/guava-modules/guava-utilities/src/test/java/com/baeldung/guava/bloomfilter/BloomFilterUnitTest.java # usage of guava's bloom filter
- https://github.com/google/guava/blob/master/guava/src/com/google/common/hash/BloomFilterStrategies.java # guava's bloom filter's strategies

### hash functions
- https://sites.google.com/site/murmurhash/
- https://gist.github.com/sgsfak/9ba382a0049f6ee885f68621ae86079b

### micro benchmarking
- https://stackoverflow.com/questions/51232809/performance-comparison-of-modulo-operator-and-bitwise-and
- https://stackoverflow.com/questions/504103/how-do-i-write-a-correct-micro-benchmark-in-java
- https://www.baeldung.com/java-microbenchmark-harness
- https://www.loicmathieu.fr/wordpress/informatique/introduction-a-jmh-java-microbenchmark-harness/
- http://leogomes.github.io/assets/JMH_cheatsheet.pdf
- https://github.com/guozheng/jmh-tutorial // for the jar build

## how to run

run benchmarks
```bash
mvn clean install

java --add-modules jdk.incubator.vector -jar target/benchmarks.jar # for all benchmarks
# or
java --add-modules jdk.incubator.vector -jar target/benchmarks.jar com.leikoe.Bencher # for only bloom filter benchmarks
java --add-modules jdk.incubator.vector -jar target/benchmarks.jar com.leikoe.ObjectToByte # for only ObjectToBytes benchmarks
```

Unit tests
```bash
mvn test 
```

## Optimisations
> Benchmarks are all done with the same haashFunctions arrayList, but it might not be 
> the same as the one currently pushed on the repo. 

### From Object to byte[]
At first, I used a stack overflow answer to go from an Object to byte[], this is the code in Utils.objectToBytes().
```java
public static byte[] objectToBytes(Object object) {
    try (ByteArrayOutputStream bos = new ByteArrayOutputStream(); ObjectOutputStream oos = new ObjectOutputStream(bos)) {
        oos.writeObject(object);
        return bos.toByteArray();
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}
```
but, after doing the BloomFilter benchmarks, I found that I was much slower than java's HashSet, even when only using one hash function, 
the same one used in the HashSet, so it couldn't be my hash functions fault. After some more digging, this is the implementation most java BloomFilters use.
```java
public static byte[] objectToStringToBytes(Object object) {
    if(object == null) {
        return new byte[]{}; // null is represented by an empty byte array
    }

    // no need for .toString() when object is already a String
    if(object instanceof String) {
        return ((String) object).getBytes(StandardCharsets.UTF_8);
    }

    return object.toString().getBytes(StandardCharsets.UTF_8);
}
```
This proved to be much faster, about a 10x speedup.

```text
Benchmark                                         Mode  Cnt  Score   Error  Units
ObjectToByteArrayBenchmark.serilizationDouble     avgt    5  0.647 ± 0.019  us/op
ObjectToByteArrayBenchmark.serilizationInteger    avgt    5  0.640 ± 0.020  us/op
ObjectToByteArrayBenchmark.serilizationString     avgt    5  0.452 ± 0.015  us/op
ObjectToByteArrayBenchmark.stringGetBytesDouble   avgt    5  0.098 ± 0.005  us/op
ObjectToByteArrayBenchmark.stringGetBytesInteger  avgt    5  0.055 ± 0.005  us/op
ObjectToByteArrayBenchmark.stringGetBytesString   avgt    5  0.072 ± 0.006  us/op
```

### murmurHash2 Optimizations

Loading **4 bytes** into **int** optimisation
```java
// going from 
int k = ByteBuffer.wrap(Arrays.copyOfRange(data, i, i+4)).getInt();
// to
int k = ByteBuffer.wrap(data, i, 4);
```
```text
Benchmark                              (size)  Mode  Cnt     Score    Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5    13.307 ±  0.639  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5    13.473 ±  1.042  us/op
Bencher.arrayBloomFilterAdd            100000  avgt    5    14.225 ±  0.227  us/op
Bencher.arrayBloomFilterContains           10  avgt    5    13.281 ±  0.356  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5    12.992 ±  3.369  us/op
Bencher.arrayBloomFilterContains       100000  avgt    5    14.173 ±  0.418  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5    12.764 ±  3.911  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5    12.061 ±  4.064  us/op
Bencher.arrayListBloomFilterAdd        100000  avgt    5    14.098 ±  0.139  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5    12.617 ±  3.500  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5    13.379 ±  0.234  us/op
Bencher.arrayListBloomFilterContains   100000  avgt    5    14.264 ±  0.260  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5    13.033 ±  2.599  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    24.772 ±  0.117  us/op
Bencher.linkedListBloomFilterAdd       100000  avgt    5  1275.189 ± 35.425  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5    12.811 ±  5.370  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    22.341 ±  1.643  us/op
Bencher.linkedListBloomFilterContains  100000  avgt    5  1288.736 ± 64.979  us/op
```
to
```text
Benchmark                              (size)  Mode  Cnt     Score    Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5    11.430 ±  5.403  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5    11.303 ±  4.107  us/op
Bencher.arrayBloomFilterAdd            100000  avgt    5    12.632 ±  1.905  us/op
Bencher.arrayBloomFilterContains           10  avgt    5    11.860 ±  0.813  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5    11.161 ±  6.221  us/op
Bencher.arrayBloomFilterContains       100000  avgt    5    12.710 ±  0.513  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5    10.126 ±  4.166  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5    11.106 ±  3.977  us/op
Bencher.arrayListBloomFilterAdd        100000  avgt    5    12.666 ±  1.566  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5    10.920 ±  5.341  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5    10.982 ±  5.409  us/op
Bencher.arrayListBloomFilterContains   100000  avgt    5    12.501 ±  1.873  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5    10.365 ±  4.681  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    23.979 ±  0.258  us/op
Bencher.linkedListBloomFilterAdd       100000  avgt    5  1273.741 ± 29.381  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5    10.893 ±  5.591  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    24.021 ±  0.493  us/op
Bencher.linkedListBloomFilterContains  100000  avgt    5  1275.462 ± 59.471  us/op
```

Then, tried to improve further by removing the allocation of a new ByteBuffer
```java
// going from 
int k = ByteBuffer.wrap(data, i, 4);
// to
int k = data[i]
        + data[i+1] << 8
        + data[i+2] << 16
        + data[i+3] << 24;
```
```text
Benchmark                              (size)  Mode  Cnt    Score    Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5    9.258 ±  0.491  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5    9.137 ±  0.704  us/op
Bencher.arrayBloomFilterAdd            100000  avgt    5    9.272 ±  0.160  us/op
Bencher.arrayBloomFilterContains           10  avgt    5    9.222 ±  0.485  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5    9.229 ±  0.324  us/op
Bencher.arrayBloomFilterContains       100000  avgt    5    9.275 ±  0.332  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5    9.105 ±  0.525  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5    9.167 ±  0.350  us/op
Bencher.arrayListBloomFilterAdd        100000  avgt    5    9.297 ±  0.442  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5    9.198 ±  0.311  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5    9.224 ±  0.532  us/op
Bencher.arrayListBloomFilterContains   100000  avgt    5    9.256 ±  0.107  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5    9.286 ±  0.425  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5   17.757 ±  0.438  us/op
Bencher.linkedListBloomFilterAdd       100000  avgt    5  618.787 ± 39.022  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5    9.566 ±  0.896  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5   18.062 ±  0.483  us/op
Bencher.linkedListBloomFilterContains  100000  avgt    5  623.874 ± 30.746  us/op
```
we got a lot faster.

### BloomFilter optimizations
The mightContain() method's code was
```java
public boolean mightContain(T value) {
    boolean all_true = true;
    for (ToIntFunction<T> hashFunction: this.hashFunctions) {
        int pos = hashFunction.applyAsInt(value);
        boolean v = bits.get(positiveMod(pos, bits.size()));
        all_true = all_true && v;
    }

    return all_true;
}
```
changed to
```java
public boolean mightContain(T value) {
    boolean all_true = true;
    for (int i=0; all_true && i<this.hashFunctions.size(); i++) {
        ToIntFunction<T> hashFunction = this.hashFunctions.get(i);
        int pos = hashFunction.applyAsInt(value);
        all_true = bits.get(positiveMod(pos, bits.size()));
    }

    return all_true;
}
```
This provided a 20% performance boost across the board. (baseline is hashset contains from java's collections)

![before](./images/mightContain_v0_vs_hashsetContains.png)
![after](./images/mightContain_v1_vs_hashsetContains.png)

C style for loops tend to be faster than iterator based ones, 
this could explain the performance gain but i don't think it's the only factor here.

Then looking at some other implementations and reading papers (such as "Vectorized Bloom Filters for Advanced SIMD Processors"), I understood that we didn't need K hash functions, we just needed two base ones and then bishift + multiply would work for the next k-2 functions.
With this knowlegde, I produced the following code:
```java
public boolean mightContain(T value) {
        long[] hashes = new long[]{0, 0};

        boolean all_true = true;
        for (int i=0; all_true && i<this.k; i++) {
            long pos = hash(hashes, value, i);
            all_true = bits.get(positiveMod(pos, bits.size()));
        }

        return all_true;
}
```

Which i then optimized by removing the allocation:
```java
public boolean mightContain(T value) {
        hashes[0] = 0;
        hashes[1] = 0;

        boolean all_true = true;
        for (int i=0; all_true && i<this.k; i++) {
            long pos = hash(hashes, value, i);
            all_true = bits.get(positiveMod(pos, bits.size()));
        }

        return all_true;
}
```
and adding a long[] hashes in the class attributes, which gets allocated and initialized in the constructor.

Removing the allocation provided the following speedup:
```text
Bencher.arrayBloomFilterAdd                          8192  avgt    5       559.725 ±     21.785  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5       178.845 ±     27.856  us/op
```
to 
```text
Bencher.arrayBloomFilterAdd                          8192  avgt    5       308.701 ±     35.437  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5        93.384 ±     60.560  us/op
```
about a 2x speedup.

Then, removed the hashes long array reset in each call, because it was overriden by the first and second hash() calls before being used.

```text
Bencher.arrayBloomFilterAdd                          8192  avgt    5       308.701 ±     35.437  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5        93.384 ±     60.560  us/op
```
to
```text
Bencher.arrayBloomFilterAdd                          8192  avgt    5  297.222 ±  9.343  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5   88.677 ± 30.999  us/op
```

This provided little improvement across the board for all benchmarks.

inlining the two hashfunctions allowed for reusing result for the second one, (using hashCode() and hashMapHash()).
```text
Benchmark                         (items)  Mode  Cnt    Score    Error  Units
Bencher.arrayBloomFilterAdd          8192  avgt    5  142.792 ± 10.284  us/op
Bencher.arrayBloomFilterContains     8192  avgt    5   85.736 ± 17.159  us/op
```
to
```text
Benchmark                         (items)  Mode  Cnt    Score    Error  Units
Bencher.arrayBloomFilterAdd          8192  avgt    5  107.403 ± 12.855  us/op
Bencher.arrayBloomFilterContains     8192  avgt    5   73.524 ± 16.212  us/op
```
to provided a ~35% speedup for Add() and ~15% speedup for Contains().
> note: contains benefits less from this optimization as it does not run through all the hash functions when the element isn't present (%50 of the time in our bechmarks).

At this point, the bloomfilter is beating java's standard library's HashSet.

## UltraFastBloomFilter

- broadcast optimization (moved unit array creation to constructor instead of each call since its not modified)
- reducing compare operations, found out that they allocate. (using profiler)
- lt, compare and not all allocate, need to find a workaround
- the method I came up with to retain positive hash values allocates + is expensive

### fixing the positive hash values
```java
VectorMask<Integer> mask = v_combinedHash.lt(0);
v_combinedHash = v_combinedHash.blend(v_combinedHash.not(), mask);
```
this works and is the direct translation of the following in simd:
```java
// from google's guava hash implementation

// Flip all the bits if it's negative (guaranteed positive number)
if (combinedHash < 0) {
  combinedHash = ~combinedHash;
}
```
I noticed in the debugger that flipping all the bits like this gets the absolute value of the hash, which is a lot faster in smd than my implementation
> note: this might be architecture dependent
 
So I came up with this:
```java
v_combineHash = v_combineHash.abs();
```
This gave the following results when benchmarked (SimdBenchmark):

| mask + blend | 12.8 ns/op |
|--------------|------------|
| abs()        | 12.2 ns/op |

abs() runs just as fast and allocates less, while being clearer to read.

## UFBF, cache friendly

during my benchmarks, ufbf was doing worse than vectorizedBloomFilter, which wasn't supposed to happen.
after profiling, this part seemed to be the bottleneck
```java
 // process the rest in scalar code
for (; i<k; i++) {
    int pos = hash1 + ((i+1) * hash2);
    if (pos < 0) {
        pos = ~pos;
    }
//    block[i] |= 1 << pos;
    bits.set(pos % bits.size(), true);
}
```

bits.set was producing cache misses, I fixed it by reusing the block used by the vector loop above it
```java
// process the rest in scalar code
// block is a block of k ints
for (; i<k; i++) {
    int pos = hash1 + ((i+1) * hash2);
    if (pos < 0) {
        pos = ~pos;
    }
    block[i] |= 1 << pos;
}
```

this had a huge impact on performance

| ufbf.add() (cache miss)     | 2771.778 us/op  |
|-----------------------------|-----------------|
| ufbf.add() (cache friendly) | 943.710 us/op   |


## BitsContainer optimizations

according to https://stackoverflow.com/questions/605226/boolean-vs-bitset-which-is-more-efficient
> After some research, it appears that java's boolean type is more than a bit wide, java's solution is poviding us with a BitSet, which internally uses longs to store bits without wasting space.
> Taking advantage of this, I implemented NativeBitSet which implements IBitsContainer

## Tests optimizations

When using getObservedFalsePositives() in my tests, i noticed it was way slower than expected,
I initially thought it was my bloom filter being slow when checking if a given items belongs in it, but no.
It was the array list used to accumulate added values, found that out using the profiler, cpu was using 90% of it's time traversing the array list for the .contains calls.
Replaced it by an hashset and now its blazingly fast :speed: .

## Full Benchmarks
> note: all benchmarks were done on an m1 pro cpu (taking about an hour to complete), since they ran significantly slower on my i5 9600K and took 2+ hours to run.

![add](./images/add_v3.png)
![contains](./images/contains_v3.png)

**and without linked list**

![add - no linked list](./images/add_v5_-_no_linked_list.png)
![contains - no linked list](./images/contains_v5_-_no_linked_list.png)

When we look at the charts without the linked list, we can clearly see lines, which indicate a complexity of O(n), but when we add the linked list to the chart, it's a curve ! This indicates O(n^2), and the other lines look flat compared to it, even tho they are O(n).
What's weird is, we know from textbooks that linked list random access is O(n), and array/array list random access is O(1), why are we getting O(n^2) and O(n) ?
The answer is simple, since for each benchmark, we insert n elements, the compexity is multiplied by n. This gives results which explain perfectly the curves we are seeing on the charts.

```text
Benchmark                                         (items)  Mode  Cnt     Score     Error  Units
Bencher.arrayBloomFilterAdd                           100  avgt   25     1.413 ±   0.004  us/op
Bencher.arrayBloomFilterAdd                          1000  avgt   25    25.896 ±   0.074  us/op
Bencher.arrayBloomFilterAdd                         10000  avgt   25   330.483 ±   2.085  us/op
Bencher.arrayBloomFilterAdd                        100000  avgt   25  3496.858 ±   8.325  us/op
Bencher.arrayBloomFilterContains                      100  avgt   25     0.548 ±   0.021  us/op
Bencher.arrayBloomFilterContains                     1000  avgt   25     5.510 ±   0.076  us/op
Bencher.arrayBloomFilterContains                    10000  avgt   25    59.387 ±   3.361  us/op
Bencher.arrayBloomFilterContains                   100000  avgt   25   744.646 ± 138.558  us/op
Bencher.arrayListBloomFilterAdd                       100  avgt   25     1.395 ±   0.007  us/op
Bencher.arrayListBloomFilterAdd                      1000  avgt   25    25.729 ±   0.039  us/op
Bencher.arrayListBloomFilterAdd                     10000  avgt   25   331.732 ±   0.846  us/op
Bencher.arrayListBloomFilterAdd                    100000  avgt   25  3537.820 ±  22.890  us/op
Bencher.arrayListBloomFilterContains                  100  avgt   25     0.558 ±   0.020  us/op
Bencher.arrayListBloomFilterContains                 1000  avgt   25     5.557 ±   0.101  us/op
Bencher.arrayListBloomFilterContains                10000  avgt   25    61.056 ±   2.172  us/op
Bencher.arrayListBloomFilterContains               100000  avgt   25   747.699 ± 132.508  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           100  avgt   25     4.288 ±   0.048  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          1000  avgt   25    58.082 ±   1.147  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd         10000  avgt   25   564.690 ±   8.627  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd        100000  avgt   25  6045.567 ±  69.743  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      100  avgt   25     0.620 ±   0.024  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     1000  avgt   25     6.126 ±   0.125  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains    10000  avgt   25    63.429 ±   5.304  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains   100000  avgt   25   557.271 ±  25.598  us/op
Bencher.hashsetAdd                                    100  avgt   25     0.970 ±   0.063  us/op
Bencher.hashsetAdd                                   1000  avgt   25    10.426 ±   1.453  us/op
Bencher.hashsetAdd                                  10000  avgt   25   103.097 ±   3.038  us/op
Bencher.hashsetAdd                                 100000  avgt   25  4809.749 ± 283.105  us/op
Bencher.hashsetAddAll                                 100  avgt   25     1.098 ±   0.037  us/op
Bencher.hashsetAddAll                                1000  avgt   25    14.737 ±   0.920  us/op
Bencher.hashsetAddAll                               10000  avgt   25   124.986 ±   1.831  us/op
Bencher.hashsetAddAll                              100000  avgt   25  4824.546 ± 261.390  us/op
Bencher.hashsetContains                               100  avgt   25     0.452 ±   0.007  us/op
Bencher.hashsetContains                              1000  avgt   25     4.377 ±   0.063  us/op
Bencher.hashsetContains                             10000  avgt   25    49.130 ±   3.326  us/op
Bencher.hashsetContains                            100000  avgt   25   799.595 ±   5.226  us/op
Bencher.nativeBitSetBloomFilterAdd                    100  avgt   25     3.570 ±   0.092  us/op
Bencher.nativeBitSetBloomFilterAdd                   1000  avgt   25    39.065 ±   1.743  us/op
Bencher.nativeBitSetBloomFilterAdd                  10000  avgt   25   371.331 ±   1.151  us/op
Bencher.nativeBitSetBloomFilterAdd                 100000  avgt   25  3954.239 ±  34.139  us/op
Bencher.nativeBitSetBloomFilterContains               100  avgt   25     0.580 ±   0.024  us/op
Bencher.nativeBitSetBloomFilterContains              1000  avgt   25     5.844 ±   0.129  us/op
Bencher.nativeBitSetBloomFilterContains             10000  avgt   25    61.191 ±   3.425  us/op
Bencher.nativeBitSetBloomFilterContains            100000  avgt   25   544.132 ±  36.991  us/op
```