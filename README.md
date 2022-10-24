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
// benchmarks
mvn clean compile exec:java

// unit tests
mvn test -Dtest=BloomFilterTest
```

## hash functions implementation optimisations
### murmurHash2

**4 bytes** to **int** conversion optimisation
```java
// going from 
int k = ByteBuffer.wrap(Arrays.copyOfRange(data, i, i+4)).getInt();
// to
int k = ByteBuffer.wrap(data, i, 4);
```
```txt
Benchmark                                     Mode  Cnt  Score   Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  3.527 ± 0.047  us/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  7.945 ± 0.196  us/op
```
to
```txt
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
```txt
Benchmark                                     Mode  Cnt  Score   Error  Units
Bencher.measureArrayListBloomFilterContains   avgt    5  2.977 ± 0.016  us/op
Bencher.measureLinkedListBloomFilterContains  avgt    5  6.403 ± 0.078  us/op
```

... only made it slower
