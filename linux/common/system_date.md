```
执行tzselect命令-->选择Asia-->选择China-->选择east China - Beijing,  Shanghai, etc-->然后输入1

TZ='Asia/Shanghai'; export TZ

----------------------------------------------------------------------------------------
# rm -f  /etc/localtime
# ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
----------------------------------------------------------------------------------------
timedatectl set-timezone Asia/Shanghai
```

