# 安装samba

    sudo apt-get install samba

# 配置samba

     /etc/samba/smb.conf
     在最后面加上以下内容

     security = share

    [share]
    comment = share
    path = /home/wsd/software(设置成你要共享的文件路径)
    available = yes
    browsable = yes
    public = yes
    writable = yes
    create mask = 0777

    把/home/wsd/software文件修改成777权限（所有操作都可以执行），执行命令：
    chmod 777 /home/wsd/software

# windows 挂载
    映射网络磁盘： \\ip\share
    share 为配置文件中[share]



# 带用户控制
    /etc/samba/smb.conf

    [myshare1]
    comment = myshare1
    path = /data
    browsable = yes
    writable = yes
    create mask = 0777

    [myshare2]
    comment = myshare2
    path = /code
    browsable = yes
    writable = yes
    create mask = 0777

    cd /etc/samba 
    touch smbpasswd
    smbpasswd -a sambauser

    /etc/init.d/smbd restart
    smbclient -L \\127.0.0.1 -U sambauser

# 其他

    smbpasswd命令的常用方法smbpasswd -a 增加用户（要增加的用户必须以是系统用户）smbpasswd -d 冻结用户，就是这个用户不能在登录了
    smbpasswd -e 恢复用户，解冻用户，
    可以在使用smbpasswd -n 把用户的密码设置成空.  要在global中写入 null passwords -true
    smbpasswd -x 删除用户

