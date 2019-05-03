
使用国内源：参考 https://www.cnblogs.com/sunnydou/p/5801760.html

阿里云 http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 

豆瓣(douban) http://pypi.douban.com/simple/ 

清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

pip install <packages> -i http://pypi.douban.com/simple --trusted-host pypi.douban.com



如果想配置成默认的源，方法如下：

需要创建或修改配置文件（一般都是创建），

linux的文件在~/.pip/pip.conf，

windows在%HOMEPATH%\pip\pip.ini），

修改内容为：

```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```
这样在使用pip来安装时，会默认调用该镜像。

<https://pypi.tuna.tsinghua.edu.cn/simple/pip/>  pip 下载地址

<https://pypi.tuna.tsinghua.edu.cn/simple/setuptools/>  setup-tools 下载地址



