### pip source

```
Python官方: https://pypi.python.org/simple/
v2ex :	http://pypi.v2ex.com/simple/
清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：https://pypi.douban.com/simple/
```



### pip source config

```
~/.pip/pip.conf 

[global]
index-url=https://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```



### solutions:
```

The repository located at pypi.doubanio.com is not a trusted or secure host and is being ignored.

~/.pip/pip.conf 中将 http 换为 https

```

### windows:

```

(1):在windows文件管理器中,输入 **%APPDATA%**

(2):会定位到一个新的目录下，在该目录下新建pip文件夹，然后到pip文件夹里面去新建个pip.ini文件

(3):在新建的pip.ini文件中输入以下内容，搞定文件路径：pip\pip.ini

```

