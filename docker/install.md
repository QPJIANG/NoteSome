https://wiki.archlinux.org/index.php/Docker#Installation



 install

```
$ sudo pacman -S docker

resolving dependencies...
looking for conflicting packages...

Packages (4) bridge-utils-1.6-3  containerd-1.2.0-2  runc-1.0.0rc5+168+g079817cc-1  docker-1:18.09.0-2

Total Download Size:    55.75 MiB
Total Installed Size:  269.04 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 bridge-utils-1.6-3-x86_64                                    15.5 KiB   310K/s 00:00 [#################################################] 100%
 runc-1.0.0rc5+168+g079817cc-1-x86_64                          2.0 MiB   296K/s 00:07 [#################################################] 100%
 containerd-1.2.0-2-x86_64                                    21.0 MiB   218K/s 01:39 [#################################################] 100%
 docker-1:18.09.0-2-x86_64                                    32.7 MiB   218K/s 02:34 [#################################################] 100%
(4/4) checking keys in keyring                                                        [#################################################] 100%
(4/4) checking package integrity                                                      [#################################################] 100%
(4/4) loading package files                                                           [#################################################] 100%
(4/4) checking for file conflicts                                                     [#################################################] 100%
(4/4) checking available disk space                                                   [#################################################] 100%
:: Processing package changes...
(1/4) installing bridge-utils                                                         [#################################################] 100%
(2/4) installing runc                                                                 [#################################################] 100%
(3/4) installing containerd                                                           [#################################################] 100%
(4/4) installing docker                                                               [#################################################] 100%
Optional dependencies for docker
    btrfs-progs: btrfs backend support [installed]
    pigz: parallel gzip compressor support
:: Running post-transaction hooks...
(1/4) Reloading system manager configuration...
(2/4) Creating system user accounts...
(3/4) Reloading device manager configuration...
(4/4) Arming ConditionNeedsUpdate...
```

service:

```
启用： docker.service
# systemctl start docker
# docker info
```

if you want to be able to run docker as a regular user, add your user to the `docker` [user group](https://wiki.archlinux.org/index.php/User_group).



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

install:

```
# pacman -S docker
```

start service:

```
# systemctl status docker
# systemctl start docker
```

base usage:

```
docker --help
docker version
docker version
docker images

```



文档： https://docs.docker.com/get-started/