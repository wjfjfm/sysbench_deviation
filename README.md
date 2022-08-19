# Sysbench Output Deviation

## Usage:

```bash
$ python3 sb_analyze.py sample_sysbench_output.txt
```

the *sb_analyze_basic.py* is a simple implementation without any non-origin independence, which can be used by a basic python3 interpreter.

##Samples:

**Default Usage:**

```text
$ python3 sb_analyze.py sample_sysbench_output.txt
Total Records: 120
[tps] avg: 29.8     std_err(SE): 0.3     std_dev(SD): 3.0     max-min: 14.0
[qps] avg: 416.7    std_err(SE): 3.7     std_dev(SD): 41.0    max-min: 184.7
[lat] avg: 38.1     std_err(SE): 0.5     std_dev(SD): 5.0     max-min: 22.3
[ r ] avg: 416.7    std_err(SE): 3.7     std_dev(SD): 41.0    max-min: 184.7
[ w ] avg: 0.0      std_err(SE): 0.0     std_dev(SD): 0.0     max-min: 0.0
[ o ] avg: 0.0      std_err(SE): 0.0     std_dev(SD): 0.0     max-min: 0.0
                                   qps time series
     ┌─────────────────────────────────────────────────────────────────────────┐
461.1┤                                                 ▟  ▗                    │
     │                        ▗  ▖  ▖▖▗     ▗▌    ▖  ▖▗▘▌▄▜ ▖▗▚▄▌▖▞▖▗▚▗▄▄▚▗▀▟  │
     │                       ▄▜▞▞▝▚▀▝▚▘▀▄  ▄▜▚▖▗▀▀▚▄▞▝▀ ▜  █▝▘  ▝▝ ▐▞ ▘ ▝ ▘ ▝▄▌│
430.3┤                ▟ ▗▞▀▄▞ ▐▌         ▀▟   ▝▘           ▝        ▘        ▜▌│
     │               ▄▀▄▘      ▘                                              ▝│
399.5┤            ▗▜▞                                                          │
     │            ▌ ▘                                                          │
     │         ▞▀▜                                                             │
368.7┤        ▟                                                                │
     │      ▗▞▝                                                                │
337.9┤      ▌                                                                  │
     │    ▗▀▘                                                                  │
     │   ▞▘                                                                    │
307.2┤  ▞                                                                      │
     │▞▄▌                                                                      │
276.4┤▌                                                                        │
     └┬─────────────────┬─────────────────┬─────────────────┬─────────────────┬┘
      1.0             30.8              60.5              90.3            120.0
                             qps data distribution (avg=416.7 SD=41)
                 ┌─────────────────────────────────────────────────────────────┐
 [457.7,~) 1 100%┤█                                                            │
[437.2,~) 40  99%┤███████████████████████████████████████████████████          │
[416.7,~) 48  65%┤█████████████████████████████████████████████████████████████│
 [396.3,~) 9  25%┤███████████                                                  │
 [375.8,~) 5  18%┤██████                                                       │
 [355.3,~) 4  14%┤█████                                                        │
 [334.8,~) 2  10%┤██                                                           │
 [314.3,~) 5   9%┤██████                                                       │
 [293.9,~) 3   5%┤████                                                         │
 [273.4,~) 3   2%┤████                                                         │
                 └┬──────────────┬──────────────┬──────────────┬──────────────┬┘
                  1.0          12.8           24.5           36.3          48.0

```

**Strip data:**

some time the data in front is called "warm up", we can jump over it

```text
$ python3 sb_analyze.py sample_sysbench_output.txt --start 51
Total Records: 120
Records after strip: 70
[tps] avg: 31.3     std_err(SE): 0.1     std_dev(SD): 0.7     max-min: 3.0
[qps] avg: 438.2    std_err(SE): 1.1     std_dev(SD): 8.9     max-min: 46.0
[lat] avg: 35.5     std_err(SE): 0.1     std_dev(SD): 1.3     max-min: 6.4
[ r ] avg: 438.2    std_err(SE): 1.1     std_dev(SD): 8.9     max-min: 46.0
[ w ] avg: 0.0      std_err(SE): 0.0     std_dev(SD): 0.0     max-min: 0.0
[ o ] avg: 0.0      std_err(SE): 0.0     std_dev(SD): 0.0     max-min: 0.0
                                   qps time series
     ┌─────────────────────────────────────────────────────────────────────────┐
461.1┤                                ▟                                        │
     │                                █                                        │
     │                                ▌▌    ▖                                  │
453.4┤                                ▌▚   ▞▌     ▖  ▗                   ▖     │
     │              ▗                ▐ ▐  ▗▘▌    ▐▌ ▗▜       ▗       ▖  ▞▚ ▗   │
445.7┤              █                ▐ ▐ ▞▘ ▚    ▞▚ ▞▐   ▞▜  ▛▖  ▖ ▖▐▚ ▐  ▚▜   │
     │▗▌ ▖          █        ▖    ▗  ▐ ▝▖▌  ▐  ▖ ▌▐▗▘ ▌  ▌▐  ▌▐ ▐▝▞▚▞ ▌▞   ▐   │
438.1┤▞▌▐▚ ▟        ▌▌      ▐▌   ▞▀▖ ▞  ▙▘  ▐ ▐▌▐  ▘  ▌▟▐  ▌ ▌ ▚▌  ▝▌ ▝▌   ▐ ▗ │
     │▘▐▞ ▀▝▖     ▗▐ ▌     ▖▌▐  ▗▘ ▚▟   █   ▝▖▐▐▌     ▝ ▜  ▚▗▘  ▘          ▐ █ │
     │ ▐▌   ▌     █▐ ▐   ▄▀▝▘▝▖ ▞       ▝    ▌▞ ▘          ▐▐              ▐ █ │
430.4┤  ▘   ▝▄   ▐ █ ▐ ▖▞     ▝▀             ▐▌             █               ▌█ │
     │       ▐   ▌ ▝  ▀▝▘                    ▝▌             ▜               ▙▀▖│
422.7┤        ▌  ▌                                                          █ ▌│
     │        ▐ ▐                                                           █ ▌│
     │         ▚▐                                                           █ ▌│
415.1┤          ▀                                                           ▝ ▚│
     └┬─────────────────┬─────────────────┬─────────────────┬─────────────────┬┘
      51.0            68.3              85.5              102.8           120.0
                             qps data distribution (avg=438.2 SD=9)
                 ┌─────────────────────────────────────────────────────────────┐
 [460.5,~) 1 100%┤█████                                                        │
 [456.0,~) 0  98%┤                                                             │
 [451.6,~) 1  98%┤█████                                                        │
 [447.1,~) 9  97%┤███████████████████████████████████                          │
[442.6,~) 11  84%┤██████████████████████████████████████████                   │
[438.2,~) 14  68%┤██████████████████████████████████████████████████████       │
[433.7,~) 16  48%┤█████████████████████████████████████████████████████████████│
 [429.3,~) 8  25%┤███████████████████████████████                              │
 [424.8,~) 5  14%┤████████████████████                                         │
 [420.3,~) 1   7%┤█████                                                        │
 [415.9,~) 3   5%┤████████████                                                 │
 [411.4,~) 1   1%┤█████                                                        │
                 └┬──────────────┬──────────────┬──────────────┬──────────────┬┘
                  0.0           4.0            8.0           12.0          16.0

```

**Other parameters:**

```text
$ python3 sb_analyze.py -h

positional arguments:
  sysbench_output       the file path of sysbench output

optional arguments:
  -h, --help            show this help message and exit
  --summary {all,tps,qps,lat,w,r,o} [{all,tps,qps,lat,w,r,o} ...], -S {all,tp
                        output summary info
  --graph {all,tps,qps,lat,w,r,o} [{all,tps,qps,lat,w,r,o} ...], -g {all,tps,
                        output time series and data distribution graphs
  --start START, -s START
                        strip data from (include)
  --end END, -e END     strip data to (not include)
  --width WIDTH, -W WIDTH
                        width of graphs
  --height HEIGHT, -H HEIGHT
                        height of graphs
```
