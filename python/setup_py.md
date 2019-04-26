

参考： <https://blog.csdn.net/caiguoxiong0101/article/details/50285279>

setup.py :

```
python setup.py --help-commands
```



打包/安装

1. 编写setup.py

2. 打包

   ```
   python setup.py -q bdist_egg  egg打包
   python setup.py -q bdist_wininst 打包为exe
   python setup.py install  直接安装到python site-packages 目录
   ```

   

egg安装方式：

（1） easy_install xx.egg  

（2）将 xxx.egg`包直接放到虚拟工作目录的`lib > site-packages`路径下，并在`site-packages/easy-install.pth 文件添加egg包路径引用





开发模式:  develop(    install package in 'development mode')

python setup.py develop   :  将开发环境链接到 site-packages  列表。