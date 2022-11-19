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

java -jar target/benchmarks.jar # for all benchmarks
# or
java -jar target/benchmarks.jar com.leikoe.Bencher # for only bloom filter benchmarks
java -jar target/benchmarks.jar com.leikoe.ObjectToByte # for only ObjectToBytes benchmarks
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

![add](./images/add_v3.png)
![contains](./images/contains_v3.png)

**and without linked list**

![add - no linked list](./images/add_v3_-_no_linked_list.png)
![contains - no linked list](./images/contains_v3_-_no_linked_list.png)

When we look at the charts without the linked list, we can clearly see lines, which indicate a complexity of O(n), but when we add the linked list to the chart, it's a curve ! This indicates O(n^2), and the other lines look flat compared to it, even tho they are O(n).
What's weird is, we know from textbooks that linked list random access is O(n), and array/array list random access is O(1), why are we getting O(n^2) and O(n) ?
The answer is simple, since for each benchmark, we insert n elements, the compexity is multiplied by n. This gives results which explain perfectly the curves we are seeing on the charts.

```text
Benchmark                                         (items)  Mode  Cnt         Score        Error  Units
Bencher.arrayBloomFilterAdd                             2  avgt    5         0.042 ±      0.031  us/op
Bencher.arrayBloomFilterAdd                             4  avgt    5         0.073 ±      0.029  us/op
Bencher.arrayBloomFilterAdd                             8  avgt    5         0.133 ±      0.030  us/op
Bencher.arrayBloomFilterAdd                            16  avgt    5         0.252 ±      0.030  us/op
Bencher.arrayBloomFilterAdd                            32  avgt    5         0.497 ±      0.077  us/op
Bencher.arrayBloomFilterAdd                            64  avgt    5         1.026 ±      0.024  us/op
Bencher.arrayBloomFilterAdd                           128  avgt    5         2.901 ±      0.929  us/op
Bencher.arrayBloomFilterAdd                           256  avgt    5         6.035 ±      4.094  us/op
Bencher.arrayBloomFilterAdd                           512  avgt    5        20.823 ±      1.084  us/op
Bencher.arrayBloomFilterAdd                          1024  avgt    5        40.173 ±     11.665  us/op
Bencher.arrayBloomFilterAdd                          2048  avgt    5        77.072 ±     23.324  us/op
Bencher.arrayBloomFilterAdd                          4096  avgt    5       150.534 ±     14.550  us/op
Bencher.arrayBloomFilterAdd                          8192  avgt    5       308.701 ±     35.437  us/op
Bencher.arrayBloomFilterContains                        2  avgt    5         0.034 ±      0.049  us/op
Bencher.arrayBloomFilterContains                        4  avgt    5         0.056 ±      0.008  us/op
Bencher.arrayBloomFilterContains                        8  avgt    5         0.089 ±      0.026  us/op
Bencher.arrayBloomFilterContains                       16  avgt    5         0.214 ±      0.159  us/op
Bencher.arrayBloomFilterContains                       32  avgt    5         0.358 ±      0.210  us/op
Bencher.arrayBloomFilterContains                       64  avgt    5         0.709 ±      0.232  us/op
Bencher.arrayBloomFilterContains                      128  avgt    5         1.382 ±      0.462  us/op
Bencher.arrayBloomFilterContains                      256  avgt    5         3.052 ±      2.149  us/op
Bencher.arrayBloomFilterContains                      512  avgt    5         7.525 ±      0.272  us/op
Bencher.arrayBloomFilterContains                     1024  avgt    5        11.849 ±      9.105  us/op
Bencher.arrayBloomFilterContains                     2048  avgt    5        22.840 ±     15.854  us/op
Bencher.arrayBloomFilterContains                     4096  avgt    5        46.761 ±     34.471  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5        93.384 ±     60.560  us/op
Bencher.arrayListBloomFilterAdd                         2  avgt    5         0.047 ±      0.031  us/op
Bencher.arrayListBloomFilterAdd                         4  avgt    5         0.076 ±      0.035  us/op
Bencher.arrayListBloomFilterAdd                         8  avgt    5         0.128 ±      0.002  us/op
Bencher.arrayListBloomFilterAdd                        16  avgt    5         0.253 ±      0.039  us/op
Bencher.arrayListBloomFilterAdd                        32  avgt    5         0.511 ±      0.067  us/op
Bencher.arrayListBloomFilterAdd                        64  avgt    5         0.985 ±      0.147  us/op
Bencher.arrayListBloomFilterAdd                       128  avgt    5         3.127 ±      1.166  us/op
Bencher.arrayListBloomFilterAdd                       256  avgt    5         6.025 ±      4.043  us/op
Bencher.arrayListBloomFilterAdd                       512  avgt    5        20.642 ±      0.866  us/op
Bencher.arrayListBloomFilterAdd                      1024  avgt    5        40.359 ±     10.460  us/op
Bencher.arrayListBloomFilterAdd                      2048  avgt    5        79.448 ±     24.490  us/op
Bencher.arrayListBloomFilterAdd                      4096  avgt    5       150.421 ±     16.676  us/op
Bencher.arrayListBloomFilterAdd                      8192  avgt    5       300.077 ±     25.161  us/op
Bencher.arrayListBloomFilterContains                    2  avgt    5         0.033 ±      0.020  us/op
Bencher.arrayListBloomFilterContains                    4  avgt    5         0.059 ±      0.066  us/op
Bencher.arrayListBloomFilterContains                    8  avgt    5         0.108 ±      0.100  us/op
Bencher.arrayListBloomFilterContains                   16  avgt    5         0.204 ±      0.082  us/op
Bencher.arrayListBloomFilterContains                   32  avgt    5         0.385 ±      0.148  us/op
Bencher.arrayListBloomFilterContains                   64  avgt    5         0.708 ±      0.239  us/op
Bencher.arrayListBloomFilterContains                  128  avgt    5         1.347 ±      0.496  us/op
Bencher.arrayListBloomFilterContains                  256  avgt    5         2.949 ±      0.064  us/op
Bencher.arrayListBloomFilterContains                  512  avgt    5         7.637 ±      0.467  us/op
Bencher.arrayListBloomFilterContains                 1024  avgt    5        12.190 ±     11.544  us/op
Bencher.arrayListBloomFilterContains                 2048  avgt    5        24.180 ±     16.853  us/op
Bencher.arrayListBloomFilterContains                 4096  avgt    5        42.644 ±      0.376  us/op
Bencher.arrayListBloomFilterContains                 8192  avgt    5       109.703 ±     81.989  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             2  avgt    5         0.109 ±      0.054  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             4  avgt    5         0.187 ±      0.049  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             8  avgt    5         0.380 ±      0.127  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            16  avgt    5         0.707 ±      0.169  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            32  avgt    5         1.365 ±      0.320  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            64  avgt    5         2.727 ±      0.503  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           128  avgt    5         5.854 ±      1.344  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           256  avgt    5        15.088 ±      3.261  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           512  avgt    5        27.756 ±     19.073  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          1024  avgt    5        60.705 ±     11.612  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          2048  avgt    5       126.116 ±     20.590  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          4096  avgt    5       242.119 ±     18.737  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          8192  avgt    5       491.225 ±     10.123  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        2  avgt    5         0.050 ±      0.040  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        4  avgt    5         0.074 ±      0.069  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        8  avgt    5         0.152 ±      0.098  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       16  avgt    5         0.324 ±      0.165  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       32  avgt    5         0.522 ±      0.303  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       64  avgt    5         0.918 ±      0.286  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      128  avgt    5         1.937 ±      0.643  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      256  avgt    5         3.674 ±      1.156  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      512  avgt    5         8.752 ±      0.236  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     1024  avgt    5        15.296 ±      0.288  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     2048  avgt    5        31.621 ±     14.118  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     4096  avgt    5        64.639 ±     15.699  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     8192  avgt    5       120.239 ±     39.299  us/op
Bencher.hashsetAdd                                      2  avgt    5         0.065 ±      0.011  us/op
Bencher.hashsetAdd                                      4  avgt    5         0.074 ±      0.028  us/op
Bencher.hashsetAdd                                      8  avgt    5         0.113 ±      0.069  us/op
Bencher.hashsetAdd                                     16  avgt    5         0.157 ±      0.071  us/op
Bencher.hashsetAdd                                     32  avgt    5         0.310 ±      0.068  us/op
Bencher.hashsetAdd                                     64  avgt    5         0.617 ±      0.039  us/op
Bencher.hashsetAdd                                    128  avgt    5         1.238 ±      0.071  us/op
Bencher.hashsetAdd                                    256  avgt    5         2.636 ±      0.200  us/op
Bencher.hashsetAdd                                    512  avgt    5         6.558 ±      4.294  us/op
Bencher.hashsetAdd                                   1024  avgt    5        14.768 ±      4.120  us/op
Bencher.hashsetAdd                                   2048  avgt    5        34.690 ±      8.734  us/op
Bencher.hashsetAdd                                   4096  avgt    5        76.511 ±     14.395  us/op
Bencher.hashsetAdd                                   8192  avgt    5       179.248 ±     12.460  us/op
Bencher.hashsetAddAll                                   2  avgt    5         0.066 ±      0.034  us/op
Bencher.hashsetAddAll                                   4  avgt    5         0.080 ±      0.043  us/op
Bencher.hashsetAddAll                                   8  avgt    5         0.125 ±      0.056  us/op
Bencher.hashsetAddAll                                  16  avgt    5         0.204 ±      0.077  us/op
Bencher.hashsetAddAll                                  32  avgt    5         0.382 ±      0.087  us/op
Bencher.hashsetAddAll                                  64  avgt    5         0.714 ±      0.079  us/op
Bencher.hashsetAddAll                                 128  avgt    5         1.498 ±      0.048  us/op
Bencher.hashsetAddAll                                 256  avgt    5         3.304 ±      0.227  us/op
Bencher.hashsetAddAll                                 512  avgt    5         6.690 ±      2.423  us/op
Bencher.hashsetAddAll                                1024  avgt    5        14.381 ±      4.277  us/op
Bencher.hashsetAddAll                                2048  avgt    5        35.143 ±      7.481  us/op
Bencher.hashsetAddAll                                4096  avgt    5        75.939 ±     12.995  us/op
Bencher.hashsetAddAll                                8192  avgt    5       178.601 ±     21.865  us/op
Bencher.hashsetContains                                 2  avgt    5         0.030 ±      0.004  us/op
Bencher.hashsetContains                                 4  avgt    5         0.063 ±      0.118  us/op
Bencher.hashsetContains                                 8  avgt    5         0.119 ±      0.173  us/op
Bencher.hashsetContains                                16  avgt    5         0.108 ±      0.234  us/op
Bencher.hashsetContains                                32  avgt    5         0.182 ±      0.011  us/op
Bencher.hashsetContains                                64  avgt    5         0.273 ±      0.366  us/op
Bencher.hashsetContains                               128  avgt    5         0.525 ±      0.756  us/op
Bencher.hashsetContains                               256  avgt    5         1.049 ±      1.527  us/op
Bencher.hashsetContains                               512  avgt    5         1.953 ±      2.473  us/op
Bencher.hashsetContains                              1024  avgt    5         3.703 ±      4.105  us/op
Bencher.hashsetContains                              2048  avgt    5         6.611 ±      5.133  us/op
Bencher.hashsetContains                              4096  avgt    5        12.152 ±      9.159  us/op
Bencher.hashsetContains                              8192  avgt    5        29.461 ±     19.535  us/op
Bencher.linkedListBloomFilterAdd                        2  avgt    5         0.710 ±      1.076  us/op
Bencher.linkedListBloomFilterAdd                        4  avgt    5         3.336 ±      4.324  us/op
Bencher.linkedListBloomFilterAdd                        8  avgt    5        14.682 ±     24.122  us/op
Bencher.linkedListBloomFilterAdd                       16  avgt    5        60.217 ±     28.744  us/op
Bencher.linkedListBloomFilterAdd                       32  avgt    5       233.229 ±    134.106  us/op
Bencher.linkedListBloomFilterAdd                       64  avgt    5      1021.766 ±    169.988  us/op
Bencher.linkedListBloomFilterAdd                      128  avgt    5      4334.186 ±    505.610  us/op
Bencher.linkedListBloomFilterAdd                      256  avgt    5     16864.718 ±   1441.404  us/op
Bencher.linkedListBloomFilterAdd                      512  avgt    5     66296.361 ±   6950.772  us/op
Bencher.linkedListBloomFilterAdd                     1024  avgt    5    265922.352 ±  17840.991  us/op
Bencher.linkedListBloomFilterAdd                     2048  avgt    5   1073404.917 ±  75829.317  us/op
Bencher.linkedListBloomFilterAdd                     4096  avgt    5   4542597.075 ± 130971.004  us/op
Bencher.linkedListBloomFilterAdd                     8192  avgt    5  17919423.700 ± 119308.363  us/op
Bencher.linkedListBloomFilterContains                   2  avgt    5         0.236 ±      0.369  us/op
Bencher.linkedListBloomFilterContains                   4  avgt    5         1.189 ±      3.471  us/op
Bencher.linkedListBloomFilterContains                   8  avgt    5         8.343 ±      6.775  us/op
Bencher.linkedListBloomFilterContains                  16  avgt    5        30.256 ±      6.728  us/op
Bencher.linkedListBloomFilterContains                  32  avgt    5       140.684 ±     66.374  us/op
Bencher.linkedListBloomFilterContains                  64  avgt    5       602.268 ±    190.832  us/op
Bencher.linkedListBloomFilterContains                 128  avgt    5      2520.847 ±    357.547  us/op
Bencher.linkedListBloomFilterContains                 256  avgt    5      9478.117 ±   1795.424  us/op
Bencher.linkedListBloomFilterContains                 512  avgt    5     38711.094 ±   5343.840  us/op
Bencher.linkedListBloomFilterContains                1024  avgt    5    151974.707 ±  24011.880  us/op
Bencher.linkedListBloomFilterContains                2048  avgt    5    613122.363 ±  51112.392  us/op
Bencher.linkedListBloomFilterContains                4096  avgt    5   2850469.350 ± 145125.691  us/op
Bencher.linkedListBloomFilterContains                8192  avgt    5  12128564.750 ± 318030.277  us/op
Bencher.nativeBitSetBloomFilterAdd                      2  avgt    5         0.090 ±      0.014  us/op
Bencher.nativeBitSetBloomFilterAdd                      4  avgt    5         0.168 ±      0.005  us/op
Bencher.nativeBitSetBloomFilterAdd                      8  avgt    5         0.312 ±      0.009  us/op
Bencher.nativeBitSetBloomFilterAdd                     16  avgt    5         0.596 ±      0.040  us/op
Bencher.nativeBitSetBloomFilterAdd                     32  avgt    5         1.148 ±      0.068  us/op
Bencher.nativeBitSetBloomFilterAdd                     64  avgt    5         2.177 ±      0.296  us/op
Bencher.nativeBitSetBloomFilterAdd                    128  avgt    5         4.190 ±      0.707  us/op
Bencher.nativeBitSetBloomFilterAdd                    256  avgt    5        10.322 ±      1.005  us/op
Bencher.nativeBitSetBloomFilterAdd                    512  avgt    5        14.969 ±      0.423  us/op
Bencher.nativeBitSetBloomFilterAdd                   1024  avgt    5        43.645 ±      1.907  us/op
Bencher.nativeBitSetBloomFilterAdd                   2048  avgt    5        87.761 ±     11.245  us/op
Bencher.nativeBitSetBloomFilterAdd                   4096  avgt    5       172.676 ±     23.896  us/op
Bencher.nativeBitSetBloomFilterAdd                   8192  avgt    5       335.592 ±     33.110  us/op
Bencher.nativeBitSetBloomFilterContains                 2  avgt    5         0.045 ±      0.023  us/op
Bencher.nativeBitSetBloomFilterContains                 4  avgt    5         0.060 ±      0.019  us/op
Bencher.nativeBitSetBloomFilterContains                 8  avgt    5         0.116 ±      0.044  us/op
Bencher.nativeBitSetBloomFilterContains                16  avgt    5         0.232 ±      0.051  us/op
Bencher.nativeBitSetBloomFilterContains                32  avgt    5         0.431 ±      0.115  us/op
Bencher.nativeBitSetBloomFilterContains                64  avgt    5         0.844 ±      0.170  us/op
Bencher.nativeBitSetBloomFilterContains               128  avgt    5         1.634 ±      0.445  us/op
Bencher.nativeBitSetBloomFilterContains               256  avgt    5         3.405 ±      0.912  us/op
Bencher.nativeBitSetBloomFilterContains               512  avgt    5         8.646 ±      0.509  us/op
Bencher.nativeBitSetBloomFilterContains              1024  avgt    5        16.545 ±      3.547  us/op
Bencher.nativeBitSetBloomFilterContains              2048  avgt    5        32.864 ±      5.696  us/op
Bencher.nativeBitSetBloomFilterContains              4096  avgt    5        65.856 ±     13.485  us/op
Bencher.nativeBitSetBloomFilterContains              8192  avgt    5       135.400 ±     18.100  us/op
```