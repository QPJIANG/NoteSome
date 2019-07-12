```
error: UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range
参考： https://blog.csdn.net/weixin_39221360/article/details/79525341
解决方法有三种：
1.在命令行修改，仅本会话有效：
1)通过>>>sys.getdefaultencoding()查看当前编码(若报错，先执行>>>import sys >>>reload(sys));
2)通过>>>sys.setdefaultencoding('utf8')设置编码

2.较繁琐，最有效
1)在程序文件中以下三句
import sys
reload(sys)
sys.setdefaultencoding('utf8')
      
3.修改Python本环境（推荐）
在Python的Lib\site-packages文件夹下新建一个sitecustomize.py文件，内容为：
#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')



```





```
open函数指名encoding    文件读取
```

