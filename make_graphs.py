from matplotlib import pyplot as plt
from math import log

data = """
Benchmark                                         (items)  Mode  Cnt         Score        Error  Units
Bencher.arrayBloomFilterAdd                             2  avgt    5         0.076 ±      0.043  us/op
Bencher.arrayBloomFilterAdd                             4  avgt    5         0.124 ±      0.009  us/op
Bencher.arrayBloomFilterAdd                             8  avgt    5         0.251 ±      0.107  us/op
Bencher.arrayBloomFilterAdd                            16  avgt    5         0.455 ±      0.016  us/op
Bencher.arrayBloomFilterAdd                            32  avgt    5         0.869 ±      0.032  us/op
Bencher.arrayBloomFilterAdd                            64  avgt    5         1.696 ±      0.080  us/op
Bencher.arrayBloomFilterAdd                           128  avgt    5         4.452 ±      0.438  us/op
Bencher.arrayBloomFilterAdd                           256  avgt    5         9.350 ±      0.792  us/op
Bencher.arrayBloomFilterAdd                           512  avgt    5        33.236 ±      0.203  us/op
Bencher.arrayBloomFilterAdd                          1024  avgt    5        70.687 ±     12.394  us/op
Bencher.arrayBloomFilterAdd                          2048  avgt    5       147.321 ±     17.079  us/op
Bencher.arrayBloomFilterAdd                          4096  avgt    5       275.007 ±     36.451  us/op
Bencher.arrayBloomFilterAdd                          8192  avgt    5       559.725 ±     21.785  us/op
Bencher.arrayBloomFilterContains                        2  avgt    5         0.070 ±      0.030  us/op
Bencher.arrayBloomFilterContains                        4  avgt    5         0.115 ±      0.012  us/op
Bencher.arrayBloomFilterContains                        8  avgt    5         0.186 ±      0.072  us/op
Bencher.arrayBloomFilterContains                       16  avgt    5         0.343 ±      0.046  us/op
Bencher.arrayBloomFilterContains                       32  avgt    5         0.651 ±      0.114  us/op
Bencher.arrayBloomFilterContains                       64  avgt    5         1.324 ±      0.288  us/op
Bencher.arrayBloomFilterContains                      128  avgt    5         2.425 ±      0.451  us/op
Bencher.arrayBloomFilterContains                      256  avgt    5         5.101 ±      1.117  us/op
Bencher.arrayBloomFilterContains                      512  avgt    5        14.572 ±      2.581  us/op
Bencher.arrayBloomFilterContains                     1024  avgt    5        28.394 ±      2.314  us/op
Bencher.arrayBloomFilterContains                     2048  avgt    5        60.743 ±     13.630  us/op
Bencher.arrayBloomFilterContains                     4096  avgt    5        90.017 ±     23.582  us/op
Bencher.arrayBloomFilterContains                     8192  avgt    5       178.845 ±     27.856  us/op
Bencher.arrayListBloomFilterAdd                         2  avgt    5         0.080 ±      0.043  us/op
Bencher.arrayListBloomFilterAdd                         4  avgt    5         0.137 ±      0.058  us/op
Bencher.arrayListBloomFilterAdd                         8  avgt    5         0.256 ±      0.114  us/op
Bencher.arrayListBloomFilterAdd                        16  avgt    5         0.476 ±      0.170  us/op
Bencher.arrayListBloomFilterAdd                        32  avgt    5         0.893 ±      0.030  us/op
Bencher.arrayListBloomFilterAdd                        64  avgt    5         1.747 ±      0.115  us/op
Bencher.arrayListBloomFilterAdd                       128  avgt    5         4.443 ±      0.160  us/op
Bencher.arrayListBloomFilterAdd                       256  avgt    5         9.462 ±      1.805  us/op
Bencher.arrayListBloomFilterAdd                       512  avgt    5        33.580 ±      1.070  us/op
Bencher.arrayListBloomFilterAdd                      1024  avgt    5        71.131 ±      3.120  us/op
Bencher.arrayListBloomFilterAdd                      2048  avgt    5       146.321 ±     22.263  us/op
Bencher.arrayListBloomFilterAdd                      4096  avgt    5       281.415 ±     40.842  us/op
Bencher.arrayListBloomFilterAdd                      8192  avgt    5       565.145 ±     13.229  us/op
Bencher.arrayListBloomFilterContains                    2  avgt    5         0.072 ±      0.033  us/op
Bencher.arrayListBloomFilterContains                    4  avgt    5         0.114 ±      0.032  us/op
Bencher.arrayListBloomFilterContains                    8  avgt    5         0.196 ±      0.065  us/op
Bencher.arrayListBloomFilterContains                   16  avgt    5         0.359 ±      0.071  us/op
Bencher.arrayListBloomFilterContains                   32  avgt    5         0.656 ±      0.058  us/op
Bencher.arrayListBloomFilterContains                   64  avgt    5         1.267 ±      0.158  us/op
Bencher.arrayListBloomFilterContains                  128  avgt    5         2.411 ±      0.163  us/op
Bencher.arrayListBloomFilterContains                  256  avgt    5         4.922 ±      1.084  us/op
Bencher.arrayListBloomFilterContains                  512  avgt    5        13.816 ±      0.423  us/op
Bencher.arrayListBloomFilterContains                 1024  avgt    5        28.762 ±      3.989  us/op
Bencher.arrayListBloomFilterContains                 2048  avgt    5        52.100 ±     34.029  us/op
Bencher.arrayListBloomFilterContains                 4096  avgt    5        97.943 ±     61.743  us/op
Bencher.arrayListBloomFilterContains                 8192  avgt    5       185.108 ±     45.971  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             2  avgt    5         0.175 ±      0.019  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             4  avgt    5         0.358 ±      0.057  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd             8  avgt    5         0.702 ±      0.126  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            16  avgt    5         1.278 ±      0.181  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            32  avgt    5         2.244 ±      0.431  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd            64  avgt    5         4.712 ±      0.413  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           128  avgt    5         9.155 ±      3.076  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           256  avgt    5        19.359 ±      2.842  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           512  avgt    5        45.275 ±      3.707  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          1024  avgt    5       106.352 ±      2.193  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          2048  avgt    5       219.092 ±     16.184  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          4096  avgt    5       413.210 ±     19.336  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          8192  avgt    5       830.881 ±     45.375  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        2  avgt    5         0.094 ±      0.008  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        4  avgt    5         0.146 ±      0.020  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains        8  avgt    5         0.273 ±      0.108  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       16  avgt    5         0.508 ±      0.163  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       32  avgt    5         0.861 ±      0.056  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains       64  avgt    5         1.784 ±      0.378  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      128  avgt    5         3.394 ±      1.157  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      256  avgt    5         6.828 ±      1.825  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      512  avgt    5        16.136 ±      3.742  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     1024  avgt    5        33.489 ±      9.377  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     2048  avgt    5        68.015 ±     42.307  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     4096  avgt    5       114.159 ±     53.370  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     8192  avgt    5       237.739 ±     20.018  us/op
Bencher.hashsetAdd                                      2  avgt    5         0.072 ±      0.015  us/op
Bencher.hashsetAdd                                      4  avgt    5         0.095 ±      0.024  us/op
Bencher.hashsetAdd                                      8  avgt    5         0.147 ±      0.051  us/op
Bencher.hashsetAdd                                     16  avgt    5         0.272 ±      0.056  us/op
Bencher.hashsetAdd                                     32  avgt    5         0.539 ±      0.184  us/op
Bencher.hashsetAdd                                     64  avgt    5         0.934 ±      0.185  us/op
Bencher.hashsetAdd                                    128  avgt    5         2.155 ±      0.872  us/op
Bencher.hashsetAdd                                    256  avgt    5         4.435 ±      0.928  us/op
Bencher.hashsetAdd                                    512  avgt    5        10.028 ±      2.149  us/op
Bencher.hashsetAdd                                   1024  avgt    5        17.095 ±      3.133  us/op
Bencher.hashsetAdd                                   2048  avgt    5        34.481 ±      9.074  us/op
Bencher.hashsetAdd                                   4096  avgt    5        89.823 ±     35.059  us/op
Bencher.hashsetAdd                                   8192  avgt    5       237.897 ±    136.261  us/op
Bencher.hashsetAddAll                                   2  avgt    5         0.065 ±      0.024  us/op
Bencher.hashsetAddAll                                   4  avgt    5         0.104 ±      0.039  us/op
Bencher.hashsetAddAll                                   8  avgt    5         0.161 ±      0.023  us/op
Bencher.hashsetAddAll                                  16  avgt    5         0.276 ±      0.053  us/op
Bencher.hashsetAddAll                                  32  avgt    5         0.551 ±      0.122  us/op
Bencher.hashsetAddAll                                  64  avgt    5         1.129 ±      0.243  us/op
Bencher.hashsetAddAll                                 128  avgt    5         2.254 ±      0.154  us/op
Bencher.hashsetAddAll                                 256  avgt    5         4.978 ±      1.073  us/op
Bencher.hashsetAddAll                                 512  avgt    5         9.409 ±      1.488  us/op
Bencher.hashsetAddAll                                1024  avgt    5        20.429 ±      3.913  us/op
Bencher.hashsetAddAll                                2048  avgt    5        41.259 ±      2.896  us/op
Bencher.hashsetAddAll                                4096  avgt    5        89.467 ±     28.291  us/op
Bencher.hashsetAddAll                                8192  avgt    5       229.567 ±     58.586  us/op
Bencher.hashsetContains                                 2  avgt    5         0.043 ±      0.004  us/op
Bencher.hashsetContains                                 4  avgt    5         0.063 ±      0.007  us/op
Bencher.hashsetContains                                 8  avgt    5         0.069 ±      0.012  us/op
Bencher.hashsetContains                                16  avgt    5         0.113 ±      0.021  us/op
Bencher.hashsetContains                                32  avgt    5         0.189 ±      0.178  us/op
Bencher.hashsetContains                                64  avgt    5         0.338 ±      0.291  us/op
Bencher.hashsetContains                               128  avgt    5         0.554 ±      0.366  us/op
Bencher.hashsetContains                               256  avgt    5         1.146 ±      0.531  us/op
Bencher.hashsetContains                               512  avgt    5         1.981 ±      0.487  us/op
Bencher.hashsetContains                              1024  avgt    5         3.879 ±      0.451  us/op
Bencher.hashsetContains                              2048  avgt    5         8.542 ±      3.940  us/op
Bencher.hashsetContains                              4096  avgt    5        20.641 ±     32.405  us/op
Bencher.hashsetContains                              8192  avgt    5        42.728 ±     73.660  us/op
Bencher.linkedListBloomFilterAdd                        2  avgt    5         0.786 ±      0.948  us/op
Bencher.linkedListBloomFilterAdd                        4  avgt    5         3.609 ±      4.385  us/op
Bencher.linkedListBloomFilterAdd                        8  avgt    5        16.785 ±     16.390  us/op
Bencher.linkedListBloomFilterAdd                       16  avgt    5        77.294 ±     44.445  us/op
Bencher.linkedListBloomFilterAdd                       32  avgt    5       292.783 ±     43.741  us/op
Bencher.linkedListBloomFilterAdd                       64  avgt    5      1216.470 ±    319.711  us/op
Bencher.linkedListBloomFilterAdd                      128  avgt    5      4875.239 ±    352.387  us/op
Bencher.linkedListBloomFilterAdd                      256  avgt    5     20011.147 ±   1619.099  us/op
Bencher.linkedListBloomFilterAdd                      512  avgt    5     82347.974 ±   4121.082  us/op
Bencher.linkedListBloomFilterAdd                     1024  avgt    5    338723.321 ±  18271.964  us/op
Bencher.linkedListBloomFilterAdd                     2048  avgt    5   1413374.600 ±  73367.703  us/op
Bencher.linkedListBloomFilterAdd                     4096  avgt    5   5633575.833 ± 150764.845  us/op
Bencher.linkedListBloomFilterAdd                     8192  avgt    5  22679455.283 ± 467797.922  us/op
Bencher.linkedListBloomFilterContains                   2  avgt    5         0.441 ±      0.827  us/op
Bencher.linkedListBloomFilterContains                   4  avgt    5         1.729 ±      2.329  us/op
Bencher.linkedListBloomFilterContains                   8  avgt    5        11.667 ±     11.443  us/op
Bencher.linkedListBloomFilterContains                  16  avgt    5        42.152 ±     12.663  us/op
Bencher.linkedListBloomFilterContains                  32  avgt    5       172.258 ±    108.853  us/op
Bencher.linkedListBloomFilterContains                  64  avgt    5       732.707 ±    404.263  us/op
Bencher.linkedListBloomFilterContains                 128  avgt    5      2779.024 ±    665.508  us/op
Bencher.linkedListBloomFilterContains                 256  avgt    5     11930.227 ±   1284.901  us/op
Bencher.linkedListBloomFilterContains                 512  avgt    5     49496.850 ±   4448.429  us/op
Bencher.linkedListBloomFilterContains                1024  avgt    5    196370.595 ±  14407.586  us/op
Bencher.linkedListBloomFilterContains                2048  avgt    5    804727.805 ±  49154.621  us/op
Bencher.linkedListBloomFilterContains                4096  avgt    5   3240470.258 ± 102841.867  us/op
Bencher.linkedListBloomFilterContains                8192  avgt    5  13689682.425 ± 556627.208  us/op
Bencher.nativeBitSetBloomFilterAdd                      2  avgt    5         0.136 ±      0.030  us/op
Bencher.nativeBitSetBloomFilterAdd                      4  avgt    5         0.241 ±      0.045  us/op
Bencher.nativeBitSetBloomFilterAdd                      8  avgt    5         0.487 ±      0.139  us/op
Bencher.nativeBitSetBloomFilterAdd                     16  avgt    5         0.863 ±      0.096  us/op
Bencher.nativeBitSetBloomFilterAdd                     32  avgt    5         1.670 ±      0.266  us/op
Bencher.nativeBitSetBloomFilterAdd                     64  avgt    5         3.526 ±      0.383  us/op
Bencher.nativeBitSetBloomFilterAdd                    128  avgt    5         6.564 ±      0.341  us/op
Bencher.nativeBitSetBloomFilterAdd                    256  avgt    5        15.351 ±      8.209  us/op
Bencher.nativeBitSetBloomFilterAdd                    512  avgt    5        31.295 ±      3.484  us/op
Bencher.nativeBitSetBloomFilterAdd                   1024  avgt    5        85.038 ±      5.371  us/op
Bencher.nativeBitSetBloomFilterAdd                   2048  avgt    5       170.098 ±      4.247  us/op
Bencher.nativeBitSetBloomFilterAdd                   4096  avgt    5       320.334 ±     27.409  us/op
Bencher.nativeBitSetBloomFilterAdd                   8192  avgt    5       656.257 ±     89.046  us/op
Bencher.nativeBitSetBloomFilterContains                 2  avgt    5         0.072 ±      0.031  us/op
Bencher.nativeBitSetBloomFilterContains                 4  avgt    5         0.120 ±      0.018  us/op
Bencher.nativeBitSetBloomFilterContains                 8  avgt    5         0.223 ±      0.058  us/op
Bencher.nativeBitSetBloomFilterContains                16  avgt    5         0.411 ±      0.041  us/op
Bencher.nativeBitSetBloomFilterContains                32  avgt    5         0.803 ±      0.122  us/op
Bencher.nativeBitSetBloomFilterContains                64  avgt    5         1.506 ±      0.025  us/op
Bencher.nativeBitSetBloomFilterContains               128  avgt    5         2.917 ±      0.295  us/op
Bencher.nativeBitSetBloomFilterContains               256  avgt    5         6.261 ±      2.044  us/op
Bencher.nativeBitSetBloomFilterContains               512  avgt    5        16.223 ±      0.415  us/op
Bencher.nativeBitSetBloomFilterContains              1024  avgt    5        34.090 ±      4.309  us/op
Bencher.nativeBitSetBloomFilterContains              2048  avgt    5        62.480 ±     38.274  us/op
Bencher.nativeBitSetBloomFilterContains              4096  avgt    5        99.191 ±     21.973  us/op
Bencher.nativeBitSetBloomFilterContains              8192  avgt    5       216.468 ±     41.648  us/op
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
