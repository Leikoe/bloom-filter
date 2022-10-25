from matplotlib import pyplot as plt

data = """
Benchmark                              (size)  Mode  Cnt        Score       Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5       45.328 ±    18.184  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5      452.735 ±   248.837  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5     2039.488 ±  1012.244  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5     3940.519 ±  1103.096  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5    32281.996 ±  7633.452  us/op
Bencher.arrayBloomFilterContains           10  avgt    5       33.034 ±     8.140  us/op
Bencher.arrayBloomFilterContains          100  avgt    5      344.485 ±    97.904  us/op
Bencher.arrayBloomFilterContains          500  avgt    5     1704.259 ±   483.596  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5     3424.717 ±  1371.490  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5    28616.340 ±  6790.772  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5       40.697 ±    12.865  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5      407.221 ±   181.610  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5     1953.271 ±   280.185  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5     4008.855 ±  1035.644  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5    32253.788 ±  6967.791  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5       33.782 ±    13.063  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5      388.249 ±   238.152  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5     1927.403 ±  2146.600  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5     3728.762 ±   735.553  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5    30049.579 ±  3353.363  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5       46.225 ±    18.639  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      710.134 ±    96.583  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     8074.379 ±  1286.764  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    23541.855 ±  1232.630  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  1820743.146 ± 88833.208  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5       35.841 ±     7.286  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      536.106 ±   259.484  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     7244.282 ±  1108.602  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    21896.456 ±  2621.899  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  1813582.583 ± 66060.102  us/op
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
        if "linked" in name:
            continue

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
    plt.xlabel("size")
    plt.legend()
    plt.show()
    plt.clf()

print(sizes)
