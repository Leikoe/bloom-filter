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

### murmurHash2

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

## Full Benchmark

```text
Benchmark                              (size)  Mode  Cnt         Score         Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5        19.850 ±       1.321  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5       196.954 ±      13.039  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5       962.339 ±      17.903  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5      2094.526 ±     183.543  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5     26808.605 ±    7812.667  us/op
Bencher.arrayBloomFilterContains           10  avgt    5        19.131 ±       1.301  us/op
Bencher.arrayBloomFilterContains          100  avgt    5       193.008 ±      13.243  us/op
Bencher.arrayBloomFilterContains          500  avgt    5       937.986 ±      50.217  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5      2113.543 ±      66.201  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5     27498.714 ±    9934.526  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5        19.267 ±       1.023  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5       192.554 ±       8.570  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5       939.425 ±      29.086  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5      2060.662 ±     101.311  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5     26266.045 ±    3305.013  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5        19.154 ±       1.039  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5       192.491 ±       8.740  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5       947.019 ±      42.559  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5      2074.407 ±      39.236  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5     28712.362 ±   15544.948  us/op
Bencher.hashsetAdd                         10  avgt    5         0.095 ±       0.005  us/op
Bencher.hashsetAdd                        100  avgt    5         1.141 ±       0.655  us/op
Bencher.hashsetAdd                        500  avgt    5         4.678 ±       0.671  us/op
Bencher.hashsetAdd                       1000  avgt    5        16.444 ±       3.833  us/op
Bencher.hashsetAdd                      10000  avgt    5       137.495 ±       5.807  us/op
Bencher.hashsetAddAll                      10  avgt    5         0.105 ±       0.008  us/op
Bencher.hashsetAddAll                     100  avgt    5         1.153 ±       0.187  us/op
Bencher.hashsetAddAll                     500  avgt    5         6.245 ±       0.667  us/op
Bencher.hashsetAddAll                    1000  avgt    5        16.281 ±       5.724  us/op
Bencher.hashsetAddAll                   10000  avgt    5       168.502 ±      17.163  us/op
Bencher.hashsetContains                    10  avgt    5         0.092 ±       0.122  us/op
Bencher.hashsetContains                   100  avgt    5         0.276 ±       0.003  us/op
Bencher.hashsetContains                   500  avgt    5         1.325 ±       0.055  us/op
Bencher.hashsetContains                  1000  avgt    5         2.585 ±       0.091  us/op
Bencher.hashsetContains                 10000  avgt    5        30.826 ±       2.713  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5        30.745 ±       4.179  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      1552.945 ±     142.532  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     40493.725 ±     361.704  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    135596.099 ±    6157.114  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  15864174.583 ± 1992853.695  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5        32.971 ±       5.788  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      1606.076 ±     147.564  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     46505.354 ±    1619.691  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    152244.185 ±    3013.852  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  17953940.325 ± 3225326.896  us/op
```