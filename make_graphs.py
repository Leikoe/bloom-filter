from matplotlib import pyplot as plt
from math import log

data = """
Benchmark                                         (items)  Mode  Cnt         Score        Error  Units
Bencher.arrayBloomFilterAdd                             2  avgt    5         0.074 ±      0.017  us/op
Bencher.arrayBloomFilterAdd                             4  avgt    5         0.091 ±      0.018  us/op
Bencher.arrayBloomFilterAdd                             8  avgt    5         0.152 ±      0.005  us/op
Bencher.arrayBloomFilterAdd                            16  avgt    5         0.283 ±      0.020  us/op
Bencher.arrayBloomFilterAdd                            32  avgt    5         0.542 ±      0.034  us/op
Bencher.arrayBloomFilterAdd                            64  avgt    5         1.081 ±      0.064  us/op
Bencher.arrayBloomFilterAdd                           128  avgt    5         2.130 ±      0.024  us/op
Bencher.arrayBloomFilterAdd                           256  avgt    5         6.046 ±      0.223  us/op
Bencher.arrayBloomFilterAdd                           512  avgt    5        13.712 ±      0.847  us/op
Bencher.arrayBloomFilterAdd                          1024  avgt    5        27.315 ±      1.052  us/op
Bencher.arrayBloomFilterAdd                          2048  avgt    5        76.434 ±      3.371  us/op
Bencher.arrayBloomFilterAdd                          4096  avgt    5       153.682 ±      3.129  us/op
Bencher.arrayBloomFilterAdd                          8192  avgt    5       311.059 ±     27.822  us/op
Bencher.arrayBloomFilterContains                        2  avgt    5         0.025 ±      0.019  us/op
Bencher.arrayBloomFilterContains                        4  avgt    5         0.103 ±      0.017  us/op
Bencher.arrayBloomFilterContains                        8  avgt    5         0.161 ±      0.014  us/op
Bencher.arrayBloomFilterContains                       16  avgt    5         0.242 ±      0.024  us/op
Bencher.arrayBloomFilterContains                       32  avgt    5         0.423 ±      0.031  us/op
Bencher.arrayBloomFilterContains                       64  avgt    5         0.805 ±      0.015  us/op
Bencher.arrayBloomFilterContains                      128  avgt    5         1.609 ±      0.033  us/op
Bencher.arrayBloomFilterContains                      256  avgt    5         3.317 ±      0.093  us/op
Bencher.arrayBloomFilterContains                      512  avgt    5         7.724 ±      0.280  us/op
Bencher.arrayBloomFilterContains                     1024  avgt    5        12.613 ±      0.746  us/op
Bencher.arrayBloomFilterContains                     2048  avgt    5        26.240 ±      8.671  us/op
Bencher.arrayBloomFilterContains                     4096  avgt    5        53.258 ±      3.068  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5       113.712 ±      9.662  us/op
Bencher.arrayListBloomFilterAdd                         2  avgt    5         0.077 ±      0.031  us/op
Bencher.arrayListBloomFilterAdd                         4  avgt    5         0.091 ±      0.024  us/op
Bencher.arrayListBloomFilterAdd                         8  avgt    5         0.150 ±      0.004  us/op
Bencher.arrayListBloomFilterAdd                        16  avgt    5         0.281 ±      0.013  us/op
Bencher.arrayListBloomFilterAdd                        32  avgt    5         0.538 ±      0.037  us/op
Bencher.arrayListBloomFilterAdd                        64  avgt    5         1.070 ±      0.083  us/op
Bencher.arrayListBloomFilterAdd                       128  avgt    5         2.137 ±      0.034  us/op
Bencher.arrayListBloomFilterAdd                       256  avgt    5         6.036 ±      0.083  us/op
Bencher.arrayListBloomFilterAdd                       512  avgt    5        13.688 ±      0.286  us/op
Bencher.arrayListBloomFilterAdd                      1024  avgt    5        25.649 ±     12.201  us/op
Bencher.arrayListBloomFilterAdd                      2048  avgt    5        80.439 ±     22.145  us/op
Bencher.arrayListBloomFilterAdd                      4096  avgt    5       153.259 ±      3.010  us/op
Bencher.arrayListBloomFilterAdd                      8192  avgt    5       313.017 ±      8.372  us/op
Bencher.arrayListBloomFilterContains                    2  avgt    5         0.025 ±      0.023  us/op
Bencher.arrayListBloomFilterContains                    4  avgt    5         0.100 ±      0.066  us/op
Bencher.arrayListBloomFilterContains                    8  avgt    5         0.162 ±      0.019  us/op
Bencher.arrayListBloomFilterContains                   16  avgt    5         0.244 ±      0.016  us/op
Bencher.arrayListBloomFilterContains                   32  avgt    5         0.421 ±      0.012  us/op
Bencher.arrayListBloomFilterContains                   64  avgt    5         0.807 ±      0.025  us/op
Bencher.arrayListBloomFilterContains                  128  avgt    5         1.608 ±      0.025  us/op
Bencher.arrayListBloomFilterContains                  256  avgt    5         3.331 ±      0.054  us/op
Bencher.arrayListBloomFilterContains                  512  avgt    5         7.729 ±      0.152  us/op
Bencher.arrayListBloomFilterContains                 1024  avgt    5        12.603 ±      1.223  us/op
Bencher.arrayListBloomFilterContains                 2048  avgt    5        27.598 ±     13.937  us/op
Bencher.arrayListBloomFilterContains                 4096  avgt    5        53.978 ±      3.101  us/op
Bencher.arrayListBloomFilterContains                 8192  avgt    5       113.419 ±     10.481  us/op
Bencher.hashsetAdd                                      2  avgt    5         0.051 ±      0.006  us/op
Bencher.hashsetAdd                                      4  avgt    5         0.061 ±      0.007  us/op
Bencher.hashsetAdd                                      8  avgt    5         0.110 ±      0.032  us/op
Bencher.hashsetAdd                                     16  avgt    5         0.156 ±      0.071  us/op
Bencher.hashsetAdd                                     32  avgt    5         0.332 ±      0.097  us/op
Bencher.hashsetAdd                                     64  avgt    5         0.624 ±      0.201  us/op
Bencher.hashsetAdd                                    128  avgt    5         1.477 ±      0.267  us/op
Bencher.hashsetAdd                                    256  avgt    5         2.672 ±      1.350  us/op
Bencher.hashsetAdd                                    512  avgt    5         6.145 ±      3.244  us/op
Bencher.hashsetAdd                                   1024  avgt    5        15.473 ±      6.550  us/op
Bencher.hashsetAdd                                   2048  avgt    5        34.661 ±      9.200  us/op
Bencher.hashsetAdd                                   4096  avgt    5        70.670 ±     19.711  us/op
Bencher.hashsetAdd                                   8192  avgt    5       185.008 ±     34.495  us/op
Bencher.hashsetAddAll                                   2  avgt    5         0.054 ±      0.009  us/op
Bencher.hashsetAddAll                                   4  avgt    5         0.069 ±      0.029  us/op
Bencher.hashsetAddAll                                   8  avgt    5         0.141 ±      0.153  us/op
Bencher.hashsetAddAll                                  16  avgt    5         0.178 ±      0.076  us/op
Bencher.hashsetAddAll                                  32  avgt    5         0.326 ±      0.016  us/op
Bencher.hashsetAddAll                                  64  avgt    5         0.665 ±      0.128  us/op
Bencher.hashsetAddAll                                 128  avgt    5         1.407 ±      0.256  us/op
Bencher.hashsetAddAll                                 256  avgt    5         3.004 ±      0.376  us/op
Bencher.hashsetAddAll                                 512  avgt    5         6.224 ±      0.341  us/op
Bencher.hashsetAddAll                                1024  avgt    5        14.647 ±      3.693  us/op
Bencher.hashsetAddAll                                2048  avgt    5        33.185 ±      8.583  us/op
Bencher.hashsetAddAll                                4096  avgt    5        72.730 ±      8.585  us/op
Bencher.hashsetAddAll                                8192  avgt    5       173.539 ±     25.323  us/op
Bencher.hashsetContains                                 2  avgt    5         0.027 ±      0.016  us/op
Bencher.hashsetContains                                 4  avgt    5         0.061 ±      0.047  us/op
Bencher.hashsetContains                                 8  avgt    5         0.080 ±      0.096  us/op
Bencher.hashsetContains                                16  avgt    5         0.112 ±      0.083  us/op
Bencher.hashsetContains                                32  avgt    5         0.188 ±      0.023  us/op
Bencher.hashsetContains                                64  avgt    5         0.338 ±      0.041  us/op
Bencher.hashsetContains                               128  avgt    5         0.677 ±      0.027  us/op
Bencher.hashsetContains                               256  avgt    5         1.329 ±      0.062  us/op
Bencher.hashsetContains                               512  avgt    5         2.412 ±      0.113  us/op
Bencher.hashsetContains                              1024  avgt    5         4.431 ±      0.100  us/op
Bencher.hashsetContains                              2048  avgt    5         7.585 ±      0.080  us/op
Bencher.hashsetContains                              4096  avgt    5        15.151 ±      0.263  us/op
Bencher.hashsetContains                              8192  avgt    5        35.365 ±      2.470  us/op
Bencher.linkedListBloomFilterAdd                        2  avgt    5         0.554 ±      0.896  us/op
Bencher.linkedListBloomFilterAdd                        4  avgt    5         3.122 ±      2.804  us/op
Bencher.linkedListBloomFilterAdd                        8  avgt    5        13.922 ±      9.878  us/op
Bencher.linkedListBloomFilterAdd                       16  avgt    5        61.751 ±     27.615  us/op
Bencher.linkedListBloomFilterAdd                       32  avgt    5       246.146 ±    110.934  us/op
Bencher.linkedListBloomFilterAdd                       64  avgt    5      1037.335 ±    277.359  us/op
Bencher.linkedListBloomFilterAdd                      128  avgt    5      4059.615 ±    521.353  us/op
Bencher.linkedListBloomFilterAdd                      256  avgt    5     17046.640 ±   2089.719  us/op
Bencher.linkedListBloomFilterAdd                      512  avgt    5     67326.032 ±   7450.210  us/op
Bencher.linkedListBloomFilterAdd                     1024  avgt    5    265865.983 ±  18241.350  us/op
Bencher.linkedListBloomFilterAdd                     2048  avgt    5   1071327.609 ±  88316.840  us/op
Bencher.linkedListBloomFilterAdd                     4096  avgt    5   4593210.917 ± 173384.370  us/op
Bencher.linkedListBloomFilterAdd                     8192  avgt    5  18009778.925 ± 250210.705  us/op
Bencher.linkedListBloomFilterContains                   2  avgt    5         0.247 ±      0.469  us/op
Bencher.linkedListBloomFilterContains                   4  avgt    5         1.346 ±      1.731  us/op
Bencher.linkedListBloomFilterContains                   8  avgt    5         8.504 ±      4.340  us/op
Bencher.linkedListBloomFilterContains                  16  avgt    5        32.734 ±     15.273  us/op
Bencher.linkedListBloomFilterContains                  32  avgt    5       155.195 ±     85.063  us/op
Bencher.linkedListBloomFilterContains                  64  avgt    5       607.956 ±    228.650  us/op
Bencher.linkedListBloomFilterContains                 128  avgt    5      2409.540 ±    613.114  us/op
Bencher.linkedListBloomFilterContains                 256  avgt    5      9526.655 ±   1226.596  us/op
Bencher.linkedListBloomFilterContains                 512  avgt    5     38240.944 ±   4444.911  us/op
Bencher.linkedListBloomFilterContains                1024  avgt    5    153090.092 ±  16449.767  us/op
Bencher.linkedListBloomFilterContains                2048  avgt    5    615489.104 ±  41814.016  us/op
Bencher.linkedListBloomFilterContains                4096  avgt    5   2899868.966 ± 152024.374  us/op
Bencher.linkedListBloomFilterContains                8192  avgt    5  12323199.934 ± 433281.528  us/op
Bencher.nativeBitSetBloomFilterAdd                      2  avgt    5         0.106 ±      0.005  us/op
Bencher.nativeBitSetBloomFilterAdd                      4  avgt    5         0.191 ±      0.012  us/op
Bencher.nativeBitSetBloomFilterAdd                      8  avgt    5         0.336 ±      0.005  us/op
Bencher.nativeBitSetBloomFilterAdd                     16  avgt    5         0.610 ±      0.008  us/op
Bencher.nativeBitSetBloomFilterAdd                     32  avgt    5         1.147 ±      0.041  us/op
Bencher.nativeBitSetBloomFilterAdd                     64  avgt    5         2.157 ±      0.098  us/op
Bencher.nativeBitSetBloomFilterAdd                    128  avgt    5         4.084 ±      0.133  us/op
Bencher.nativeBitSetBloomFilterAdd                    256  avgt    5        10.337 ±      1.961  us/op
Bencher.nativeBitSetBloomFilterAdd                    512  avgt    5        15.577 ±      0.582  us/op
Bencher.nativeBitSetBloomFilterAdd                   1024  avgt    5        32.859 ±      9.672  us/op
Bencher.nativeBitSetBloomFilterAdd                   2048  avgt    5        87.973 ±      7.417  us/op
Bencher.nativeBitSetBloomFilterAdd                   4096  avgt    5       181.189 ±     14.588  us/op
Bencher.nativeBitSetBloomFilterAdd                   8192  avgt    5       370.182 ±     20.305  us/op
Bencher.nativeBitSetBloomFilterContains                 2  avgt    5         0.053 ±      0.007  us/op
Bencher.nativeBitSetBloomFilterContains                 4  avgt    5         0.105 ±      0.015  us/op
Bencher.nativeBitSetBloomFilterContains                 8  avgt    5         0.169 ±      0.005  us/op
Bencher.nativeBitSetBloomFilterContains                16  avgt    5         0.278 ±      0.026  us/op
Bencher.nativeBitSetBloomFilterContains                32  avgt    5         0.474 ±      0.046  us/op
Bencher.nativeBitSetBloomFilterContains                64  avgt    5         0.917 ±      0.018  us/op
Bencher.nativeBitSetBloomFilterContains               128  avgt    5         1.852 ±      0.046  us/op
Bencher.nativeBitSetBloomFilterContains               256  avgt    5         3.776 ±      0.116  us/op
Bencher.nativeBitSetBloomFilterContains               512  avgt    5         8.851 ±      0.322  us/op
Bencher.nativeBitSetBloomFilterContains              1024  avgt    5        15.306 ±      5.702  us/op
Bencher.nativeBitSetBloomFilterContains              2048  avgt    5        31.662 ±     15.482  us/op
Bencher.nativeBitSetBloomFilterContains              4096  avgt    5        61.340 ±      4.388  us/op
Bencher.nativeBitSetBloomFilterContains              8192  avgt    5       127.266 ±      6.484  us/op
ObjectToByteArrayBenchmark.serilizationDouble         N/A  avgt    5         0.458 ±      0.018  us/op
ObjectToByteArrayBenchmark.serilizationInteger        N/A  avgt    5         0.461 ±      0.026  us/op
ObjectToByteArrayBenchmark.serilizationString         N/A  avgt    5         0.326 ±      0.013  us/op
ObjectToByteArrayBenchmark.stringGetBytesDouble       N/A  avgt    5         0.107 ±      0.005  us/op
ObjectToByteArrayBenchmark.stringGetBytesInteger      N/A  avgt    5         0.034 ±      0.003  us/op
ObjectToByteArrayBenchmark.stringGetBytesString       N/A  avgt    5         0.065 ±      0.003  us/op
"""

# split data into lines and remove empty lines + remove header line
data = list(filter(lambda line: len(line) > 0, data.splitlines()))[1:]


def unique(xs: []) -> []:
    return list({*xs})


operations = ["Add", "Contains"]

# get lines by operation defined above
results = map(
    lambda op: filter(lambda line: op in line, data),
    operations
)

# get values for each line
results = map(
    lambda op_group: list(map(
        lambda line: line.split(),
        op_group
    )),
    results
)

results = map(
    lambda op_group: list(
        map(
            lambda l: (l[0], l[1], l[4]),
            op_group
        )
    ),
    results
)

def size_to_optimal_bit_array_size(n):
    return -n * log(0.01) / (log(2)**2)

results = list(results)
for op_group in results:
    # get the list of names
    names = unique(list(map(lambda x: x[0], op_group)))
    names.sort()
    for name in names:
        if "linked" in name:
            # continue
            pass

        # keep only name, size, time
        measurements = list(
            map(
                lambda x: (float(x[1]), float(x[2])),
                filter(lambda x: x[0] == name, op_group)
            )
        )
        # unzip measurements
        xs, ys = zip(*measurements)
        # xs, ys = xs[:-1], ys[:-1]
        #
        # change x to size of the bit array (bit => byte = lambda x: x/8)
        # xs = list(map(lambda x: size_to_optimal_bit_array_size(x)/8000, xs))

        print(name)
        print(measurements)

        plt.plot(xs, ys, label=name.split(".")[1])

    plt.yscale('linear')
    plt.ylabel("us/op")
    # plt.xlabel("BitArray size (KB)")
    plt.xlabel("items")
    plt.legend()
    plt.show()
    plt.clf()
