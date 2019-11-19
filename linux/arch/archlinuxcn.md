<https://github.com/archlinuxcn/mirrorlist-repo>




主站点：

https://mirrors.sjtug.sjtu.edu.cn/#/
https://mirrors.ustc.edu.cn/              （根据使用的电信服务商配置域名可更快访问）
https://mirrors.tuna.tsinghua.edu.cn/
https://mirrors.cloud.tencent.com/
https://mirrors.cqu.edu.cn/
https://mirrors.163.com/
https://mirrors.ocf.berkeley.edu/
https://mirrors.zju.edu.cn/
https://mirrors.ustc.edu.cn/
https://mirror.xtom.com/
https://mirror.xtom.com.hk
https://mirrors.huaweicloud.com/

仅archlinuxcn：

https://repo.archlinuxcn.org/



 /etc/pacman.conf 

```
[archlinuxcn]
Server = 主站点/archlinuxcn/$arch
-------------------------------------------------------
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch

```

```
#[testing]
#Include = /etc/pacman.d/mirrorlist

[core]
Include = /etc/pacman.d/mirrorlist

[extra]
Include = /etc/pacman.d/mirrorlist

#[community-testing]
#Include = /etc/pacman.d/mirrorlist

[community]
Include = /etc/pacman.d/mirrorlist

# If you want to run 32 bit applications on your x86_64 system,
# enable the multilib repositories as required here.

#[multilib-testing]
#Include = /etc/pacman.d/mirrorlist

[multilib]
Include = /etc/pacman.d/mirrorlist

-------------------------------------------------------------
[$repo]
Include = /etc/pacman.d/mirrorlist

```







Add PGP Keys

```
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```



mirrorlist

```
Server = 主站点/archlinux/$repo/os/$arch
-------------------------------------------------------
# 163
#Server = http://mirrors.163.com/archlinux/$repo/os/$arch
# 清华
#Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
# 上海交通大学
#Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux/$repo/os/$arch
```





