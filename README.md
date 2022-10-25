# Simple Bloom Filter implementation in java
## References:
- https://fr.wikipedia.org/wiki/Filtre_de_Bloom
- https://llimllib.github.io/bloomfilter-tutorial/
- https://fr.wikipedia.org/wiki/Fonction_de_hachage
- https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
### hash functions
- https://sites.google.com/site/murmurhash/
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
### murmurHash2

Loading **4 bytes** into **int** optimisation
```java
// going from 
int k = ByteBuffer.wrap(Arrays.copyOfRange(data, i, i+4)).getInt();
// to
int k = ByteBuffer.wrap(data, i, 4);
```
```text
Benchmark                                     Mode  Cnt  Score   Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  3.527 ± 0.047  us/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  7.945 ± 0.196  us/op
```
to
```text
Benchmark                                     Mode  Cnt  Score   Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  2.891 ± 0.009  us/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  7.359 ± 0.013  us/op
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
Benchmark                                     Mode  Cnt  Score   Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  2.977 ± 0.016  us/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  6.403 ± 0.078  us/op
```

... only made it slower

## Full Benchmark

```text
Benchmark                              (size)  Mode  Cnt    Score    Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5    3.318 ±  0.282  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5    3.354 ±  0.138  us/op
Bencher.arrayBloomFilterAdd            100000  avgt    5    3.356 ±  0.165  us/op
Bencher.arrayBloomFilterContains           10  avgt    5    3.387 ±  0.262  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5    3.417 ±  0.296  us/op
Bencher.arrayBloomFilterContains       100000  avgt    5    3.399 ±  0.376  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5    3.361 ±  0.130  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5    3.345 ±  0.185  us/op
Bencher.arrayListBloomFilterAdd        100000  avgt    5    3.328 ±  0.399  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5    3.388 ±  0.226  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5    3.412 ±  0.124  us/op
Bencher.arrayListBloomFilterContains   100000  avgt    5    3.399 ±  0.318  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5    3.390 ±  0.266  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5   10.526 ±  0.690  us/op
Bencher.linkedListBloomFilterAdd       100000  avgt    5  735.690 ± 19.659  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5    3.430 ±  0.259  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5   10.570 ±  0.654  us/op
Bencher.linkedListBloomFilterContains  100000  avgt    5  726.056 ± 61.732  us/op
```