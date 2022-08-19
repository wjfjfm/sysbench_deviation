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
                                   tps time series
    ┌──────────────────────────────────────────────────────────────────────────┐
33.0┤                                                 ▗▜ ▗▌                    │
    │                       ▗▌  ▗▌ ▟ ▞▖     ▟    ▟  ▟ ▐ ▌▞▌ ▗▀▙▀▜▗▀▌▟ ▞▀▄▜▗▀▜  │
    │                    ▟ ▗█▐▗▀▘▝▀ ▀▘▝▀▌ ▞▜▌▀▙▀▀▀▞▀▘▀▀ ▝▘▝▀▀ ▝  ▀ ▝▘▀▘ ▝ ▘ ▝▄▌│
30.7┤                ▄ ▗▄▛▄▌▜ ▜         ▝▄▌▝▌ ▜                              ▜▚│
    │             ▄ ▐ ▚▌                                                       │
28.3┤          ▖ ▐▝▄▌                                                          │
    │         ▐▚▗▟                                                             │
26.0┤       ▗▗▟▝▌                                                              │
    │       █▌                                                                 │
    │      ▗▘▘                                                                 │
23.6┤     ▟▞                                                                   │
    │  ▗▀▀▘▘                                                                   │
    │  ▞                                                                       │
21.3┤▞▌▌                                                                       │
    │▌▝▌                                                                       │
19.0┤▌                                                                         │
    └┬─────────────────┬──────────────────┬─────────────────┬─────────────────┬┘
     1.0             30.8               60.5              90.3            120.0
                              tps data distribution (avg=29.8 SD=3)
                ┌──────────────────────────────────────────────────────────────┐
 [32.7,~) 3 100%┤███                                                           │
[31.2,~) 25  97%┤████████████████████████                                      │
[29.8,~) 64  76%┤██████████████████████████████████████████████████████████████│
 [28.3,~) 5  23%┤█████                                                         │
 [26.8,~) 6  19%┤██████                                                        │
 [25.3,~) 4  14%┤████                                                          │
 [23.8,~) 3  10%┤███                                                           │
 [22.4,~) 5   8%┤█████                                                         │
 [20.9,~) 3   4%┤███                                                           │
 [19.4,~) 1   1%┤█                                                             │
 [17.9,~) 1   0%┤█                                                             │
                └┬──────────────┬───────────────┬──────────────┬──────────────┬┘
                 1.0          16.8            32.5           48.3          64.0

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
                                   tps time series
     ┌─────────────────────────────────────────────────────────────────────────┐
33.01┤                                ▞▜   ▗▌                                  │
     │                                ▌▐   ▐▌                                  │
32.51┤                                ▌▐   ▐▌                                  │
     │                                ▌▐   ▌▌                                  │
     │                                ▌▐   ▌▌                                  │
32.01┤  ▗▌          ▟       ▗▌    ▗  ▗▘▝▖ ▗▘▚   ▗▀▌▗▀▀▄  ▞▜  ▟  ▗▀▚▖▗▀▌▗▀▚▄▟   │
     │  ▐▌          █       ▐▌    █  ▐  ▌ ▐ ▐   ▐ ▌▐  ▐  ▌▐  █  ▐  ▌▐ ▌▐   ▐   │
31.51┤  ▐▌          ▌▌      ▐▌    █  ▐  ▌ ▌ ▐   ▐ ▌▐  ▐  ▌▐  █  ▐  ▌▐ ▌▐   ▐   │
     │  ▌▐          ▌▌      ▌▐   ▗▘▌ ▐  ▌ ▌ ▐   ▌ ▐▌   ▌▐  ▌▐ ▌ ▌  ▐▌ ▐▌   ▐   │
     │  ▌▐          ▌▐      ▌▐   ▐ ▌ ▐  ▌▐  ▐   ▌ ▐▌   ▌▐  ▌▐ ▌ ▌  ▐▌ ▐▌   ▐   │
31.00┤▄▄▌▝▄▄▄▄   ▗▄▗▘▝▄▖ ▄▄▄▌▝▄▚▄▟ ▚▄▟  ▚▟  ▝▄▄▄▌ ▝▌   ▚▟  ▚▟ ▚▄▌  ▝▌ ▝▌   ▝▖▗ │
     │       ▐   ▌▐▐   ▌▐                                                   ▌█ │
     │       ▐   ▌▐▐   ▌▐                                                   ▌█ │
30.50┤        ▌ ▗▘ █   ▐▞                                                   ▙▘▌│
     │        ▌ ▐  █   ▐▌                                                   █ ▌│
30.00┤        ▚▄▟  ▜   ▝▌                                                   ▜ ▚│
     └┬─────────────────┬─────────────────┬─────────────────┬─────────────────┬┘
      51.0            68.3              85.5              102.8           120.0
                              tps data distribution (avg=31.3 SD=1)
                ┌──────────────────────────────────────────────────────────────┐
 [32.7,~) 3 100%┤██████                                                        │
 [32.4,~) 0  95%┤                                                              │
 [32.0,~) 3  95%┤██████                                                        │
[31.7,~) 19  91%┤████████████████████████████████                              │
 [31.3,~) 0  64%┤                                                              │
[30.9,~) 38  64%┤██████████████████████████████████████████████████████████████│
 [30.6,~) 0  10%┤                                                              │
 [30.2,~) 0  10%┤                                                              │
 [29.9,~) 7  10%┤████████████                                                  │
                └┬──────────────┬───────────────┬──────────────┬──────────────┬┘
                 0.0           9.5            19.0           28.5          38.0
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
