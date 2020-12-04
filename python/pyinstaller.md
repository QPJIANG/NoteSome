pyinstaller

```
pip install pyinstaller
```



```
参数说明:

-w指令 (不带额外参数)
直接发布的exe应用带命令行调试窗口，在指令内加入-w命令可以屏蔽；

-F指令(不带额外参数)
注意指令区分大小写。这里是大写。使用-F指令可以把应用打包成一个独立的exe文件，否则是一个带各种dll和依赖文件的文件夹；

-p指令
这个指令后面可以增加pyinstaller搜索模块的路径。因为应用打包涉及的模块很多。这里可以自己添加路径

-i 指定exe图标打包



```







```
例子:

pyinstaller -F myfile.py	（打包后运行：ImportError: No module named ，使用-p ）		

pyinstaller -F myfile.py  -p  源码包根目录 ,  可执行程序换节点可能不能执行

pyinstaller -F setup.py 打包exe
pyinstaller -F -w setup.py 不带控制台的打包
pyinstaller -F -i xx.ico setup.py 打包指定exe图标打包

pyinstaller  -D xxxx/setup.py
pyinstaller -p xxxx -D  xxx/setup.py
pyinstaller xxx.spec   
```

  





cxfreeze, py2exe



```
pip install cx_freeze
```





```


```

