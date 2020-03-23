查看进程PID专用工具 pgrep



```
当前用户所有进程号： pgrep -u $USER
当前用户所有进程号+进程名：  pgrep -l  -u $USER

-l  : 显示pid 和进程名
-u  ： 过滤用户
-x  : 进程名精确查找

$ pgrep -l -u $USER Typo
1619 Typora
1621 Typora
1651 Typora

$ pgrep -l -x -u $USER Typora
1619 Typora
1621 Typora
1651 Typora


更多用法：
    pgrep -h  
    man pgrep
```

