from matplotlib import pyplot as plt

data = """
Benchmark                              (items)  Mode  Cnt         Score         Error  Units
Bencher.arrayBloomFilterAdd                 10  avgt    5         0.183 ±       0.007  us/op
Bencher.arrayBloomFilterAdd                100  avgt    5         1.631 ±       0.083  us/op
Bencher.arrayBloomFilterAdd                500  avgt    5        10.853 ±       0.181  us/op
Bencher.arrayBloomFilterAdd               1000  avgt    5        27.121 ±       0.755  us/op
Bencher.arrayBloomFilterAdd              10000  avgt    5       279.876 ±      10.158  us/op
Bencher.arrayBloomFilterContains            10  avgt    5         0.181 ±       0.034  us/op
Bencher.arrayBloomFilterContains           100  avgt    5         1.169 ±       0.042  us/op
Bencher.arrayBloomFilterContains           500  avgt    5         5.632 ±       0.181  us/op
Bencher.arrayBloomFilterContains          1000  avgt    5        15.805 ±       7.365  us/op
Bencher.arrayBloomFilterContains         10000  avgt    5       137.899 ±       6.420  us/op
Bencher.arrayListBloomFilterAdd             10  avgt    5         0.180 ±       0.005  us/op
Bencher.arrayListBloomFilterAdd            100  avgt    5         1.617 ±       0.029  us/op
Bencher.arrayListBloomFilterAdd            500  avgt    5        10.962 ±       0.923  us/op
Bencher.arrayListBloomFilterAdd           1000  avgt    5        25.223 ±      10.083  us/op
Bencher.arrayListBloomFilterAdd          10000  avgt    5       273.327 ±      75.153  us/op
Bencher.arrayListBloomFilterContains        10  avgt    5         0.184 ±       0.033  us/op
Bencher.arrayListBloomFilterContains       100  avgt    5         1.159 ±       0.045  us/op
Bencher.arrayListBloomFilterContains       500  avgt    5         5.650 ±       0.129  us/op
Bencher.arrayListBloomFilterContains      1000  avgt    5        13.981 ±       9.408  us/op
Bencher.arrayListBloomFilterContains     10000  avgt    5       136.217 ±      12.218  us/op
Bencher.hashsetAdd                          10  avgt    5         0.093 ±       0.007  us/op
Bencher.hashsetAdd                         100  avgt    5         1.005 ±       0.076  us/op
Bencher.hashsetAdd                         500  avgt    5         4.678 ±       0.046  us/op
Bencher.hashsetAdd                        1000  avgt    5         9.851 ±       0.735  us/op
Bencher.hashsetAdd                       10000  avgt    5       122.693 ±      59.733  us/op
Bencher.hashsetAddAll                       10  avgt    5         0.104 ±       0.010  us/op
Bencher.hashsetAddAll                      100  avgt    5         1.184 ±       0.083  us/op
Bencher.hashsetAddAll                      500  avgt    5         6.668 ±       3.157  us/op
Bencher.hashsetAddAll                     1000  avgt    5        15.859 ±       5.943  us/op
Bencher.hashsetAddAll                    10000  avgt    5       145.371 ±      10.331  us/op
Bencher.hashsetContains                     10  avgt    5         0.090 ±       0.119  us/op
Bencher.hashsetContains                    100  avgt    5         0.275 ±       0.011  us/op
Bencher.hashsetContains                    500  avgt    5         1.303 ±       0.062  us/op
Bencher.hashsetContains                   1000  avgt    5         2.578 ±       0.042  us/op
Bencher.hashsetContains                  10000  avgt    5        31.874 ±       5.354  us/op
Bencher.linkedListBloomFilterAdd            10  avgt    5        21.271 ±      17.147  us/op
Bencher.linkedListBloomFilterAdd           100  avgt    5      2646.032 ±     632.213  us/op
Bencher.linkedListBloomFilterAdd           500  avgt    5     63637.660 ±    5544.081  us/op
Bencher.linkedListBloomFilterAdd          1000  avgt    5    254095.704 ±   20136.899  us/op
Bencher.linkedListBloomFilterAdd         10000  avgt    5  26894370.658 ± 1236313.584  us/op
Bencher.linkedListBloomFilterContains       10  avgt    5        13.002 ±      14.071  us/op
Bencher.linkedListBloomFilterContains      100  avgt    5      1461.591 ±     461.716  us/op
Bencher.linkedListBloomFilterContains      500  avgt    5     36740.733 ±    3195.509  us/op
Bencher.linkedListBloomFilterContains     1000  avgt    5    145115.033 ±   17593.301  us/op
Bencher.linkedListBloomFilterContains    10000  avgt    5  18581175.733 ±  506765.637  us/op
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
