# Simple Bloom Filter implementation in java
## References:
- https://fr.wikipedia.org/wiki/Filtre_de_Bloom
- https://llimllib.github.io/bloomfilter-tutorial/
- https://fr.wikipedia.org/wiki/Fonction_de_hachage
- https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
- https://andybui01.github.io/bloom-filter/#implementation-and-benchmarks

### hash functions
- https://sites.google.com/site/murmurhash/
- https://gist.github.com/sgsfak/9ba382a0049f6ee885f68621ae86079b

### micro benchmarking
- https://stackoverflow.com/questions/51232809/performance-comparison-of-modulo-operator-and-bitwise-and
- https://stackoverflow.com/questions/504103/how-do-i-write-a-correct-micro-benchmark-in-java
- https://www.baeldung.com/java-microbenchmark-harness
- https://www.loicmathieu.fr/wordpress/informatique/introduction-a-jmh-java-microbenchmark-harness/
- http://leogomes.github.io/assets/JMH_cheatsheet.pdf

## how to run
Unit tests and Benchmarks
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

![before](./images/mightContain_v0_vs_hashsetContains)
![after](./images/mightContain_v1_vs_hashsetContains)

C style for loops tend to be faster than iterator based ones, 
this could explain the performance gain but i don't think it's the only factor here.

## Full Benchmark

```text
Benchmark                              (size)  Mode  Cnt        Score       Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5        0.059 ±     0.001  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5        0.531 ±     0.026  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5        3.186 ±     0.082  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5        5.628 ±     3.586  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5       48.326 ±     1.367  us/op
Bencher.arrayBloomFilterContains           10  avgt    5        0.069 ±     0.133  us/op
Bencher.arrayBloomFilterContains          100  avgt    5        0.487 ±     0.007  us/op
Bencher.arrayBloomFilterContains          500  avgt    5        2.426 ±     0.031  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5        4.850 ±     0.053  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5       49.767 ±     2.013  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5        0.064 ±     0.040  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5        0.523 ±     0.018  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5        3.178 ±     0.045  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5        5.202 ±     0.114  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5       46.924 ±     4.408  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5        0.065 ±     0.097  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5        0.528 ±     0.350  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5        2.431 ±     0.016  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5        4.895 ±     0.272  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5       49.972 ±     0.386  us/op
Bencher.hashsetAdd                         10  avgt    5        0.093 ±     0.005  us/op
Bencher.hashsetAdd                        100  avgt    5        1.096 ±     0.453  us/op
Bencher.hashsetAdd                        500  avgt    5        6.265 ±     5.971  us/op
Bencher.hashsetAdd                       1000  avgt    5       13.051 ±    12.923  us/op
Bencher.hashsetAdd                      10000  avgt    5      115.468 ±     5.873  us/op
Bencher.hashsetAddAll                      10  avgt    5        0.106 ±     0.013  us/op
Bencher.hashsetAddAll                     100  avgt    5        1.140 ±     0.197  us/op
Bencher.hashsetAddAll                     500  avgt    5        6.088 ±     0.447  us/op
Bencher.hashsetAddAll                    1000  avgt    5       14.888 ±     6.984  us/op
Bencher.hashsetAddAll                   10000  avgt    5      140.742 ±    11.030  us/op
Bencher.hashsetContains                    10  avgt    5        0.095 ±     0.129  us/op
Bencher.hashsetContains                   100  avgt    5        0.275 ±     0.004  us/op
Bencher.hashsetContains                   500  avgt    5        1.309 ±     0.075  us/op
Bencher.hashsetContains                  1000  avgt    5        2.589 ±     0.046  us/op
Bencher.hashsetContains                 10000  avgt    5       31.350 ±     3.677  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5        3.381 ±     6.376  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      377.952 ±    34.843  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     9289.068 ±   969.204  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    37596.084 ±  1629.044  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  3866428.283 ± 39552.540  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5        3.255 ±     3.420  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      368.887 ±   159.707  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     9179.882 ±  1220.485  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    36275.222 ±  2642.397  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  4833588.692 ± 99254.762  us/op
```