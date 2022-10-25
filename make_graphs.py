from matplotlib import pyplot as plt

data = """
Benchmark                               (size)  Mode  Cnt      Score      Error  Units
Bencher.arrayBloomFilterAdd             250000  avgt    5     13.699 ±    0.786  us/op
Bencher.arrayBloomFilterAdd             500000  avgt    5     14.826 ±    1.530  us/op
Bencher.arrayBloomFilterAdd             750000  avgt    5     13.546 ±    0.621  us/op
Bencher.arrayBloomFilterAdd            1000000  avgt    5     13.657 ±    0.188  us/op
Bencher.arrayBloomFilterAdd            1250000  avgt    5     14.294 ±    5.366  us/op
Bencher.arrayBloomFilterAdd            1500000  avgt    5     14.626 ±    2.042  us/op
Bencher.arrayBloomFilterAdd            1750000  avgt    5     14.833 ±    0.858  us/op
Bencher.arrayBloomFilterAdd            2000000  avgt    5     15.027 ±    1.379  us/op
Bencher.arrayBloomFilterAdd            2250000  avgt    5     15.298 ±    1.695  us/op
Bencher.arrayBloomFilterAdd            2500000  avgt    5     16.068 ±    2.746  us/op
Bencher.arrayBloomFilterAdd            2750000  avgt    5     16.845 ±    2.876  us/op
Bencher.arrayBloomFilterAdd            3000000  avgt    5     15.410 ±    3.654  us/op
Bencher.arrayBloomFilterContains        250000  avgt    5     13.343 ±    0.693  us/op
Bencher.arrayBloomFilterContains        500000  avgt    5     13.921 ±    0.519  us/op
Bencher.arrayBloomFilterContains        750000  avgt    5     13.144 ±    0.571  us/op
Bencher.arrayBloomFilterContains       1000000  avgt    5     13.398 ±    1.069  us/op
Bencher.arrayBloomFilterContains       1250000  avgt    5     13.584 ±    2.580  us/op
Bencher.arrayBloomFilterContains       1500000  avgt    5     14.022 ±    0.948  us/op
Bencher.arrayBloomFilterContains       1750000  avgt    5     14.400 ±    1.740  us/op
Bencher.arrayBloomFilterContains       2000000  avgt    5     14.787 ±    2.009  us/op
Bencher.arrayBloomFilterContains       2250000  avgt    5     15.418 ±    1.280  us/op
Bencher.arrayBloomFilterContains       2500000  avgt    5     16.259 ±    3.471  us/op
Bencher.arrayBloomFilterContains       2750000  avgt    5     15.774 ±    1.238  us/op
Bencher.arrayBloomFilterContains       3000000  avgt    5     15.079 ±    5.248  us/op
Bencher.arrayListBloomFilterAdd         250000  avgt    5     13.138 ±    0.333  us/op
Bencher.arrayListBloomFilterAdd         500000  avgt    5     13.862 ±    0.420  us/op
Bencher.arrayListBloomFilterAdd         750000  avgt    5     13.022 ±    0.564  us/op
Bencher.arrayListBloomFilterAdd        1000000  avgt    5     13.350 ±    0.552  us/op
Bencher.arrayListBloomFilterAdd        1250000  avgt    5     13.927 ±    1.319  us/op
Bencher.arrayListBloomFilterAdd        1500000  avgt    5     14.183 ±    0.622  us/op
Bencher.arrayListBloomFilterAdd        1750000  avgt    5     14.042 ±    3.464  us/op
Bencher.arrayListBloomFilterAdd        2000000  avgt    5     15.520 ±    1.497  us/op
Bencher.arrayListBloomFilterAdd        2250000  avgt    5     15.719 ±    1.164  us/op
Bencher.arrayListBloomFilterAdd        2500000  avgt    5     16.127 ±    2.855  us/op
Bencher.arrayListBloomFilterAdd        2750000  avgt    5     16.172 ±    2.560  us/op
Bencher.arrayListBloomFilterAdd        3000000  avgt    5     15.670 ±    3.913  us/op
Bencher.arrayListBloomFilterContains    250000  avgt    5     13.266 ±    1.159  us/op
Bencher.arrayListBloomFilterContains    500000  avgt    5     13.912 ±    0.461  us/op
Bencher.arrayListBloomFilterContains    750000  avgt    5     13.301 ±    0.321  us/op
Bencher.arrayListBloomFilterContains   1000000  avgt    5     13.269 ±    1.302  us/op
Bencher.arrayListBloomFilterContains   1250000  avgt    5     14.174 ±    2.259  us/op
Bencher.arrayListBloomFilterContains   1500000  avgt    5     14.380 ±    2.034  us/op
Bencher.arrayListBloomFilterContains   1750000  avgt    5     13.573 ±    1.829  us/op
Bencher.arrayListBloomFilterContains   2000000  avgt    5     14.904 ±    1.877  us/op
Bencher.arrayListBloomFilterContains   2250000  avgt    5     15.873 ±    1.904  us/op
Bencher.arrayListBloomFilterContains   2500000  avgt    5     16.876 ±    5.089  us/op
Bencher.arrayListBloomFilterContains   2750000  avgt    5     16.591 ±    2.419  us/op
Bencher.arrayListBloomFilterContains   3000000  avgt    5     15.685 ±    3.428  us/op
Bencher.linkedListBloomFilterAdd        250000  avgt    5   1992.334 ±   49.067  us/op
Bencher.linkedListBloomFilterAdd        500000  avgt    5   9707.836 ±  757.221  us/op
Bencher.linkedListBloomFilterAdd        750000  avgt    5   8970.181 ±  317.401  us/op
Bencher.linkedListBloomFilterAdd       1000000  avgt    5  11365.503 ± 1467.262  us/op
Bencher.linkedListBloomFilterAdd       1250000  avgt    5  10488.765 ±  137.480  us/op
Bencher.linkedListBloomFilterAdd       1500000  avgt    5  30725.955 ± 1072.536  us/op
Bencher.linkedListBloomFilterAdd       1750000  avgt    5  21508.477 ± 1093.608  us/op
Bencher.linkedListBloomFilterAdd       2000000  avgt    5  36747.598 ± 3914.920  us/op
Bencher.linkedListBloomFilterAdd       2250000  avgt    5  31050.951 ± 2265.950  us/op
Bencher.linkedListBloomFilterAdd       2500000  avgt    5  15410.391 ±  496.380  us/op
Bencher.linkedListBloomFilterAdd       2750000  avgt    5  39187.647 ± 3670.840  us/op
Bencher.linkedListBloomFilterAdd       3000000  avgt    5  56082.043 ± 1058.640  us/op
Bencher.linkedListBloomFilterContains   250000  avgt    5   1975.032 ±   56.787  us/op
Bencher.linkedListBloomFilterContains   500000  avgt    5   9873.772 ±  923.115  us/op
Bencher.linkedListBloomFilterContains   750000  avgt    5   8970.849 ±  223.779  us/op
Bencher.linkedListBloomFilterContains  1000000  avgt    5  11361.738 ±  875.870  us/op
Bencher.linkedListBloomFilterContains  1250000  avgt    5  10482.704 ±  125.823  us/op
Bencher.linkedListBloomFilterContains  1500000  avgt    5  31124.656 ± 1782.835  us/op
Bencher.linkedListBloomFilterContains  1750000  avgt    5  21320.114 ±  596.002  us/op
Bencher.linkedListBloomFilterContains  2000000  avgt    5  36981.151 ±  864.567  us/op
Bencher.linkedListBloomFilterContains  2250000  avgt    5  31117.760 ±  396.180  us/op
Bencher.linkedListBloomFilterContains  2500000  avgt    5  15342.860 ± 1473.610  us/op
Bencher.linkedListBloomFilterContains  2750000  avgt    5  40070.313 ± 2826.518  us/op
Bencher.linkedListBloomFilterContains  3000000  avgt    5  56201.108 ±  863.197  us/op
"""

# split data into lines and remove empty lines + remove header line
data = list(filter(lambda line: len(line) > 0, data.splitlines()))[1:]

def unique(l: []) -> []:
   return list({ *l })

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

# keep only name, size, time

results = list(results)

# get unique sample sizes in vanilla python (no numpy :pepehands:)
sizes = unique(list(map(lambda line: line.split()[1], data)))
sizes.sort()

for op_group in results:
    # get the list of names
    names = unique(list(map(lambda x: x[0], op_group)))
    names.sort()
    for name in names:
        measurements = list(
            map(
                lambda x: (float(x[1]), float(x[2])),
                filter(lambda x: x[0] == name, op_group)
            )
        )
        # unzip measurements
        xs, ys = zip(*measurements)

        print(name)
        print(measurements)

        plt.plot(xs, ys, label=name.split(".")[1])

    plt.yscale('log')
    plt.ylabel("us/op")
    plt.xlabel("size")
    plt.legend()
    plt.show()
    plt.clf()

print(sizes)
