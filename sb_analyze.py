import re
import sys
import math
import numpy as np
import plotext as plt

def stat(nums, name):
    print("[{:^3}] avg: {:<9.1f}std_err(SE): {:<8.1f}std_dev(SD): {:<8.1f}max-min: {:<8.1f}".format(
        name, np.average(nums), np.std(nums) / np.sqrt(count), np.std(nums), np.max(nums) - np.min(nums)));

def plt_sequential(time, nums, name):
    plt.clf()
    plt.clc()
    plt.plot_size(plt_width, int(plt_width / 4))
    plt.plot(time, nums)
    plt.title("{} time series".format(name))
    plt.show()

def plt_distribution(nums, name):
    plt.clf()
    plt.clc()

    pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
    percentages = [14, 36, 11, 8, 7, 4]

    avg = np.average(nums)
    SD = np.std(nums)
    if SD > 0 :
        jump = 0.5 * SD
    else:
        jump = 1

    sorted = np.sort(np.array(nums, copy=True))
    min_num = sorted[0]
    max_num = sorted[-1]
    total = len(sorted)
    spot = avg
    while (spot > min_num):
        spot -= jump
    count = 0
    p = 0
    text = []
    data = []
    while(spot <= max_num):
        next_spot = spot + jump
        while(p < total and sorted[p] < next_spot):
            p += 1
            count += 1
        data.append(count)
        text.append("[{:.1f},~) {} {:3d}%".format(spot, count, int(p * 100 / total)))
        spot = next_spot
        count = 0

    plt.bar(text, data, orientation = "h", width=0)
    plt.title("{} data distribution (avg={:.1f} SD={:.0f})".format(name, avg, SD ))
    plt.plotsize(plt_width, len(data) + 4) # 4 = (1 for x numerical ticks + 2 for x axes + 1 for title)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
         print("Usage: python3 {} sysbench_ouput.txt".format(sys.argv[0]))
         exit(0)

    f = open(sys.argv[1], "r")
    sb_content = f.read()
    pattern = re.compile(r'\[ (\d+)s ] thds: \d+ tps: (\d+\.?\d*) qps: (\d+\.?\d*) \(r/w/o: (\d+\.?\d*)/(\d+\.?\d*)/(\d+\.?\d*)\) lat \(.*\): (\d+\.?\d*).*\n')

    # numpy version
    result = np.array(pattern.findall(sb_content), dtype='float')
    count = np.size(result, 0)
    if not count > 0:
        exit(0)

    time = result[:, 0]
    tps = result[:, 1]
    qps = result[:, 2]
    lat = result[:, 6]
    r = result[:, 3]
    w = result[:, 4]
    o = result[:, 5]

    print("Total Records:", count)
    stat(tps, "tps")
    stat(qps, "qps")
    stat(lat, "lat")
    stat(r, "r")
    stat(w, "w")
    stat(o, "o")

    plt_width = 80
    plt_height = 20

    plt_sequential(time, qps, "qps")
    plt_distribution(qps, "qps")
