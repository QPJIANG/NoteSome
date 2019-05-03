参考：https://m.aliyun.com/jiaocheng/165501.html

创建用户：useradd

```
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]

Options:
  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
  -c, --comment COMMENT         GECOS field of the new account
  -d, --home-dir HOME_DIR       home directory of the new account
  -D, --defaults                print or change default useradd configuration
  -e, --expiredate EXPIRE_DATE  expiration date of the new account
  -f, --inactive INACTIVE       password inactivity period of the new account
  -g, --gid GROUP               name or ID of the primary group of the new
                                account
  -G, --groups GROUPS           list of supplementary groups of the new
                                account
  -h, --help                    display this help message and exit
  -k, --skel SKEL_DIR           use this alternative skeleton directory
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -l, --no-log-init             do not add the user to the lastlog and
                                faillog databases
  -m, --create-home             create the user's home directory
  -M, --no-create-home          do not create the user's home directory
  -N, --no-user-group           do not create a group with the same name as
                                the user
  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
  -p, --password PASSWORD       encrypted password of the new account
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             login shell of the new account
  -u, --uid UID                 user ID of the new account
  -U, --user-group              create a group with the same name as the user

用户可同时属于一个主要组及多个附属组
eg:
  # adduser -g usergroup [-d user_home_path] -m user_name 
  [-G wheel,root]  指定用户属于多个组
  
  修改用户注释信息: usermod -c xxx 用户名
  修改用户名:usermod -l 新名 旧名
  锁定用户:passwd  -l   用户
  解锁:       passwd  -u  用户
  清除用户密码:passwd -d 用户
  设置密码： passwd 用户
```

删除用户组：

```
userdel
# userdel -r user_name   (删除/etc/passwd, /etc/shadow, /etc/group等 文件中的记录 以及用户目录)
```



用户组

```
创建用户组:groupadd 组名

修改组名:groupmod -n newname oldname

修改组编号:groupmod -g 669 组名

创建用户组的同时指定编号: groupadd -g 668 组名

删除用户组:groupdel 组名
```

修改用户组： 

```
# usermod    -a  -G  group_name user_name   : 修改用户附加组
# usermod -g group_name user_name  : 修改用户主组

参考：http://blog.51cto.com/yongtao/1687595

将用户添加至附属组:gpasswd -a 用户名   用户组
从附属组删除用户:gpasswd -d 用户名  附属组名
```



```
改变用户组密码:gpasswd 用户组
```

```bash
 usermod  -l  新用户名  -d  /home/新用户名  -m  老用户名  ： 修改用户名及其家目录
 usermod -l 新用户名 老用户名   ： 仅修改用户名
```

添加一个xxxx的帐号，密码为123456

```bash
# echo xxxx:123456 | chpasswd

# echo '123456'| passwd --stdin xxxx
```

