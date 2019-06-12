<https://github.com/archlinuxcn/mirrorlist-repo>



 /etc/pacman.conf 

```
## 浙江大学 (浙江杭州) (ipv4, ipv6, http, https)
## Added: 2017-06-05
[archlinuxcn]
Server = https://mirrors.zju.edu.cn/archlinuxcn/$arch
## 中国科学技术大学 (ipv4, ipv6, http, https)
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
## 清华大学 (ipv4, ipv6, http, https)
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
## Our main server (ipv4, ipv6, http, https)
## Our main server located in Netherlands
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
## xTom (Hong Kong server) (Hong Kong) (ipv4, ipv6, http, https)
## Added: 2017-09-18
## xTom Hong Kong Mirror
[archlinuxcn]
Server = https://mirror.xtom.com.hk/archlinuxcn/$arch
## xTom (US server) (US) (ipv4, ipv6, http, https)
## Added: 2019-02-19
## xTom US Mirror
[archlinuxcn]
Server = https://mirror.xtom.com/archlinuxcn/$arch
## Open Computing Facility, UC Berkeley (Berkeley, CA, United States) (ipv4, ipv6, http, https)
## Added: 2019-02-19
[archlinuxcn]
Server = https://mirrors.ocf.berkeley.edu/archlinuxcn/$arch
## 网易 (ipv4, http, https)
[archlinuxcn]
Server = https://mirrors.163.com/archlinux-cn/$arch
## 重庆大学 (ipv4, http, https)
[archlinuxcn]
Server = https://mirrors.cqu.edu.cn/archlinuxcn/$arch
## SJTUG 软件源镜像服务 (ipv4, https)
## Added: 2018-05-21
[archlinuxcn]
Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux-cn/$arch
## 腾讯云 (ipv4, https)
## Added: 2018-11-23
[archlinuxcn]
Server = https://mirrors.cloud.tencent.com/archlinuxcn/$arch
```





Add PGP Keys

```
sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring
```