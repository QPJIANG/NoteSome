1. 键盘布局
```
  控制台键盘布局 默认为us（美式键盘映射）。
  如果您正在使用非美式键盘布局，通过以下的命令选择相应的键盘映射表：
  # loadkeys layout
```
2. 验证启动模式
```
  如果以在 UEFI 主板上启用 UEFI 模式, Archiso 将会使用 systemd-boot 来启动 Arch Linux。可以列出 efivars 目录以验证启动模式:

  # ls /sys/firmware/efi/efivars
  如果目录不存在，系统可能以 BIOS 或 CSM 模式启动
```
3. 连接到因特网
```
  (有线)护进程 dhcpcd 已被默认启用来探测有线设备, 并会尝试连接。
  如需验证网络是否正常, 可以使用 ping:

  (无线)
     wpa-cli

      wpa_supplicant - Wi-Fi Protected Access client and IEEE 802.1X supplicant
      SYNOPSIS
      wpa_supplicant [ -BddfhKLqqsTtuvW ] [ -iifname ] [ -cconfig file ] [ -D driver ] [ -PPID_file ] [ -f output file ]
      
      https://segmentfault.com/a/1190000011579147
      wpa_supplicant是一个连接、配置WIFI的工具，它主要包含wpa_supplicant与wpa_cli两个程序。通常情况下，可以通过wpa_cli来进行WIFI的配置与连接，如果有特殊的需要，可以编写应用程序直接调用wpa_supplicant的接口直接开发。


      # wpa_cli -i wlan0 scan             // 搜索附近wifi网络
      # wpa_cli -i wlan0 scan_result      // 打印搜索wifi网络结果
      # wpa_cli -i wlan0 add_network      // 添加一个网络连接
```
4. 更新系统时间
```
  用 systemd-timesyncd 确保系统时间是正确的：
  # timedatectl set-ntp true
```
5. 建立硬盘分区
```
  fdisk -l

  对于一个选定的设备，以下的分区是必须要有的:

  一个根分区（挂载在根目录） /.
  如果 UEFI 模式被启用,你还需要一个 EFI 系统分区.
  Swap 可以在一个独立的分区上设置，也可以直接建立 交换文件.
  如需修改分区表,使用 fdisk 或 parted. 查看Partitioning (简体中文)以获得更多详情.
  如果需要需要创建多级存储例如 LVM、LUKS 或 RAID，请在此时完成。
```
6. 格式化分区
```
  mkfs.ext4 /dev/sdaX
```
7. 挂载分区
```
  mount /dev/sdaX /mnt
```
  如果使用多个分区，还需要为其他分区创建目录并挂载它们（/mnt/boot、/mnt/home、……）。
```
    # mkdir /mnt/boot
    # mount /dev/sda2 /mnt/boot
```
  genfstab 将会自动检测挂载的文件系统和 swap 分区。

8. 选择镜像
```
    编辑 /etc/pacman.d/mirrorlist
    cd /etc/pacman.d ; cp mirrorlist mirrorlist.back
    cat mirrorlist.back | grep 163 > mirrorlist
```
9. 安装基本系统
```
    pacstrap   /mnt base   (仅安装基础系统)
    pacstrap   /mnt base base-devel
    pacstrap  /mnt net-tools
    pacstrap  /mnt vim
```
#  配置系统

## Fstab:

    # genfstab -U /mnt >> /mnt/etc/fstab   
    (在执行完以上命令后，后检查一下生成的 /mnt/etc/fstab 文件是否正确)

 ## Chroot:

       # arch-chroot /mnt   (切换到安装好的系统)

## 时区:

    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    hwclock --systohc --utc

## (grub 可优先安装配置)
安装并配置 bootloader

    我的主板是BIOS主板，这里采用的 bootloader 是Grub；安装 grub 包，并执行 grub-install 已安装到 MBR：
    # pacman -S grub
    # grub-install --target=i386-pc --recheck /dev/sdb
    
    #	pacman -S intel-ucode
    # grub-install --boot-directory=/mnt/boot /dev/sdb
    注意：须根据实际分区自行调整 /dev/sdb, 切勿在块设备后附加数字，比如 /dev/sdb1 就不对。
    由于我的硬盘上还有另外一个操作系统windows 7，为了检测到该系统并写到grub启动项中，还需要做下面的操作。
    # pacman -S os-prober
    # grub-mkconfig -o /boot/grub/grub.cfg

##  Locale:    设置 /etc/locale.gen  只需移除对应行前面的注释符号（＃）即可

    # nano /etc/locale.gen
    en_US.UTF-8 UTF-8
    zh_CN.UTF-8 UTF-8
    执行locale-gen以生成locale讯息
    # locale-gen
    (/etc/locale.gen 生成指定的本地化文件，每次 glibc 更新之后也会运行 locale-gen。)
    # echo LANG=en_US.UTF-8 > /etc/locale.conf

## 键盘布局配置文件: /etc/vconsole.conf

## 主机名:

	echo myhostname > /etc/hostname
	
	 vim  /etc/hosts
	 127.0.0.1	localhost.localdomain	localhost
	 ::1		localhost.localdomain	localhost
	 127.0.1.1	myhostname.localdomain	myhostname

##  网络配置:

    对新安装的系统，需要再次设置网络。具体请参考 Network configuration (简体中文) 和
    
    对于 无线网络配置，安装 软件包 iw, wpa_supplicant，dialog 以及需要的 固件软件包.

##  Initramfs

    如果修改了 mkinitcpio.conf，用以下命令创建一个初始 RAM disk：
    # mkinitcpio -p linux

## Root 密码

    设置 root 密码:
    # passwd

## 安装图形桌面

    # pacman -S xorg xorg-server
    # pacman -S deepin
    # pacman -S deepin-extra
    
    ls -1 /usr/share/xgreeters/
    
    vi /etc/lightdm/lightdm.conf
    Find the following line:
    #greeter-session=example-gtk-gnome
    And, uncomment and change it as shown below.
    greeter-session=lightdm-deepin-greeter
    
    lightdm --test-mode --debug
    
    systemctl start lightdm.service
    systemctl enable lightdm.service

##  中文乱码: https://www.cnblogs.com/bluestorm/p/6039197.html


## 输入法:

	# pacman -S fcitx fcitx-im fcitx-googlepinyi fcitx-configtool

## 网络:

    # pacman -S networkmanager
    # systemctl enable NetworkManager

先ip link 看网卡设备名。以ens192为例

cd /etc/netctl
cp examples/ethernet-static ./ens192
（文件名任意，与下面的netctl一致即可）

vim ens192
改Interface为网卡设备名。
改ip，掩码，网关，dns
然后
netctl enable ens192 （此处的ens192是文件名）
netctl start ens192
当然你也可以用 examples/ethernet-dhcp 这个模板， 只改interface=一处即可。


一篇教程：

http://bbs.archlinuxcn.org/viewtopic.php?id=1037