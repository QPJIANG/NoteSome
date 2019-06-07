## install virtualenv
```
# pip install virtualenv
# pip3 install virtualenv
```


```
virtualenv --no-site-packages venv		# python version = python -V
virtualenv -p /usr/bin/python3.5 --no-site-packages  venv	# 制定python版本
virtualenv --no-site-packages --always-copy  venv  # --allways-copy  文件不是用软链接

```





### virtualenvwrapper: 基于virtualenv之上的工具，它将所有的虚拟环境统一管理。

```
sudo pip install virtualenvwrapper

virtualenvwrapper默认将所有的虚拟环境放在 WORKON_HOME 目录下管理，可以修改环境变量WORKON_HOME来指定虚拟环境的保存目录。
 WORKON_HOME 默认值: ～/.virtualenvs
 
~/.bashrc

export WORKON_HOME=~/Envs
source $(which virtualenvwrapper.sh)


用法

创建虚拟环境
$ mkvirtualenv env27

创建指定解释器的虚拟环境
$ mkvirtualenv -p python3.4 env34
 

启动虚拟环境
$ workon env27 

退出虚拟环境
$ deactivate 

删除虚拟环境
$ rmvirtualenv env27





```

