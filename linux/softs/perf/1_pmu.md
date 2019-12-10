参考  https://github.com/freelancer-leon/notes/blob/master/kernel/profiling/perf.md

```
使用原始的 PMC 性能事件
根据 CPU 的手册,通过性能事件的标号配置 PMU 的性能计数器
perf top/stat ‐e r[Umask:EventSelect]


```

```
 # perf stat -e r003c -a sleep 5

 Performance counter stats for 'system wide':

 	 26,086,011,863 r003c                                                       

 	5.001757790 seconds time elapsed

```

