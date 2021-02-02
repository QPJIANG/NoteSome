```
rpm -qa   :查询安装了的包。

rpm -qal: 查询安装了的包，及包中包含的文件。
```



```
rpm -qf file_filepath  : 查询文件是属于哪个包的
```





rpm 包解压

```
安装软件包： rpm-tools,cpio

rpm2cpio xxx.rpm | cpio -divm
```

