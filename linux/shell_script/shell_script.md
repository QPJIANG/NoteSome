nice
renice
nohup

dd



```
#!/bin/bash

if [ $# -gt 1 -o  $# -eq 0 ]
then
    # 只接受一个参数，参数个数不正确退出。
	exit 1 
fi


# 获取命令行参数
strnum=`echo $1 | tr -cd "[0-9]"`
echo $strnum

```









