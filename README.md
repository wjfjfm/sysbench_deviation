## Sysbench Output Deviation

**Usage:**

```bash
$ python3 sb_deviation.py sample_sysbench_output.txt
```

**Sample Output:**

```text
Total Records: 120
[tps] avg: 217.13    std_err(SE): 0.37      std_dev(SD): 4.10      max-min: 27.41
[qps] avg: 3908.88   std_err(SE): 6.30      std_dev(SD): 69.05     max-min: 403.99
[lat] avg: 45.22     std_err(SE): 0.17      std_dev(SD): 1.87      max-min: 9.17
[ r ] avg: 3040.34   std_err(SE): 4.87      std_dev(SD): 53.39     max-min: 299.51
[ w ] avg: 868.54    std_err(SE): 1.48      std_dev(SD): 16.26     max-min: 106.67
[ o ] avg: 0.00      std_err(SE): 0.00      std_dev(SD): 0.00      max-min: 0.00
```
