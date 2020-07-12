参考： https://www.cnblogs.com/liwanliangblog/p/9194146.html



```
下载地址： https://sourceforge.net/projects/pdsh/

tar -jxvf pdsh-2.26.tar.bz2 -C /tmp，解压至/tmp/pdsh-2.26

cd /tmp/pdsh-2.26/

./configure \
--prefix=/usr/local/globle/softs/tools/pdsh/2.26/ \
--with-timeout=60 \
--with-ssh \
--with-exec \
--with-nodeupdown \
--with-readline \
--with-rcmd-rank-list=ssh
```

```
选项	解释
--prefix	指定安装目录
--with-timeout=60	指定pdsh默认执行超时时间
--with-ssh	编译ssh模块
--with-exec	编译exec模块
--with-nodeupdown	编译节点宕机功能
--with-readline	编译readline功能
--with-rcmd-rank-list	指定默认模式为ssh
--with-machines	指定默认主机列表
```

```
 World writable and sticky bit is not set
 将报错目前权限设置为755 或775 ， 不能是777
```

