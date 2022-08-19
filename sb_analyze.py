#! /usr/bin/python3
import re
import sys
import math
import numpy as np
import plotext as plt
import argparse

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
    parser = argparse.ArgumentParser(description='Analyze data according to standard sysbench output')
    parser.add_argument('sysbench_output', type=argparse.FileType('r', encoding='latin-1'),
                        help='the file path of sysbench output')
    parser.add_argument('--summary', '-S', choices=['all', 'tps', 'qps', 'lat', 'w', 'r', 'o'], nargs='+', default=['all'],
                        help='output summary info')
    # parser.add_argument('--csv', '-c', choices=['tps', 'qps', 'lat', 'w', 'r', 'o'], nargs='+', default=[],
    #                     help='output raw csv format data')
    parser.add_argument('--graph', '-g', choices=['all', 'tps', 'qps', 'lat', 'w', 'r', 'o'], nargs='+', default=['qps'],
                        help='output time series and data distribution graphs')
    parser.add_argument('--start', '-s', type=int, default=0,
                        help='strip data from (include)')
    parser.add_argument('--end', '-e', type=int, default=math.inf,
                        help='strip data to (not include)')
    parser.add_argument('--width', '-W', type=int, default=80,
                        help='width of graphs')
    parser.add_argument('--height', '-H', type=int, default=20,
                        help='height of graphs')
    args = parser.parse_args()

    f = args.sysbench_output
    sb_content = f.read()
    pattern = re.compile(r'\[ (\d+)s ] thds: \d+ tps: (\d+\.?\d*) qps: (\d+\.?\d*) \(r/w/o: (\d+\.?\d*)/(\d+\.?\d*)/(\d+\.?\d*)\) lat \(.*\): (\d+\.?\d*).*\n')

    # numpy version
    result = np.array(pattern.findall(sb_content), dtype='float')
    count = np.size(result, 0)
    print("Total Records:", count)
    if (args.start != 0 or args.end != math.inf):
        result = result[[x[0] >= args.start and x[0] < args.end for x in result]]
        count = np.size(result, 0)
        print("Records after strip:", count)


    if not count > 0:
        print("No rocord parsed, exit!")
        exit(0)

    time = result[:, 0]
    tps = result[:, 1]
    qps = result[:, 2]
    lat = result[:, 6]
    r = result[:, 3]
    w = result[:, 4]
    o = result[:, 5]

    choices = {
        'tps': tps,
        'qps': qps,
        'lat': lat,
        'r': r,
        'w': w,
        'o': w
    }

    # print summary
    for i in args.summary:
        if i == 'all':
            for [name, data] in choices.items():
                stat(data, name)
            break
        stat(choices[i], i)

    # print graphs
    plt_width = args.width
    plt_height = args.height

    for i in args.graph:
        if i == 'all':
            for [name, data] in choices.items():
                plt_sequential(time, data, name)
                plt_distribution(data, name)
                stat(data, name)
            break

        plt_sequential(time, choices[i], i)
        plt_distribution(choices[i], i)
