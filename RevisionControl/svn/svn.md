 #  server
    yum -y install  subversion

    指定svn的数据存储路径
    mkdir -p /application/svndata
    指定svn的配置文件信息路径
    mkdir -p /application/svnpasswd
    启动svn服务
    svnserve -d -r /application/svndata/


    检测svn服务是否正常启动,
        第一通过进程检测
        ps -ef | grep svn
        第二通过端口3690检测
        netstat -lntup | grep 3690
        第三通过文件检测,需要root用户才可以执行
        lsof -i :3690

    使用svnadmin建立svn项目版本库
        查看创建项目版本库命令
        svnadmin --help
        svnadmin help create
        创建sadoc版本库
        svnadmin create /application/svndata/sadoc

    配置sadoc版本可的权限
        进入sadoc版本库配置目录,并备份配置文件
        cd /application/svndata/sadoc/conf/
        cp -p svnserve.conf svnserve.conf.default
        进行详细配置
        anon-access = none //禁止匿名访问
        auth-access = write //认证后有读的权限
        password-db = /application/svnpasswd/passwd //指定密码文件
        authz-db = /appplication/svnpasswd/authz //指定权限认证文件
    复制passwd和authz文件到sadoc的svnpasswd目录并修改权限
      执行如下命令完成操作
      cp -p authz passwd /application/svnpasswd/
      cd /application/svnpasswd/
      chmod 700 authz passwd

    为Svn版本库创建用户并授权访问指定项目版本库
      编辑passwd文件配置用户和密码
      vi passwd
      username = password
      编辑authz文件配置读取权限
       [<版本库>:/项目/目录]
       @<用户组名> = <权限>
       <用户名>  = <权限>

    重新启动svn服务进行验证
      杀死svn服务
       pkill svnserve
       启动svn
       svnserve -d -r /application/svndata/
       备注:修改passwd和authz文件不需要重启svn服务而修改svnserve.conf则需要

    最后安装客户端进行sadoc的配置是否正确
       svn --username=xingmaogou co svn://121.xxx.xxx.xx9/sadoc
    配置passwd,authz,svnserve.conf注意前面不能有空格!

http://www.linuxidc.com/Linux/2017-05/144254.htm


# client

https://www.cnblogs.com/likwo/archive/2010/09/08/1821232.html

    svn cp svn://svn-svr/branch svn://svn-svr/new_branch -m "branche for all in one"

    svn revert --recursive folder:  取消add
