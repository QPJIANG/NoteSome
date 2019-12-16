```
sudo apt-get update: 升级安装包相关的命令,刷新可安装的软件列表(但是不做任何实际的安装动作)

sudo apt-get upgrade: 进行安装包的更新(软件版本的升级)

sudo apt-get dist-upgrade: 进行系统版本的升级(Ubuntu版本的升级)

sudo do-release-upgrade: Ubuntu官方推荐的系统升级方式,若加参数-d还可以升级到开发版本,但会不稳定

sudo apt-get autoclean: 清理旧版本的软件缓存

sudo apt-get clean: 清理所有软件缓存

sudo apt-get autoremove: 删除系统不再使用的孤立软件
```



```
卸载
sudo apt-get remove --purge 软件名称  
sudo apt-get autoremove --purge 软件名称


清理残留数据
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P 
```

