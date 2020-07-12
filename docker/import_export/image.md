参考： <https://www.jianshu.com/p/8408e06b7273>



导出：

```
docker save <image id>  > targetfile.tar
```

```
[root@wxtest1607 ~]# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
tomcat8                   3.0                 90457edaf6ff        6 hours ago         1.036 GB
[root@wxtest1607 lixr]# docker save 9045 > tomcat8-apr.tar
[root@wxtest1607 lixr]# ls -lh
总用量 1.2G
-rw-r--r--  1 root root  1005M 8月  24 17:42 tomcat8-apr.tar
```

导入：

```
docker load < targetfile.tar
```



```
[root@wxtest1607 lixr]# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
tomcat8                   3.0                 90457edaf6ff        7 hours ago         1.036 GB
[root@wxtest1607 lixr]# docker rmi 9045
Untagged: tomcat8:3.0
Deleted: sha256:90457edaf6ff4ce328dd8a3131789c66e6bd89e1ce40096b89dd49d6e9d62bc8
Deleted: sha256:00df1d61992f2d87e7149dffa7afa5907df3296f5775c53e3ee731972e253600
[root@wxtest1607 lixr]# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
[root@wxtest1607 lixr]# docker load < tomcat8-apr.tar
60685807648a: Loading layer [==================================================>] 442.7 MB/442.7 MB
[root@wxtest1607 lixr]# yer [>                                                  ] 527.7 kB/442.7 MB
[root@wxtest1607 lixr]# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
<none>                    <none>              90457edaf6ff        7 hours ago         1.036 GB
[root@wxtest1607 lixr]# docker tag 9045 tomcat8-apr:3.0
[root@wxtest1607 lixr]# 
[root@wxtest1607 lixr]# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
tomcat8-apr               3.0                 90457edaf6ff        7 hours ago         1.036 GB
```

