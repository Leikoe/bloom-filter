# Simple Bloom Filter implementation in java
## references
- https://fr.wikipedia.org/wiki/Filtre_de_Bloom
- https://llimllib.github.io/bloomfilter-tutorial/
- https://fr.wikipedia.org/wiki/Fonction_de_hachage
- https://www.baeldung.com/java-microbenchmark-harness
- https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
### hash functions references:
- https://sites.google.com/site/murmurhash/

## how to run
```bash
mvn clean compile exec:java
```

## hash functions implementation optimisations
### murmurHash2

**4 bytes** to **int** conversion optimisation
```java
// going from 
int k = ByteBuffer.wrap(Arrays.copyOfRange(data, i, i+4));
// to
int k = ByteBuffer.wrap(data, i, 4);
// i saw a x% speedup.
```
```txt
Benchmark                                     Mode  Cnt     Score     Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  3677.043 ±  30.270  ns/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  5169.316 ± 461.229  ns/op
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
```txt
Benchmark                                     Mode  Cnt     Score     Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  3828.091 ±   5.912  ns/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  5100.557 ± 528.067  ns/op
```

... only made it slower
