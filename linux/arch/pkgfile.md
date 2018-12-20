```
*.so 无法打开共享对象文件: 没有那个文件或目录
pkgfile *.so : 查看so 属于那个包，安装后再看问题能否解决
```



```
ubuntu so 问题：
参考：
https://blog.csdn.net/huoxingrenhdh/article/details/82852852
sudo apt-get install apt-file
sudo apt-file update
apt-file search *.so.* / apt-file search *.so
```

```
yum so 
yum install yum-utils 
yum whatprovides *.so.* / yum whatprovides *.so
```

