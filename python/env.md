PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。

开发阶段和将项目的顶层目录放入 PYTHONPATH 方便查找模块。

```
# 列举模块
# py 程序所在的目录，会一起打印出来。
import sys 
module = sys.path 
for i in module: 
	print(i)
```



LD_LIBRARY_PATH： 有时候python 运行时缺少系统lib 。  需将一些 so 文件的目录设置到 LD_LIBRARY_PATH

```
python 连接oracle：
需安装 client 并设置
export LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib:$LD_LIBRARY_PATH
才能连接oracle
```

