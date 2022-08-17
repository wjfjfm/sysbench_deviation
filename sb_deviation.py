import re
import sys
from statistics import mean, stdev
# import numpy as np

if len(sys.argv) != 2:
     print("Usage: python3 {} sysbench_ouput.txt".format(sys.argv[0]))
     exit(0)

f = open(sys.argv[1], "r")
sb_content = f.read()
pattern = re.compile(r'\[.*] thds: \d+ tps: (\d+\.?\d*) qps: (\d+\.?\d*) \(r/w/o: (\d+\.?\d*)/(\d+\.?\d*)/(\d+\.?\d*)\) lat \(.*\): (\d+\.?\d*).*\n')

## numpy version
# result = np.array(pattern.findall(sb_content), dtype='float')

# def stat(nums, name):
#     print("[{:^3}] avg: {:<10.2f}std_deviation: {:<10.2f}max-min: {:<10.2f}".format(
#         name, np.average(nums), np.std(nums), np.max(nums) - np.min(nums)));

# print("Total Records:", np.size(result, 0))
# stat(result[:, 0], "tps")
# stat(result[:, 1], "qps")
# stat(result[:, 5], "lat")
# stat(result[:, 2], "r")
# stat(result[:, 3], "w")
# stat(result[:, 4], "o")

# statistics version
result = pattern.findall(sb_content)

def stat(nums, name):
    print("[{:^3}] avg: {:<10.2f}std_deviation: {:<10.2f}max-min: {:<10.2f}".format(
        name, mean(nums), stdev(nums), max(nums) - min(nums)));

print("Total Records:", len(result))
stat([float(x[0]) for x in result] , "tps")
stat([float(x[1]) for x in result], "qps")
stat([float(x[5]) for x in result], "lat")
stat([float(x[2]) for x in result], "r")
stat([float(x[3]) for x in result], "w")
stat([float(x[4]) for x in result], "o")
