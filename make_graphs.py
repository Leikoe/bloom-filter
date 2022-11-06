from matplotlib import pyplot as plt
from math import log

data = """
Benchmark                                         (items)  Mode  Cnt     Score     Error  Units
Bencher.arrayBloomFilterAdd                             2  avgt    5     0.234 ±   0.143  us/op
Bencher.arrayBloomFilterAdd                             4  avgt    5     0.318 ±   0.086  us/op
Bencher.arrayBloomFilterAdd                             8  avgt    5     0.654 ±   0.227  us/op
Bencher.arrayBloomFilterAdd                            16  avgt    5     1.284 ±   0.352  us/op
Bencher.arrayBloomFilterAdd                            32  avgt    5     2.855 ±   0.318  us/op
Bencher.arrayBloomFilterAdd                            64  avgt    5     7.542 ±   1.166  us/op
Bencher.arrayBloomFilterAdd                           128  avgt    5    16.582 ±   3.235  us/op
Bencher.arrayBloomFilterAdd                           256  avgt    5    41.473 ±   6.168  us/op
Bencher.arrayBloomFilterAdd                           512  avgt    5    78.769 ±  12.681  us/op
Bencher.arrayBloomFilterAdd                          1024  avgt    5   142.569 ±  47.705  us/op
Bencher.arrayBloomFilterAdd                          2048  avgt    5   289.627 ±  55.671  us/op
Bencher.arrayBloomFilterAdd                          4096  avgt    5   558.175 ±  42.149  us/op
Bencher.arrayBloomFilterAdd                          8192  avgt    5  1123.778 ±  57.433  us/op
Bencher.arrayBloomFilterAdd                         16384  avgt    5  2425.516 ± 883.337  us/op
Bencher.arrayBloomFilterContains                        2  avgt    5     0.160 ±   0.069  us/op
Bencher.arrayBloomFilterContains                        4  avgt    5     0.374 ±   0.255  us/op
Bencher.arrayBloomFilterContains                        8  avgt    5     0.656 ±   0.222  us/op
Bencher.arrayBloomFilterContains                       16  avgt    5     1.495 ±   0.445  us/op
Bencher.arrayBloomFilterContains                       32  avgt    5     2.901 ±   0.517  us/op
Bencher.arrayBloomFilterContains                       64  avgt    5     6.822 ±   1.375  us/op
Bencher.arrayBloomFilterContains                      128  avgt    5    15.198 ±   2.010  us/op
Bencher.arrayBloomFilterContains                      256  avgt    5    32.220 ±   3.506  us/op
Bencher.arrayBloomFilterContains                      512  avgt    5    68.806 ±   7.972  us/op
Bencher.arrayBloomFilterContains                     1024  avgt    5   127.805 ±  31.847  us/op
Bencher.arrayBloomFilterContains                     2048  avgt    5   268.484 ±  30.432  us/op
Bencher.arrayBloomFilterContains                     4096  avgt    5   503.217 ±  23.635  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5  1003.636 ±  19.360  us/op
Bencher.arrayBloomFilterContains                    16384  avgt    5  2129.930 ±  94.376  us/op
Bencher.arrayListBloomFilterAdd                         2  avgt    5     0.255 ±   0.166  us/op
Bencher.arrayListBloomFilterAdd                         4  avgt    5     0.308 ±   0.023  us/op
Bencher.arrayListBloomFilterAdd                         8  avgt    5     0.660 ±   0.155  us/op
Bencher.arrayListBloomFilterAdd                        16  avgt    5     1.259 ±   0.163  us/op
Bencher.arrayListBloomFilterAdd                        32  avgt    5     2.877 ±   0.913  us/op
Bencher.arrayListBloomFilterAdd                        64  avgt    5     7.515 ±   0.366  us/op
Bencher.arrayListBloomFilterAdd                       128  avgt    5    16.834 ±   2.082  us/op
Bencher.arrayListBloomFilterAdd                       256  avgt    5    41.073 ±  13.995  us/op
Bencher.arrayListBloomFilterAdd                       512  avgt    5    78.079 ±   9.530  us/op
Bencher.arrayListBloomFilterAdd                      1024  avgt    5   147.251 ±  45.300  us/op
Bencher.arrayListBloomFilterAdd                      2048  avgt    5   291.278 ±  52.495  us/op
Bencher.arrayListBloomFilterAdd                      4096  avgt    5   566.493 ±  17.060  us/op
Bencher.arrayListBloomFilterAdd                      8192  avgt    5  1120.526 ±  13.123  us/op
Bencher.arrayListBloomFilterAdd                     16384  avgt    5  2369.673 ±  87.655  us/op
Bencher.arrayListBloomFilterContains                    2  avgt    5     0.170 ±   0.169  us/op
Bencher.arrayListBloomFilterContains                    4  avgt    5     0.337 ±   0.063  us/op
Bencher.arrayListBloomFilterContains                    8  avgt    5     0.653 ±   0.155  us/op
Bencher.arrayListBloomFilterContains                   16  avgt    5     1.509 ±   0.330  us/op
Bencher.arrayListBloomFilterContains                   32  avgt    5     3.044 ±   1.646  us/op
Bencher.arrayListBloomFilterContains                   64  avgt    5     6.876 ±   1.497  us/op
Bencher.arrayListBloomFilterContains                  128  avgt    5    15.305 ±   3.923  us/op
Bencher.arrayListBloomFilterContains                  256  avgt    5    32.686 ±   5.131  us/op
Bencher.arrayListBloomFilterContains                  512  avgt    5    67.476 ±   7.400  us/op
Bencher.arrayListBloomFilterContains                 1024  avgt    5   127.422 ±  28.920  us/op
Bencher.arrayListBloomFilterContains                 2048  avgt    5   269.687 ±  56.847  us/op
Bencher.arrayListBloomFilterContains                 4096  avgt    5   548.914 ± 326.191  us/op
Bencher.arrayListBloomFilterContains                 8192  avgt    5  1001.028 ±  14.162  us/op
Bencher.arrayListBloomFilterContains                16384  avgt    5  2132.437 ± 140.680  us/op
Bencher.hashsetAdd                                      2  avgt    5     0.049 ±   0.001  us/op
Bencher.hashsetAdd                                      4  avgt    5     0.061 ±   0.009  us/op
Bencher.hashsetAdd                                      8  avgt    5     0.105 ±   0.023  us/op
Bencher.hashsetAdd                                     16  avgt    5     0.151 ±   0.008  us/op
Bencher.hashsetAdd                                     32  avgt    5     0.317 ±   0.031  us/op
Bencher.hashsetAdd                                     64  avgt    5     0.601 ±   0.021  us/op
Bencher.hashsetAdd                                    128  avgt    5     1.203 ±   0.052  us/op
Bencher.hashsetAdd                                    256  avgt    5     2.583 ±   0.296  us/op
Bencher.hashsetAdd                                    512  avgt    5     6.239 ±   5.638  us/op
Bencher.hashsetAdd                                   1024  avgt    5    14.080 ±  14.472  us/op
Bencher.hashsetAdd                                   2048  avgt    5    35.012 ±   8.367  us/op
Bencher.hashsetAdd                                   4096  avgt    5    64.546 ±  58.619  us/op
Bencher.hashsetAdd                                   8192  avgt    5   181.459 ±  44.798  us/op
Bencher.hashsetAdd                                  16384  avgt    5   465.066 ± 207.888  us/op
Bencher.hashsetAddAll                                   2  avgt    5     0.047 ±   0.003  us/op
Bencher.hashsetAddAll                                   4  avgt    5     0.074 ±   0.010  us/op
Bencher.hashsetAddAll                                   8  avgt    5     0.119 ±   0.007  us/op
Bencher.hashsetAddAll                                  16  avgt    5     0.196 ±   0.016  us/op
Bencher.hashsetAddAll                                  32  avgt    5     0.369 ±   0.045  us/op
Bencher.hashsetAddAll                                  64  avgt    5     0.723 ±   0.075  us/op
Bencher.hashsetAddAll                                 128  avgt    5     1.517 ±   0.128  us/op
Bencher.hashsetAddAll                                 256  avgt    5     3.283 ±   0.201  us/op
Bencher.hashsetAddAll                                 512  avgt    5     7.370 ±   3.581  us/op
Bencher.hashsetAddAll                                1024  avgt    5    13.872 ±   0.590  us/op
Bencher.hashsetAddAll                                2048  avgt    5    32.564 ±   4.961  us/op
Bencher.hashsetAddAll                                4096  avgt    5    75.688 ±   5.992  us/op
Bencher.hashsetAddAll                                8192  avgt    5   186.309 ±  22.802  us/op
Bencher.hashsetAddAll                               16384  avgt    5   453.155 ±  68.536  us/op
Bencher.hashsetContains                                 2  avgt    5     0.022 ±   0.010  us/op
Bencher.hashsetContains                                 4  avgt    5     0.026 ±   0.046  us/op
Bencher.hashsetContains                                 8  avgt    5     0.048 ±   0.079  us/op
Bencher.hashsetContains                                16  avgt    5     0.071 ±   0.093  us/op
Bencher.hashsetContains                                32  avgt    5     0.099 ±   0.016  us/op
Bencher.hashsetContains                                64  avgt    5     0.185 ±   0.019  us/op
Bencher.hashsetContains                               128  avgt    5     0.356 ±   0.013  us/op
Bencher.hashsetContains                               256  avgt    5     0.688 ±   0.029  us/op
Bencher.hashsetContains                               512  avgt    5     1.362 ±   0.031  us/op
Bencher.hashsetContains                              1024  avgt    5     2.694 ±   0.018  us/op
Bencher.hashsetContains                              2048  avgt    5     5.426 ±   0.147  us/op
Bencher.hashsetContains                              4096  avgt    5    11.160 ±   0.899  us/op
Bencher.hashsetContains                              8192  avgt    5    24.932 ±   2.217  us/op
Bencher.hashsetContains                             16384  avgt    5    79.650 ±  14.310  us/op
ObjectToByteArrayBenchmark.serilizationDouble         N/A  avgt    5     0.476 ±   0.068  us/op
ObjectToByteArrayBenchmark.serilizationInteger        N/A  avgt    5     0.475 ±   0.059  us/op
ObjectToByteArrayBenchmark.serilizationString         N/A  avgt    5     0.338 ±   0.026  us/op
ObjectToByteArrayBenchmark.stringGetBytesDouble       N/A  avgt    5     0.110 ±   0.005  us/op
ObjectToByteArrayBenchmark.stringGetBytesInteger      N/A  avgt    5     0.034 ±   0.003  us/op
ObjectToByteArrayBenchmark.stringGetBytesString       N/A  avgt    5     0.064 ±   0.008  us/op
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
            continue

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
