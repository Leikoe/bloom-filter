from matplotlib import pyplot as plt
from math import log

data = """
Benchmark                                  (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                    100  avgt    5     1.478 ±    0.034  us/op
Bencher.arrayBloomFilterAdd                   1000  avgt    5    24.436 ±    3.887  us/op
Bencher.arrayBloomFilterAdd                  10000  avgt    5   328.369 ±    2.707  us/op
Bencher.arrayBloomFilterAdd                 100000  avgt    5  3517.604 ±   35.190  us/op
Bencher.arrayBloomFilterContains               100  avgt    5     0.585 ±    0.074  us/op
Bencher.arrayBloomFilterContains              1000  avgt    5     6.193 ±    0.259  us/op
Bencher.arrayBloomFilterContains             10000  avgt    5    54.645 ±    9.124  us/op
Bencher.arrayBloomFilterContains            100000  avgt    5  1161.220 ±   63.669  us/op
Bencher.hashsetAdd                             100  avgt    5     0.932 ±    0.043  us/op
Bencher.hashsetAdd                            1000  avgt    5    15.195 ±    1.473  us/op
Bencher.hashsetAdd                           10000  avgt    5    96.553 ±    4.492  us/op
Bencher.hashsetAdd                          100000  avgt    5  4603.830 ± 1697.956  us/op
Bencher.hashsetContains                        100  avgt    5     0.443 ±    0.005  us/op
Bencher.hashsetContains                       1000  avgt    5     4.188 ±    0.046  us/op
Bencher.hashsetContains                      10000  avgt    5    42.362 ±   33.928  us/op
Bencher.hashsetContains                     100000  avgt    5   907.511 ±   29.914  us/op
Bencher.nativeBitSetBloomFilterAdd             100  avgt    5     3.545 ±    0.084  us/op
Bencher.nativeBitSetBloomFilterAdd            1000  avgt    5    37.928 ±    1.735  us/op
Bencher.nativeBitSetBloomFilterAdd           10000  avgt    5   374.142 ±    3.135  us/op
Bencher.nativeBitSetBloomFilterAdd          100000  avgt    5  3999.398 ±   78.842  us/op
Bencher.nativeBitSetBloomFilterContains        100  avgt    5     0.585 ±    0.063  us/op
Bencher.nativeBitSetBloomFilterContains       1000  avgt    5     6.432 ±    0.581  us/op
Bencher.nativeBitSetBloomFilterContains      10000  avgt    5    58.313 ±    1.963  us/op
Bencher.nativeBitSetBloomFilterContains     100000  avgt    5   621.454 ±   15.033  us/op
Bencher.vectorizedArrayBloomFilterAdd          100  avgt    5     1.333 ±    0.045  us/op
Bencher.vectorizedArrayBloomFilterAdd         1000  avgt    5    13.542 ±    0.912  us/op
Bencher.vectorizedArrayBloomFilterAdd        10000  avgt    5   148.714 ±    0.325  us/op
Bencher.vectorizedArrayBloomFilterAdd       100000  avgt    5  1513.773 ±    8.718  us/op
Bencher.vectoziedArrayBloomFilterContains      100  avgt    5     0.811 ±    0.180  us/op
Bencher.vectoziedArrayBloomFilterContains     1000  avgt    5     8.154 ±    0.762  us/op
Bencher.vectoziedArrayBloomFilterContains    10000  avgt    5    75.541 ±    2.582  us/op
Bencher.vectoziedArrayBloomFilterContains   100000  avgt    5  1552.845 ±   15.208  us/op
"""


"""
Benchmark                                         (items)  Mode  Cnt     Score     Error  Units
Bencher.arrayBloomFilterAdd                           100  avgt   25     1.477 ±   0.012  us/op
Bencher.arrayBloomFilterAdd                          1000  avgt   25    24.887 ±   0.088  us/op
Bencher.arrayBloomFilterAdd                         10000  avgt   25   329.425 ±   1.004  us/op
Bencher.arrayBloomFilterAdd                        100000  avgt   25  3517.357 ±   9.579  us/op
Bencher.arrayBloomFilterContains                      100  avgt   25     0.584 ±   0.018  us/op
Bencher.arrayBloomFilterContains                     1000  avgt   25     6.114 ±   0.070  us/op
Bencher.arrayBloomFilterContains                    10000  avgt   25    62.781 ±   4.306  us/op
Bencher.arrayBloomFilterContains                   100000  avgt   25  1131.656 ±   8.145  us/op
Bencher.arrayListBloomFilterAdd                       100  avgt   25     1.452 ±   0.005  us/op
Bencher.arrayListBloomFilterAdd                      1000  avgt   25    26.251 ±   2.247  us/op
Bencher.arrayListBloomFilterAdd                     10000  avgt   25   331.910 ±   0.753  us/op
Bencher.arrayListBloomFilterAdd                    100000  avgt   25  3561.399 ±  23.927  us/op
Bencher.arrayListBloomFilterContains                  100  avgt   25     0.589 ±   0.015  us/op
Bencher.arrayListBloomFilterContains                 1000  avgt   25     6.151 ±   0.082  us/op
Bencher.arrayListBloomFilterContains                10000  avgt   25    63.978 ±   4.589  us/op
Bencher.arrayListBloomFilterContains               100000  avgt   25  1135.657 ±   6.904  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd           100  avgt   25     4.179 ±   0.032  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd          1000  avgt   25    58.809 ±   0.309  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd         10000  avgt   25   581.845 ±   1.211  us/op
Bencher.guavaLockFreeBitArrayBloomFilterAdd        100000  avgt   25  6255.794 ±  88.281  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains      100  avgt   25     0.659 ±   0.023  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains     1000  avgt   25     6.447 ±   0.101  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains    10000  avgt   25    66.934 ±   6.281  us/op
Bencher.guavaLockFreeBitArrayBloomFilterContains   100000  avgt   25   590.026 ±   3.020  us/op
Bencher.hashsetAdd                                    100  avgt   25     0.960 ±   0.067  us/op
Bencher.hashsetAdd                                   1000  avgt   25    14.612 ±   0.434  us/op
Bencher.hashsetAdd                                  10000  avgt   25    95.304 ±   1.078  us/op
Bencher.hashsetAdd                                 100000  avgt   25  4761.130 ± 289.650  us/op
Bencher.hashsetContains                               100  avgt   25     0.443 ±   0.001  us/op
Bencher.hashsetContains                              1000  avgt   25     4.263 ±   0.073  us/op
Bencher.hashsetContains                             10000  avgt   25    48.684 ±   1.509  us/op
Bencher.hashsetContains                            100000  avgt   25   895.255 ±  13.279  us/op
Bencher.nativeBitSetBloomFilterAdd                    100  avgt   25     3.614 ±   0.062  us/op
Bencher.nativeBitSetBloomFilterAdd                   1000  avgt   25    40.979 ±   1.615  us/op
Bencher.nativeBitSetBloomFilterAdd                  10000  avgt   25   372.055 ±   0.555  us/op
Bencher.nativeBitSetBloomFilterAdd                 100000  avgt   25  3966.699 ±  12.668  us/op
Bencher.nativeBitSetBloomFilterContains               100  avgt   25     0.593 ±   0.013  us/op
Bencher.nativeBitSetBloomFilterContains              1000  avgt   25     6.385 ±   0.088  us/op
Bencher.nativeBitSetBloomFilterContains             10000  avgt   25    65.492 ±   4.565  us/op
Bencher.nativeBitSetBloomFilterContains            100000  avgt   25   603.598 ±   8.679  us/op
Bencher.vectorizedArrayBloomFilterAdd                 100  avgt   25     2.053 ±   0.057  us/op
Bencher.vectorizedArrayBloomFilterAdd                1000  avgt   25    26.815 ±   0.260  us/op
Bencher.vectorizedArrayBloomFilterAdd               10000  avgt   25   324.683 ±   5.076  us/op
Bencher.vectorizedArrayBloomFilterAdd              100000  avgt   25  3873.737 ±  19.504  us/op
Bencher.vectoziedArrayBloomFilterContains             100  avgt   25     1.563 ±   0.031  us/op
Bencher.vectoziedArrayBloomFilterContains            1000  avgt   25    16.772 ±   0.255  us/op
Bencher.vectoziedArrayBloomFilterContains           10000  avgt   25   255.342 ±  25.247  us/op
Bencher.vectoziedArrayBloomFilterContains          100000  avgt   25  3401.183 ±  70.672  us/op
"""

"""
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
