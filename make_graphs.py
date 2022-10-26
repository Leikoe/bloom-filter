from matplotlib import pyplot as plt

data = """
Benchmark                              (items)  Mode  Cnt         Score         Error  Units
Bencher.arrayBloomFilterAdd                 10  avgt    5         5.784 ±       0.779  us/op
Bencher.arrayBloomFilterAdd                100  avgt    5        59.600 ±       3.088  us/op
Bencher.arrayBloomFilterAdd                500  avgt    5       279.078 ±      22.934  us/op
Bencher.arrayBloomFilterAdd               1000  avgt    5       549.384 ±      30.929  us/op
Bencher.arrayBloomFilterAdd              10000  avgt    5      6677.436 ±    1636.680  us/op
Bencher.arrayBloomFilterContains            10  avgt    5         2.753 ±       0.254  us/op
Bencher.arrayBloomFilterContains           100  avgt    5        28.300 ±       3.371  us/op
Bencher.arrayBloomFilterContains           500  avgt    5       139.031 ±      10.900  us/op
Bencher.arrayBloomFilterContains          1000  avgt    5       279.625 ±      17.594  us/op
Bencher.arrayBloomFilterContains         10000  avgt    5      3410.326 ±     531.984  us/op
Bencher.arrayListBloomFilterAdd             10  avgt    5         5.509 ±       0.379  us/op
Bencher.arrayListBloomFilterAdd            100  avgt    5        55.107 ±       4.912  us/op
Bencher.arrayListBloomFilterAdd            500  avgt    5       269.484 ±       7.182  us/op
Bencher.arrayListBloomFilterAdd           1000  avgt    5       535.784 ±      23.194  us/op
Bencher.arrayListBloomFilterAdd          10000  avgt    5      6328.349 ±    1307.420  us/op
Bencher.arrayListBloomFilterContains        10  avgt    5         2.753 ±       0.260  us/op
Bencher.arrayListBloomFilterContains       100  avgt    5        28.051 ±       6.065  us/op
Bencher.arrayListBloomFilterContains       500  avgt    5       139.117 ±      10.110  us/op
Bencher.arrayListBloomFilterContains      1000  avgt    5       280.583 ±       7.395  us/op
Bencher.arrayListBloomFilterContains     10000  avgt    5      3398.342 ±     507.111  us/op
Bencher.hashsetAdd                          10  avgt    5         0.094 ±       0.005  us/op
Bencher.hashsetAdd                         100  avgt    5         1.029 ±       0.377  us/op
Bencher.hashsetAdd                         500  avgt    5         6.594 ±       4.780  us/op
Bencher.hashsetAdd                        1000  avgt    5        15.730 ±       7.227  us/op
Bencher.hashsetAdd                       10000  avgt    5       122.770 ±      52.966  us/op
Bencher.hashsetAddAll                       10  avgt    5         0.107 ±       0.009  us/op
Bencher.hashsetAddAll                      100  avgt    5         1.186 ±       0.180  us/op
Bencher.hashsetAddAll                      500  avgt    5         6.279 ±       1.164  us/op
Bencher.hashsetAddAll                     1000  avgt    5        15.055 ±       5.825  us/op
Bencher.hashsetAddAll                    10000  avgt    5       148.572 ±       6.737  us/op
Bencher.hashsetContains                     10  avgt    5         0.067 ±       0.155  us/op
Bencher.hashsetContains                    100  avgt    5         0.324 ±       0.420  us/op
Bencher.hashsetContains                    500  avgt    5         1.307 ±       0.077  us/op
Bencher.hashsetContains                   1000  avgt    5         2.598 ±       0.103  us/op
Bencher.hashsetContains                  10000  avgt    5        29.036 ±       3.322  us/op
Bencher.linkedListBloomFilterAdd            10  avgt    5        25.781 ±      15.097  us/op
Bencher.linkedListBloomFilterAdd           100  avgt    5      2574.534 ±     575.815  us/op
Bencher.linkedListBloomFilterAdd           500  avgt    5     63560.509 ±    2858.530  us/op
Bencher.linkedListBloomFilterAdd          1000  avgt    5    262655.931 ±   19701.284  us/op
Bencher.linkedListBloomFilterAdd         10000  avgt    5  26902076.550 ±  940358.025  us/op
Bencher.linkedListBloomFilterContains       10  avgt    5        14.517 ±       9.318  us/op
Bencher.linkedListBloomFilterContains      100  avgt    5      1456.639 ±     170.669  us/op
Bencher.linkedListBloomFilterContains      500  avgt    5     37535.878 ±    3686.849  us/op
Bencher.linkedListBloomFilterContains     1000  avgt    5    152159.870 ±   11745.290  us/op
Bencher.linkedListBloomFilterContains    10000  avgt    5  21340301.892 ± 1000820.031  us/op
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
