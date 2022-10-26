from matplotlib import pyplot as plt

data = """
Benchmark                              (size)  Mode  Cnt        Score       Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5       47.977 ±    32.386  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5      426.493 ±   149.279  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5     2177.976 ±   341.725  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5     3985.485 ±  1706.349  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5    50096.823 ± 70357.494  us/op
Bencher.arrayBloomFilterContains           10  avgt    5       34.065 ±     8.746  us/op
Bencher.arrayBloomFilterContains          100  avgt    5      303.439 ±    62.573  us/op
Bencher.arrayBloomFilterContains          500  avgt    5     1487.027 ±   235.499  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5     2947.329 ±   301.983  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5    37725.893 ±  7801.107  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5       44.037 ±    16.884  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5      355.929 ±    87.702  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5     1683.658 ±   140.102  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5     3351.390 ±   554.693  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5    41932.675 ±  4177.664  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5       34.939 ±     8.393  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5      303.591 ±    85.742  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5     1540.620 ±   294.306  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5     2967.951 ±   399.980  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5    37475.414 ±  1798.806  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5       43.688 ±     7.960  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      754.609 ±   226.819  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     7395.928 ±   377.659  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    21974.058 ±  1008.987  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  1784691.377 ± 64776.823  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5       34.413 ±     6.618  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      501.623 ±    62.601  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     6854.397 ±   948.211  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    20343.517 ±   766.955  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  1783718.189 ± 51574.452  us/op
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
