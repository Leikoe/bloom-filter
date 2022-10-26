from matplotlib import pyplot as plt

data = """
Benchmark                              (size)  Mode  Cnt         Score         Error  Units
Bencher.arrayBloomFilterAdd                10  avgt    5        19.393 ±       1.276  us/op
Bencher.arrayBloomFilterAdd               100  avgt    5       195.411 ±      19.231  us/op
Bencher.arrayBloomFilterAdd               500  avgt    5       998.004 ±     125.544  us/op
Bencher.arrayBloomFilterAdd              1000  avgt    5      2186.658 ±     342.090  us/op
Bencher.arrayBloomFilterAdd             10000  avgt    5     28301.044 ±    9757.325  us/op
Bencher.arrayBloomFilterContains           10  avgt    5        19.106 ±       1.813  us/op
Bencher.arrayBloomFilterContains          100  avgt    5       191.797 ±       5.128  us/op
Bencher.arrayBloomFilterContains          500  avgt    5       930.292 ±      57.394  us/op
Bencher.arrayBloomFilterContains         1000  avgt    5      2070.954 ±      68.571  us/op
Bencher.arrayBloomFilterContains        10000  avgt    5     25951.536 ±    2057.514  us/op
Bencher.arrayListBloomFilterAdd            10  avgt    5        19.146 ±       1.767  us/op
Bencher.arrayListBloomFilterAdd           100  avgt    5       195.339 ±       8.278  us/op
Bencher.arrayListBloomFilterAdd           500  avgt    5       945.478 ±      19.150  us/op
Bencher.arrayListBloomFilterAdd          1000  avgt    5      2076.728 ±     190.687  us/op
Bencher.arrayListBloomFilterAdd         10000  avgt    5     25951.288 ±    2329.716  us/op
Bencher.arrayListBloomFilterContains       10  avgt    5        19.089 ±       1.036  us/op
Bencher.arrayListBloomFilterContains      100  avgt    5       190.544 ±       7.749  us/op
Bencher.arrayListBloomFilterContains      500  avgt    5       935.136 ±      51.612  us/op
Bencher.arrayListBloomFilterContains     1000  avgt    5      2062.579 ±     144.303  us/op
Bencher.arrayListBloomFilterContains    10000  avgt    5     25631.709 ±    2104.797  us/op
Bencher.hashsetAdd                         10  avgt    5         0.094 ±       0.005  us/op
Bencher.hashsetAdd                        100  avgt    5         1.133 ±       0.446  us/op
Bencher.hashsetAdd                        500  avgt    5         4.778 ±       0.363  us/op
Bencher.hashsetAdd                       1000  avgt    5        15.882 ±       5.188  us/op
Bencher.hashsetAdd                      10000  avgt    5       140.177 ±      55.370  us/op
Bencher.hashsetAddAll                      10  avgt    5         0.107 ±       0.009  us/op
Bencher.hashsetAddAll                     100  avgt    5         1.202 ±       0.105  us/op
Bencher.hashsetAddAll                     500  avgt    5         6.314 ±       0.838  us/op
Bencher.hashsetAddAll                    1000  avgt    5        15.800 ±       4.259  us/op
Bencher.hashsetAddAll                   10000  avgt    5       170.505 ±      12.221  us/op
Bencher.hashsetContains                    10  avgt    5         0.080 ±       0.150  us/op
Bencher.hashsetContains                   100  avgt    5         0.275 ±       0.003  us/op
Bencher.hashsetContains                   500  avgt    5         1.323 ±       0.081  us/op
Bencher.hashsetContains                  1000  avgt    5         2.611 ±       0.073  us/op
Bencher.hashsetContains                 10000  avgt    5        31.988 ±       6.845  us/op
Bencher.linkedListBloomFilterAdd           10  avgt    5        30.240 ±       2.857  us/op
Bencher.linkedListBloomFilterAdd          100  avgt    5      1566.490 ±      36.734  us/op
Bencher.linkedListBloomFilterAdd          500  avgt    5     40697.519 ±    1589.577  us/op
Bencher.linkedListBloomFilterAdd         1000  avgt    5    136463.979 ±    8495.685  us/op
Bencher.linkedListBloomFilterAdd        10000  avgt    5  15913143.367 ± 1234166.315  us/op
Bencher.linkedListBloomFilterContains      10  avgt    5        32.203 ±       6.609  us/op
Bencher.linkedListBloomFilterContains     100  avgt    5      1582.639 ±     145.315  us/op
Bencher.linkedListBloomFilterContains     500  avgt    5     46245.760 ±    2155.583  us/op
Bencher.linkedListBloomFilterContains    1000  avgt    5    152835.019 ±    3555.836  us/op
Bencher.linkedListBloomFilterContains   10000  avgt    5  17680408.250 ± 1497115.915  us/op
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
