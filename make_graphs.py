from matplotlib import pyplot as plt

data = """
Benchmark                              (size)  Mode  Cnt        Score        Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5        0.064 ±      0.042  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5        0.564 ±      0.346  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5        3.176 ±      0.042  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5        5.183 ±      0.062  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5       47.625 ±      4.910  us/op
Bencher.arrayBloomFilterContains           10  avgt    5        0.054 ±      0.001  us/op
Bencher.arrayBloomFilterContains          100  avgt    5        0.456 ±      0.405  us/op
Bencher.arrayBloomFilterContains          500  avgt    5        2.021 ±      0.042  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5        3.938 ±      0.115  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5       40.185 ±      0.862  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5        0.059 ±      0.001  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5        0.529 ±      0.025  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5        3.177 ±      0.055  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5        5.216 ±      0.185  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5       48.103 ±      0.967  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5        0.054 ±      0.001  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5        0.406 ±      0.007  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5        2.007 ±      0.034  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5        3.908 ±      0.075  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5       40.061 ±      1.404  us/op
Bencher.hashsetAdd                         10  avgt    5        0.094 ±      0.006  us/op
Bencher.hashsetAdd                        100  avgt    5        1.197 ±      0.172  us/op
Bencher.hashsetAdd                        500  avgt    5        7.161 ±      6.395  us/op
Bencher.hashsetAdd                       1000  avgt    5       12.259 ±     13.745  us/op
Bencher.hashsetAdd                      10000  avgt    5      115.256 ±      7.433  us/op
Bencher.hashsetAddAll                      10  avgt    5        0.104 ±      0.013  us/op
Bencher.hashsetAddAll                     100  avgt    5        1.182 ±      0.326  us/op
Bencher.hashsetAddAll                     500  avgt    5        6.843 ±      3.851  us/op
Bencher.hashsetAddAll                    1000  avgt    5       15.096 ±      8.857  us/op
Bencher.hashsetAddAll                   10000  avgt    5      142.138 ±      3.632  us/op
Bencher.hashsetContains                    10  avgt    5        0.090 ±      0.121  us/op
Bencher.hashsetContains                   100  avgt    5        0.275 ±      0.006  us/op
Bencher.hashsetContains                   500  avgt    5        1.300 ±      0.033  us/op
Bencher.hashsetContains                  1000  avgt    5        2.579 ±      0.079  us/op
Bencher.hashsetContains                 10000  avgt    5       30.759 ±      1.386  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5        3.361 ±      1.936  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      388.325 ±     75.170  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     9041.764 ±    392.984  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    37391.264 ±   3402.000  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  3864301.342 ±  52829.380  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5        3.018 ±      2.706  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      369.186 ±    102.875  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     9060.378 ±    319.723  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    36084.150 ±   2233.105  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  4856298.300 ± 253327.021  us/op
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

        print(name)
        print(measurements)

        plt.plot(xs, ys, label=name.split(".")[1])

    plt.yscale('linear')
    plt.ylabel("us/op")
    plt.xlabel("items")
    plt.legend()
    plt.show()
    plt.clf()
