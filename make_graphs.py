from matplotlib import pyplot as plt
from math import log

data = """
Benchmark                                     (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayNaiveBloomFilterAdd                  100  avgt    5     1.356 ±    0.004  us/op
Bencher.arrayNaiveBloomFilterAdd                 1000  avgt    5    24.745 ±    4.636  us/op
Bencher.arrayNaiveBloomFilterAdd                10000  avgt    5   316.812 ±   19.447  us/op
Bencher.arrayNaiveBloomFilterAdd               100000  avgt    5  3211.107 ±  112.279  us/op
Bencher.arrayNaiveBloomFilterContains             100  avgt    5     0.556 ±    0.056  us/op
Bencher.arrayNaiveBloomFilterContains            1000  avgt    5     5.587 ±    0.260  us/op
Bencher.arrayNaiveBloomFilterContains           10000  avgt    5    96.779 ±    5.369  us/op
Bencher.arrayNaiveBloomFilterContains          100000  avgt    5  1369.029 ±   37.333  us/op
Bencher.bloomFilterAdd                            100  avgt    5     1.178 ±    0.007  us/op
Bencher.bloomFilterAdd                           1000  avgt    5     9.958 ±    0.113  us/op
Bencher.bloomFilterAdd                          10000  avgt    5    80.860 ±    1.696  us/op
Bencher.bloomFilterAdd                         100000  avgt    5   900.933 ±    8.218  us/op
Bencher.bloomFilterContains                       100  avgt    5     0.619 ±    0.017  us/op
Bencher.bloomFilterContains                      1000  avgt    5     5.833 ±    0.041  us/op
Bencher.bloomFilterContains                     10000  avgt    5    56.760 ±   38.589  us/op
Bencher.bloomFilterContains                    100000  avgt    5  1382.041 ±   26.969  us/op
Bencher.hashsetAdd                                100  avgt    5     1.174 ±    0.127  us/op
Bencher.hashsetAdd                               1000  avgt    5    14.414 ±    0.548  us/op
Bencher.hashsetAdd                              10000  avgt    5   135.490 ±    2.725  us/op
Bencher.hashsetAdd                             100000  avgt    5  5064.750 ± 2307.996  us/op
Bencher.hashsetContains                           100  avgt    5     0.443 ±    0.005  us/op
Bencher.hashsetContains                          1000  avgt    5     4.444 ±    0.089  us/op
Bencher.hashsetContains                         10000  avgt    5    41.661 ±   27.414  us/op
Bencher.hashsetContains                        100000  avgt    5   901.771 ±   29.143  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd           100  avgt    5     3.631 ±    0.554  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd          1000  avgt    5    38.498 ±   24.935  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd         10000  avgt    5   363.404 ±    2.517  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd        100000  avgt    5  3795.377 ±   34.414  us/op
Bencher.nativeBitSetNaiveBloomFilterContains      100  avgt    5     0.589 ±    0.084  us/op
Bencher.nativeBitSetNaiveBloomFilterContains     1000  avgt    5     6.020 ±    0.088  us/op
Bencher.nativeBitSetNaiveBloomFilterContains    10000  avgt    5   107.155 ±   10.255  us/op
Bencher.nativeBitSetNaiveBloomFilterContains   100000  avgt    5  1422.956 ±   38.231  us/op
Bencher.ubfbContains                              100  avgt    5     0.742 ±    0.016  us/op
Bencher.ubfbContains                             1000  avgt    5     7.527 ±    0.205  us/op
Bencher.ubfbContains                            10000  avgt    5    67.081 ±    1.636  us/op
Bencher.ubfbContains                           100000  avgt    5   794.905 ±   15.074  us/op
Bencher.ufbfAdd                                   100  avgt    5     0.782 ±    0.015  us/op
Bencher.ufbfAdd                                  1000  avgt    5     7.603 ±    0.043  us/op
Bencher.ufbfAdd                                 10000  avgt    5    66.888 ±    0.451  us/op
Bencher.ufbfAdd                                100000  avgt    5   756.667 ±   12.733  us/op
"""

"""
Benchmark                                     (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayNaiveBloomFilterAdd                  100  avgt    5     1.355 ±    0.013  us/op
Bencher.arrayNaiveBloomFilterAdd                 1000  avgt    5    24.737 ±    4.720  us/op
Bencher.arrayNaiveBloomFilterAdd                10000  avgt    5   314.588 ±    1.645  us/op
Bencher.arrayNaiveBloomFilterAdd               100000  avgt    5  3203.032 ±   89.597  us/op
Bencher.arrayNaiveBloomFilterContains             100  avgt    5     0.553 ±    0.071  us/op
Bencher.arrayNaiveBloomFilterContains            1000  avgt    5     5.598 ±    0.081  us/op
Bencher.arrayNaiveBloomFilterContains           10000  avgt    5    93.577 ±    1.386  us/op
Bencher.arrayNaiveBloomFilterContains          100000  avgt    5  1440.319 ±  368.465  us/op
Bencher.bloomFilterAdd                            100  avgt    5     1.180 ±    0.010  us/op
Bencher.bloomFilterAdd                           1000  avgt    5     9.936 ±    0.065  us/op
Bencher.bloomFilterAdd                          10000  avgt    5    80.934 ±    0.614  us/op
Bencher.bloomFilterAdd                         100000  avgt    5   900.454 ±   13.640  us/op
Bencher.bloomFilterContains                       100  avgt    5     0.617 ±    0.027  us/op
Bencher.bloomFilterContains                      1000  avgt    5     5.958 ±    0.044  us/op
Bencher.bloomFilterContains                     10000  avgt    5    56.878 ±   40.270  us/op
Bencher.bloomFilterContains                    100000  avgt    5  1395.808 ±   11.448  us/op
Bencher.hashsetAdd                                100  avgt    5     1.121 ±    0.065  us/op
Bencher.hashsetAdd                               1000  avgt    5     9.615 ±    0.423  us/op
Bencher.hashsetAdd                              10000  avgt    5   131.679 ±   17.098  us/op
Bencher.hashsetAdd                             100000  avgt    5  4858.915 ± 1622.679  us/op
Bencher.hashsetContains                           100  avgt    5     0.444 ±    0.002  us/op
Bencher.hashsetContains                          1000  avgt    5     4.461 ±    0.038  us/op
Bencher.hashsetContains                         10000  avgt    5    41.731 ±   29.195  us/op
Bencher.hashsetContains                        100000  avgt    5   916.260 ±   55.180  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd           100  avgt    5     3.575 ±    0.036  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd          1000  avgt    5    36.057 ±    1.488  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd         10000  avgt    5   356.813 ±    1.939  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd        100000  avgt    5  3622.171 ±   30.487  us/op
Bencher.nativeBitSetNaiveBloomFilterContains      100  avgt    5     0.597 ±    0.067  us/op
Bencher.nativeBitSetNaiveBloomFilterContains     1000  avgt    5     6.028 ±    0.597  us/op
Bencher.nativeBitSetNaiveBloomFilterContains    10000  avgt    5   104.828 ±   13.633  us/op
Bencher.nativeBitSetNaiveBloomFilterContains   100000  avgt    5  1403.686 ±   50.587  us/op
Bencher.ubfbContains                              100  avgt    5     0.747 ±    0.012  us/op
Bencher.ubfbContains                             1000  avgt    5     7.299 ±    0.170  us/op
Bencher.ubfbContains                            10000  avgt    5    65.430 ±    1.048  us/op
Bencher.ubfbContains                           100000  avgt    5   780.492 ±    4.224  us/op
Bencher.ufbfAdd                                   100  avgt    5     0.799 ±    0.002  us/op
Bencher.ufbfAdd                                  1000  avgt    5     7.942 ±    0.056  us/op
Bencher.ufbfAdd                                 10000  avgt    5    67.605 ±    2.766  us/op
Bencher.ufbfAdd                                100000  avgt    5   768.717 ±   16.564  us/op
"""

"""
Benchmark                                     (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayNaiveBloomFilterAdd                  100  avgt    5     1.372 ±    0.005  us/op
Bencher.arrayNaiveBloomFilterAdd                 1000  avgt    5    24.960 ±    5.181  us/op
Bencher.arrayNaiveBloomFilterAdd                10000  avgt    5   317.645 ±    1.902  us/op
Bencher.arrayNaiveBloomFilterAdd               100000  avgt    5  3309.172 ±   37.775  us/op
Bencher.arrayNaiveBloomFilterContains             100  avgt    5     0.557 ±    0.090  us/op
Bencher.arrayNaiveBloomFilterContains            1000  avgt    5     5.605 ±    0.109  us/op
Bencher.arrayNaiveBloomFilterContains           10000  avgt    5    99.173 ±    4.064  us/op
Bencher.arrayNaiveBloomFilterContains          100000  avgt    5  1371.278 ±   55.086  us/op
Bencher.bloomFilterAdd                            100  avgt    5     1.174 ±    0.007  us/op
Bencher.bloomFilterAdd                           1000  avgt    5    11.478 ±    0.080  us/op
Bencher.bloomFilterAdd                          10000  avgt    5    95.422 ±    0.272  us/op
Bencher.bloomFilterAdd                         100000  avgt    5   964.667 ±    5.146  us/op
Bencher.bloomFilterContains                       100  avgt    5     0.790 ±    0.068  us/op
Bencher.bloomFilterContains                      1000  avgt    5     9.264 ±    0.036  us/op
Bencher.bloomFilterContains                     10000  avgt    5    87.068 ±    0.676  us/op
Bencher.bloomFilterContains                    100000  avgt    5   875.694 ±    5.130  us/op
Bencher.hashsetAdd                                100  avgt    5     1.124 ±    0.072  us/op
Bencher.hashsetAdd                               1000  avgt    5    14.884 ±    2.104  us/op
Bencher.hashsetAdd                              10000  avgt    5   133.098 ±   13.506  us/op
Bencher.hashsetAdd                             100000  avgt    5  4960.349 ± 1258.073  us/op
Bencher.hashsetContains                           100  avgt    5     0.443 ±    0.003  us/op
Bencher.hashsetContains                          1000  avgt    5     4.250 ±    0.049  us/op
Bencher.hashsetContains                         10000  avgt    5    43.690 ±   35.932  us/op
Bencher.hashsetContains                        100000  avgt    5   895.736 ±   27.941  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd           100  avgt    5     3.582 ±    0.054  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd          1000  avgt    5    38.450 ±   25.104  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd         10000  avgt    5   357.303 ±    7.697  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd        100000  avgt    5  3612.649 ±   12.379  us/op
Bencher.nativeBitSetNaiveBloomFilterContains      100  avgt    5     0.603 ±    0.003  us/op
Bencher.nativeBitSetNaiveBloomFilterContains     1000  avgt    5     5.978 ±    0.267  us/op
Bencher.nativeBitSetNaiveBloomFilterContains    10000  avgt    5   107.734 ±    4.445  us/op
Bencher.nativeBitSetNaiveBloomFilterContains   100000  avgt    5  1412.850 ±   16.259  us/op
Bencher.ubfbContains                              100  avgt    5     0.800 ±    0.055  us/op
Bencher.ubfbContains                             1000  avgt    5     7.775 ±    0.199  us/op
Bencher.ubfbContains                            10000  avgt    5    75.638 ±    1.573  us/op
Bencher.ubfbContains                           100000  avgt    5   761.850 ±    6.644  us/op
Bencher.ufbfAdd                                   100  avgt    5     1.020 ±    0.047  us/op
Bencher.ufbfAdd                                  1000  avgt    5     9.856 ±    0.042  us/op
Bencher.ufbfAdd                                 10000  avgt    5    90.850 ±    0.628  us/op
Bencher.ufbfAdd                                100000  avgt    5   959.212 ±   11.169  us/op
"""

"""
Benchmark                                     (items)  Mode  Cnt     Score     Error  Units
Bencher.arrayNaiveBloomFilterAdd                  100  avgt    5     1.415 ±   0.041  us/op
Bencher.arrayNaiveBloomFilterAdd                 1000  avgt    5    23.533 ±   2.473  us/op
Bencher.arrayNaiveBloomFilterAdd                10000  avgt    5   322.147 ±  10.871  us/op
Bencher.arrayNaiveBloomFilterAdd               100000  avgt    5  3238.508 ±  32.176  us/op
Bencher.arrayNaiveBloomFilterContains             100  avgt    5     0.604 ±   0.010  us/op
Bencher.arrayNaiveBloomFilterContains            1000  avgt    5     6.293 ±   0.147  us/op
Bencher.arrayNaiveBloomFilterContains           10000  avgt    5    97.360 ±   8.544  us/op
Bencher.arrayNaiveBloomFilterContains          100000  avgt    5  1403.284 ±  26.958  us/op
Bencher.bloomFilterAdd                            100  avgt    5     1.017 ±   0.005  us/op
Bencher.bloomFilterAdd                           1000  avgt    5     9.984 ±   0.049  us/op
Bencher.bloomFilterAdd                          10000  avgt    5    91.493 ±   0.561  us/op
Bencher.bloomFilterAdd                         100000  avgt    5   919.778 ±   6.273  us/op
Bencher.bloomFilterContains                       100  avgt    5     0.747 ±   0.071  us/op
Bencher.bloomFilterContains                      1000  avgt    5     9.318 ±   0.130  us/op
Bencher.bloomFilterContains                     10000  avgt    5    92.100 ±   3.535  us/op
Bencher.bloomFilterContains                    100000  avgt    5   935.596 ±   4.847  us/op
Bencher.hashsetAdd                                100  avgt    5     1.151 ±   0.036  us/op
Bencher.hashsetAdd                               1000  avgt    5    14.629 ±   1.491  us/op
Bencher.hashsetAdd                              10000  avgt    5   130.652 ±   3.092  us/op
Bencher.hashsetAdd                             100000  avgt    5  4772.713 ± 765.543  us/op
Bencher.hashsetContains                           100  avgt    5     0.444 ±   0.002  us/op
Bencher.hashsetContains                          1000  avgt    5     4.293 ±   0.036  us/op
Bencher.hashsetContains                         10000  avgt    5    42.802 ±  35.137  us/op
Bencher.hashsetContains                        100000  avgt    5   916.617 ±  62.974  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd           100  avgt    5     3.586 ±   0.056  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd          1000  avgt    5    39.055 ±  25.885  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd         10000  avgt    5   361.090 ±   3.403  us/op
Bencher.nativeBitSetNaiveBloomFilterAdd        100000  avgt    5  3699.224 ± 278.905  us/op
Bencher.nativeBitSetNaiveBloomFilterContains      100  avgt    5     0.670 ±   0.050  us/op
Bencher.nativeBitSetNaiveBloomFilterContains     1000  avgt    5     6.601 ±   0.137  us/op
Bencher.nativeBitSetNaiveBloomFilterContains    10000  avgt    5   107.570 ±   2.094  us/op
Bencher.nativeBitSetNaiveBloomFilterContains   100000  avgt    5  1428.585 ±  17.203  us/op
Bencher.ubfbContains                              100  avgt    5     0.829 ±   0.015  us/op
Bencher.ubfbContains                             1000  avgt    5     8.378 ±   0.179  us/op
Bencher.ubfbContains                            10000  avgt    5    67.609 ±   0.306  us/op
Bencher.ubfbContains                           100000  avgt    5   760.892 ±  30.832  us/op
Bencher.ufbfAdd                                   100  avgt    5     1.019 ±   0.013  us/op
Bencher.ufbfAdd                                  1000  avgt    5     9.872 ±   0.050  us/op
Bencher.ufbfAdd                                 10000  avgt    5    90.794 ±   0.616  us/op
Bencher.ufbfAdd                                100000  avgt    5   960.036 ±  14.312  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.416 ±    0.020  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.674 ±    0.109  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   317.746 ±    0.829  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3243.249 ±   38.665  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.609 ±    0.002  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.204 ±    0.159  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    97.751 ±    6.685  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1403.224 ±   19.729  us/op
Bencher.hashsetAdd                              100  avgt    5     1.158 ±    0.059  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.076 ±    2.145  us/op
Bencher.hashsetAdd                            10000  avgt    5   136.957 ±    8.591  us/op
Bencher.hashsetAdd                           100000  avgt    5  4736.956 ± 1991.299  us/op
Bencher.hashsetContains                         100  avgt    5     0.443 ±    0.008  us/op
Bencher.hashsetContains                        1000  avgt    5     4.431 ±    0.043  us/op
Bencher.hashsetContains                       10000  avgt    5    44.597 ±   43.980  us/op
Bencher.hashsetContains                      100000  avgt    5   921.483 ±   47.850  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.601 ±    0.077  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    36.641 ±    1.872  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   361.324 ±    2.795  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3656.156 ±   14.321  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.675 ±    0.043  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.590 ±    0.058  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   107.119 ±    6.623  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1422.586 ±   21.338  us/op
Bencher.ubfbContains                            100  avgt    5     0.814 ±    0.016  us/op
Bencher.ubfbContains                           1000  avgt    5     8.184 ±    0.020  us/op
Bencher.ubfbContains                          10000  avgt    5    67.721 ±    1.811  us/op
Bencher.ubfbContains                         100000  avgt    5   758.519 ±    6.934  us/op
Bencher.ufbfAdd                                 100  avgt    5     0.833 ±    0.013  us/op
Bencher.ufbfAdd                                1000  avgt    5     7.713 ±    0.030  us/op
Bencher.ufbfAdd                               10000  avgt    5    64.681 ±    0.716  us/op
Bencher.ufbfAdd                              100000  avgt    5   666.477 ±   16.281  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.300 ±    0.014  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    13.005 ±    0.187  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.352 ±    0.789  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1372.963 ±   14.266  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.700 ±    0.010  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.718 ±    0.101  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   129.335 ±    4.945  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1616.729 ±   11.175  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.412 ±    0.008  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.614 ±    0.233  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   317.719 ±    2.120  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3223.620 ±   63.592  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.615 ±    0.066  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.336 ±    0.413  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5   100.515 ±   21.525  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1419.285 ±   30.941  us/op
Bencher.hashsetAdd                              100  avgt    5     1.154 ±    0.069  us/op
Bencher.hashsetAdd                             1000  avgt    5     9.611 ±    0.411  us/op
Bencher.hashsetAdd                            10000  avgt    5    94.749 ±    5.432  us/op
Bencher.hashsetAdd                           100000  avgt    5  4617.015 ± 2092.568  us/op
Bencher.hashsetContains                         100  avgt    5     0.443 ±    0.005  us/op
Bencher.hashsetContains                        1000  avgt    5     4.510 ±    0.224  us/op
Bencher.hashsetContains                       10000  avgt    5    41.926 ±   31.500  us/op
Bencher.hashsetContains                      100000  avgt    5   905.241 ±   14.466  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.591 ±    0.051  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    39.004 ±   25.879  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   361.100 ±    2.845  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3649.443 ±   22.642  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.645 ±    0.025  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.639 ±    0.225  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   106.992 ±    5.494  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1422.584 ±   26.549  us/op
Bencher.ubfbContains                            100  avgt    5     0.751 ±    0.080  us/op
Bencher.ubfbContains                           1000  avgt    5     9.334 ±    0.103  us/op
Bencher.ubfbContains                          10000  avgt    5    92.129 ±    3.326  us/op
Bencher.ubfbContains                         100000  avgt    5   929.625 ±    5.623  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.050 ±    0.006  us/op
Bencher.ufbfAdd                                1000  avgt    5    10.077 ±    0.076  us/op
Bencher.ufbfAdd                               10000  avgt    5    91.528 ±    0.940  us/op
Bencher.ufbfAdd                              100000  avgt    5   919.694 ±    4.366  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.293 ±    0.019  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.966 ±    0.167  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.331 ±    1.504  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1369.042 ±   37.685  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.698 ±    0.008  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.729 ±    0.090  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   124.223 ±   10.223  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1642.108 ±   22.455  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.413 ±    0.014  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.762 ±    0.550  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   317.329 ±    3.126  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3232.890 ±   93.944  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.605 ±    0.035  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.341 ±    0.236  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5   100.091 ±    6.223  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1406.823 ±   37.060  us/op
Bencher.hashsetAdd                              100  avgt    5     0.919 ±    0.010  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.197 ±    2.026  us/op
Bencher.hashsetAdd                            10000  avgt    5    95.359 ±    4.232  us/op
Bencher.hashsetAdd                           100000  avgt    5  4874.210 ± 1714.404  us/op
Bencher.hashsetContains                         100  avgt    5     0.443 ±    0.008  us/op
Bencher.hashsetContains                        1000  avgt    5     4.494 ±    0.054  us/op
Bencher.hashsetContains                       10000  avgt    5    43.255 ±   31.461  us/op
Bencher.hashsetContains                      100000  avgt    5   906.361 ±   30.248  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.577 ±    0.018  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    36.611 ±    1.780  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   361.235 ±    5.941  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3652.439 ±   27.490  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.658 ±    0.073  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.480 ±    0.218  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   105.938 ±   11.208  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1438.241 ±   81.402  us/op
Bencher.ubfbContains                            100  avgt    5     0.790 ±    0.017  us/op
Bencher.ubfbContains                           1000  avgt    5     8.672 ±    0.059  us/op
Bencher.ubfbContains                          10000  avgt    5    75.012 ±    2.059  us/op
Bencher.ubfbContains                         100000  avgt    5   756.639 ±   14.120  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.027 ±    0.009  us/op
Bencher.ufbfAdd                                1000  avgt    5     9.997 ±    0.104  us/op
Bencher.ufbfAdd                               10000  avgt    5    93.335 ±    0.880  us/op
Bencher.ufbfAdd                              100000  avgt    5   943.710 ±    6.191  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.297 ±    0.023  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.928 ±    0.205  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.610 ±    2.399  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1309.895 ±   26.867  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.699 ±    0.017  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.773 ±    0.043  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   124.126 ±    5.436  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1602.312 ±  111.001  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.413 ±    0.007  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.684 ±    0.518  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   317.959 ±    1.622  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3238.274 ±   42.521  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.603 ±    0.026  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.276 ±    0.303  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    98.353 ±    6.707  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1403.142 ±   42.987  us/op
Bencher.hashsetAdd                              100  avgt    5     0.924 ±    0.037  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.291 ±    1.833  us/op
Bencher.hashsetAdd                            10000  avgt    5    95.084 ±    5.113  us/op
Bencher.hashsetAdd                           100000  avgt    5  4620.328 ± 1532.100  us/op
Bencher.hashsetContains                         100  avgt    5     0.442 ±    0.009  us/op
Bencher.hashsetContains                        1000  avgt    5     4.279 ±    0.038  us/op
Bencher.hashsetContains                       10000  avgt    5    43.478 ±   34.944  us/op
Bencher.hashsetContains                      100000  avgt    5   898.082 ±   14.673  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.589 ±    0.067  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    39.247 ±   26.254  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   361.040 ±    2.836  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3661.457 ±   98.285  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.648 ±    0.039  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.382 ±    0.169  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   104.785 ±    7.562  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1425.025 ±   51.273  us/op
Bencher.ubfbContains                            100  avgt    5     0.911 ±    0.016  us/op
Bencher.ubfbContains                           1000  avgt    5     8.750 ±    1.033  us/op
Bencher.ubfbContains                          10000  avgt    5    68.189 ±    0.943  us/op
Bencher.ubfbContains                         100000  avgt    5   688.887 ±    1.742  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.782 ±    0.058  us/op
Bencher.ufbfAdd                                1000  avgt    5    17.079 ±    0.347  us/op
Bencher.ufbfAdd                               10000  avgt    5   228.321 ±   18.426  us/op
Bencher.ufbfAdd                              100000  avgt    5  2771.778 ±   81.416  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.303 ±    0.023  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    13.000 ±    0.135  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.016 ±    1.128  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1365.179 ±   29.690  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.704 ±    0.034  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.719 ±    0.054  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5    82.618 ±    4.683  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1618.171 ±   48.522  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.427 ±    0.004  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.850 ±    0.060  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   320.440 ±    1.872  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3348.875 ±   28.369  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.611 ±    0.022  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.118 ±    0.344  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    97.641 ±    9.378  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1413.543 ±   61.167  us/op
Bencher.hashsetAdd                              100  avgt    5     0.922 ±    0.031  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.040 ±    1.070  us/op
Bencher.hashsetAdd                            10000  avgt    5    95.311 ±    3.795  us/op
Bencher.hashsetAdd                           100000  avgt    5  4921.896 ± 2055.394  us/op
Bencher.hashsetContains                         100  avgt    5     0.444 ±    0.004  us/op
Bencher.hashsetContains                        1000  avgt    5     4.307 ±    0.466  us/op
Bencher.hashsetContains                       10000  avgt    5    41.184 ±   27.930  us/op
Bencher.hashsetContains                      100000  avgt    5   902.888 ±   32.531  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.623 ±    0.026  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    39.115 ±   26.129  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   363.385 ±    8.205  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3835.816 ±  114.446  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.646 ±    0.030  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.587 ±    0.120  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   105.265 ±   10.485  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1421.865 ±   36.710  us/op
Bencher.ubfbContains                            100  avgt    5     0.957 ±    0.025  us/op
Bencher.ubfbContains                           1000  avgt    5     9.017 ±    1.443  us/op
Bencher.ubfbContains                          10000  avgt    5    69.697 ±    1.072  us/op
Bencher.ubfbContains                         100000  avgt    5   710.341 ±    8.783  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.899 ±    0.083  us/op
Bencher.ufbfAdd                                1000  avgt    5    18.196 ±    0.276  us/op
Bencher.ufbfAdd                               10000  avgt    5   228.204 ±   17.121  us/op
Bencher.ufbfAdd                              100000  avgt    5  2769.944 ±   69.266  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.303 ±    0.011  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.875 ±    0.201  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.886 ±    0.959  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1303.039 ±    8.998  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.695 ±    0.011  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.801 ±    0.060  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   134.323 ±   14.615  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1774.219 ±   26.681  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.413 ±    0.009  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.673 ±    0.519  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   318.812 ±    1.503  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3237.723 ±   46.675  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.611 ±    0.015  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.207 ±    0.218  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    99.971 ±    4.779  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1401.891 ±   39.349  us/op
Bencher.hashsetAdd                              100  avgt    5     0.923 ±    0.026  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.206 ±    1.466  us/op
Bencher.hashsetAdd                            10000  avgt    5    95.806 ±    3.806  us/op
Bencher.hashsetAdd                           100000  avgt    5  4772.244 ± 1166.716  us/op
Bencher.hashsetContains                         100  avgt    5     0.442 ±    0.009  us/op
Bencher.hashsetContains                        1000  avgt    5     4.458 ±    0.014  us/op
Bencher.hashsetContains                       10000  avgt    5    41.840 ±   28.564  us/op
Bencher.hashsetContains                      100000  avgt    5   891.665 ±   25.959  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.620 ±    0.021  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    39.047 ±   25.795  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   360.906 ±    1.807  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3687.153 ±  120.145  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.652 ±    0.049  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.445 ±    0.194  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   105.965 ±    8.471  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1419.914 ±   36.581  us/op
Bencher.ubfbContains                            100  avgt    5     0.957 ±    0.035  us/op
Bencher.ubfbContains                           1000  avgt    5     9.048 ±    1.800  us/op
Bencher.ubfbContains                          10000  avgt    5    70.565 ±    0.735  us/op
Bencher.ubfbContains                         100000  avgt    5   709.377 ±    8.103  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.897 ±    0.063  us/op
Bencher.ufbfAdd                                1000  avgt    5    18.099 ±    0.209  us/op
Bencher.ufbfAdd                               10000  avgt    5   227.355 ±   16.769  us/op
Bencher.ufbfAdd                              100000  avgt    5  2754.959 ±   48.814  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.303 ±    0.015  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.870 ±    0.138  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.882 ±    1.649  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1392.155 ±   31.389  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.726 ±    0.080  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.746 ±    0.076  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   113.553 ±   13.119  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1829.300 ±   51.887  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.414 ±    0.008  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    31.713 ±    0.236  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   322.013 ±   26.311  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3239.652 ±   58.094  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.602 ±    0.029  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.325 ±    0.131  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    96.558 ±    5.971  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1419.141 ±   62.275  us/op
Bencher.hashsetAdd                              100  avgt    5     0.925 ±    0.044  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.824 ±    1.887  us/op
Bencher.hashsetAdd                            10000  avgt    5    97.429 ±    7.726  us/op
Bencher.hashsetAdd                           100000  avgt    5  4733.489 ± 1054.951  us/op
Bencher.hashsetContains                         100  avgt    5     0.444 ±    0.006  us/op
Bencher.hashsetContains                        1000  avgt    5     4.314 ±    0.243  us/op
Bencher.hashsetContains                       10000  avgt    5    43.381 ±   31.942  us/op
Bencher.hashsetContains                      100000  avgt    5   976.671 ±   26.589  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.636 ±    0.027  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    36.574 ±    1.812  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   244.444 ±    1.381  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3676.479 ±  153.738  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.659 ±    0.058  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.628 ±    0.229  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   105.744 ±    8.750  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1441.269 ±   61.278  us/op
Bencher.ubfbContains                            100  avgt    5     1.006 ±    0.058  us/op
Bencher.ubfbContains                           1000  avgt    5     9.455 ±    2.058  us/op
Bencher.ubfbContains                          10000  avgt    5    71.864 ±    0.593  us/op
Bencher.ubfbContains                         100000  avgt    5   728.025 ±   15.953  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.898 ±    0.087  us/op
Bencher.ufbfAdd                                1000  avgt    5    18.163 ±    0.447  us/op
Bencher.ufbfAdd                               10000  avgt    5   232.386 ±    7.612  us/op
Bencher.ufbfAdd                              100000  avgt    5  2785.840 ±   74.213  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.305 ±    0.014  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.996 ±    0.292  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   129.001 ±    3.038  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1406.557 ±   80.959  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.708 ±    0.048  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.814 ±    0.065  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   130.919 ±   12.647  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1786.557 ±   57.937  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.412 ±    0.004  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.705 ±    0.315  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   318.474 ±    2.689  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3251.098 ±  103.367  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.617 ±    0.077  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.313 ±    0.114  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    96.608 ±    5.210  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1415.636 ±   46.104  us/op
Bencher.hashsetAdd                              100  avgt    5     0.931 ±    0.064  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.606 ±    1.155  us/op
Bencher.hashsetAdd                            10000  avgt    5    95.068 ±    6.859  us/op
Bencher.hashsetAdd                           100000  avgt    5  4779.048 ± 1150.150  us/op
Bencher.hashsetContains                         100  avgt    5     0.446 ±    0.014  us/op
Bencher.hashsetContains                        1000  avgt    5     4.430 ±    0.039  us/op
Bencher.hashsetContains                       10000  avgt    5    42.184 ±   30.442  us/op
Bencher.hashsetContains                      100000  avgt    5   912.541 ±   30.078  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.601 ±    0.076  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    39.192 ±   26.052  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   362.800 ±    7.556  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3688.682 ±   79.330  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.638 ±    0.073  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.444 ±    0.384  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   104.803 ±    4.458  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1442.416 ±   94.791  us/op
Bencher.ubfbContains                            100  avgt    5     1.001 ±    0.006  us/op
Bencher.ubfbContains                           1000  avgt    5     9.236 ±    0.170  us/op
Bencher.ubfbContains                          10000  avgt    5    68.127 ±    0.879  us/op
Bencher.ubfbContains                         100000  avgt    5   724.081 ±    7.410  us/op
Bencher.ufbfAdd                                 100  avgt    5     1.886 ±    0.086  us/op
Bencher.ufbfAdd                                1000  avgt    5    18.214 ±    0.442  us/op
Bencher.ufbfAdd                               10000  avgt    5   230.193 ±   11.154  us/op
Bencher.ufbfAdd                              100000  avgt    5  2782.779 ±   55.857  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.290 ±    0.003  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.882 ±    0.128  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   125.665 ±    1.301  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1399.651 ±   48.102  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.694 ±    0.018  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.804 ±    0.090  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   132.059 ±    7.568  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1827.307 ±   29.589  us/op
"""

"""
Benchmark                                   (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                     100  avgt    5     1.430 ±    0.012  us/op
Bencher.arrayBloomFilterAdd                    1000  avgt    5    23.844 ±    0.224  us/op
Bencher.arrayBloomFilterAdd                   10000  avgt    5   320.346 ±    1.661  us/op
Bencher.arrayBloomFilterAdd                  100000  avgt    5  3255.051 ±   30.251  us/op
Bencher.arrayBloomFilterContains                100  avgt    5     0.605 ±    0.029  us/op
Bencher.arrayBloomFilterContains               1000  avgt    5     6.140 ±    0.313  us/op
Bencher.arrayBloomFilterContains              10000  avgt    5    98.916 ±    5.812  us/op
Bencher.arrayBloomFilterContains             100000  avgt    5  1403.858 ±   18.179  us/op
Bencher.hashsetAdd                              100  avgt    5     0.919 ±    0.066  us/op
Bencher.hashsetAdd                             1000  avgt    5    14.375 ±    1.818  us/op
Bencher.hashsetAdd                            10000  avgt    5    96.296 ±    6.098  us/op
Bencher.hashsetAdd                           100000  avgt    5  4938.618 ± 1829.998  us/op
Bencher.hashsetContains                         100  avgt    5     0.443 ±    0.011  us/op
Bencher.hashsetContains                        1000  avgt    5     4.469 ±    0.191  us/op
Bencher.hashsetContains                       10000  avgt    5    48.733 ±   50.913  us/op
Bencher.hashsetContains                      100000  avgt    5   950.811 ±   81.204  us/op
Bencher.nativeBitSetBloomFilterAdd              100  avgt    5     3.828 ±    1.019  us/op
Bencher.nativeBitSetBloomFilterAdd             1000  avgt    5    36.968 ±    1.534  us/op
Bencher.nativeBitSetBloomFilterAdd            10000  avgt    5   362.323 ±    5.011  us/op
Bencher.nativeBitSetBloomFilterAdd           100000  avgt    5  3676.735 ±   74.763  us/op
Bencher.nativeBitSetBloomFilterContains         100  avgt    5     0.653 ±    0.017  us/op
Bencher.nativeBitSetBloomFilterContains        1000  avgt    5     6.577 ±    0.468  us/op
Bencher.nativeBitSetBloomFilterContains       10000  avgt    5   103.979 ±    9.947  us/op
Bencher.nativeBitSetBloomFilterContains      100000  avgt    5  1430.785 ±   75.672  us/op
Bencher.ubfbContains                            100  avgt    5     1.674 ±    0.023  us/op
Bencher.ubfbContains                           1000  avgt    5    16.687 ±    0.343  us/op
Bencher.ubfbContains                          10000  avgt    5   171.714 ±    4.497  us/op
Bencher.ubfbContains                         100000  avgt    5  1710.722 ±   44.749  us/op
Bencher.ufbfAdd                                 100  avgt    5     3.026 ±    0.262  us/op
Bencher.ufbfAdd                                1000  avgt    5    30.501 ±    1.015  us/op
Bencher.ufbfAdd                               10000  avgt    5   344.861 ±    2.224  us/op
Bencher.ufbfAdd                              100000  avgt    5  3800.150 ±   41.479  us/op
Bencher.vectorizedArrayBloomFilterAdd           100  avgt    5     1.223 ±    0.008  us/op
Bencher.vectorizedArrayBloomFilterAdd          1000  avgt    5    12.882 ±    0.205  us/op
Bencher.vectorizedArrayBloomFilterAdd         10000  avgt    5   128.585 ±    0.989  us/op
Bencher.vectorizedArrayBloomFilterAdd        100000  avgt    5  1388.470 ±   65.830  us/op
Bencher.vectorizedArrayBloomFilterContains      100  avgt    5     0.739 ±    0.024  us/op
Bencher.vectorizedArrayBloomFilterContains     1000  avgt    5     6.798 ±    0.072  us/op
Bencher.vectorizedArrayBloomFilterContains    10000  avgt    5   130.545 ±    6.378  us/op
Bencher.vectorizedArrayBloomFilterContains   100000  avgt    5  1844.238 ±   56.430  us/op
"""

"""
Benchmark                                  (items)  Mode  Cnt     Score      Error  Units
Bencher.arrayBloomFilterAdd                    100  avgt    5     1.431 ±    0.008  us/op
Bencher.arrayBloomFilterAdd                   1000  avgt    5    23.984 ±    0.149  us/op
Bencher.arrayBloomFilterAdd                  10000  avgt    5   189.583 ±    2.272  us/op
Bencher.arrayBloomFilterAdd                 100000  avgt    5  3286.465 ±  106.456  us/op
Bencher.arrayBloomFilterContains               100  avgt    5     0.606 ±    0.020  us/op
Bencher.arrayBloomFilterContains              1000  avgt    5     6.100 ±    0.166  us/op
Bencher.arrayBloomFilterContains             10000  avgt    5    98.611 ±    4.306  us/op
Bencher.arrayBloomFilterContains            100000  avgt    5  1405.461 ±   24.294  us/op
Bencher.hashsetAdd                             100  avgt    5     0.926 ±    0.053  us/op
Bencher.hashsetAdd                            1000  avgt    5    16.793 ±    2.951  us/op
Bencher.hashsetAdd                           10000  avgt    5   129.948 ±    5.879  us/op
Bencher.hashsetAdd                          100000  avgt    5  4830.531 ± 2005.408  us/op
Bencher.hashsetContains                        100  avgt    5     0.444 ±    0.003  us/op
Bencher.hashsetContains                       1000  avgt    5     4.375 ±    0.043  us/op
Bencher.hashsetContains                      10000  avgt    5    40.838 ±   27.501  us/op
Bencher.hashsetContains                     100000  avgt    5   916.189 ±   31.227  us/op
Bencher.nativeBitSetBloomFilterAdd             100  avgt    5     3.632 ±    0.032  us/op
Bencher.nativeBitSetBloomFilterAdd            1000  avgt    5    36.642 ±    1.852  us/op
Bencher.nativeBitSetBloomFilterAdd           10000  avgt    5   360.948 ±    2.471  us/op
Bencher.nativeBitSetBloomFilterAdd          100000  avgt    5  3663.179 ±   22.269  us/op
Bencher.nativeBitSetBloomFilterContains        100  avgt    5     0.665 ±    0.040  us/op
Bencher.nativeBitSetBloomFilterContains       1000  avgt    5     6.445 ±    0.333  us/op
Bencher.nativeBitSetBloomFilterContains      10000  avgt    5   104.584 ±    5.276  us/op
Bencher.nativeBitSetBloomFilterContains     100000  avgt    5  1422.798 ±   23.599  us/op
Bencher.vectorizedArrayBloomFilterAdd          100  avgt    5     1.300 ±    0.005  us/op
Bencher.vectorizedArrayBloomFilterAdd         1000  avgt    5    12.894 ±    0.252  us/op
Bencher.vectorizedArrayBloomFilterAdd        10000  avgt    5   128.853 ±    0.466  us/op
Bencher.vectorizedArrayBloomFilterAdd       100000  avgt    5  1393.928 ±   35.444  us/op
Bencher.vectoziedArrayBloomFilterContains      100  avgt    5     0.696 ±    0.013  us/op
Bencher.vectoziedArrayBloomFilterContains     1000  avgt    5     7.088 ±    0.094  us/op
Bencher.vectoziedArrayBloomFilterContains    10000  avgt    5   129.151 ±    7.230  us/op
Bencher.vectoziedArrayBloomFilterContains   100000  avgt    5  1822.875 ±   17.934  us/op
"""

"""
Benchmark                              (items)  Mode  Cnt      Score       Error  Units
Bencher.arrayBloomFilterAdd                100  avgt    5      1.488 ±     0.050  us/op
Bencher.arrayBloomFilterAdd               1000  avgt    5     24.732 ±     3.037  us/op
Bencher.arrayBloomFilterAdd              10000  avgt    5    329.489 ±     1.774  us/op
Bencher.arrayBloomFilterAdd             100000  avgt    5   3530.797 ±   177.013  us/op
Bencher.arrayBloomFilterAdd            1000000  avgt    5  74544.906 ± 36687.561  us/op
Bencher.hashsetAdd                         100  avgt    5      0.913 ±     0.084  us/op
Bencher.hashsetAdd                        1000  avgt    5     14.884 ±     2.528  us/op
Bencher.hashsetAdd                       10000  avgt    5    130.938 ±     5.155  us/op
Bencher.hashsetAdd                      100000  avgt    5   5202.726 ±   851.013  us/op
Bencher.hashsetAdd                     1000000  avgt    5  84358.900 ± 21503.731  us/op
Bencher.nativeBitSetBloomFilterAdd         100  avgt    5      3.690 ±     0.065  us/op
Bencher.nativeBitSetBloomFilterAdd        1000  avgt    5     39.521 ±    28.240  us/op
Bencher.nativeBitSetBloomFilterAdd       10000  avgt    5    391.273 ±     1.102  us/op
Bencher.nativeBitSetBloomFilterAdd      100000  avgt    5   4002.848 ±    35.404  us/op
Bencher.nativeBitSetBloomFilterAdd     1000000  avgt    5  76105.251 ± 24330.483  us/op
Bencher.vectorizedArrayBloomFilterAdd      100  avgt    5      1.347 ±     0.032  us/op
Bencher.vectorizedArrayBloomFilterAdd     1000  avgt    5     13.591 ±     1.116  us/op
Bencher.vectorizedArrayBloomFilterAdd    10000  avgt    5    149.081 ±     1.115  us/op
Bencher.vectorizedArrayBloomFilterAdd   100000  avgt    5   1564.842 ±    14.060  us/op
Bencher.vectorizedArrayBloomFilterAdd  1000000  avgt    5  34446.752 ± 13601.624  us/op
"""

"""
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
