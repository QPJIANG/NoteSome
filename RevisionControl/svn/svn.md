 #  server

```
0.验证是否有svnserver (svnserve --version)
1.安装svnserver 
2.验证是否安装成功 (svnserve --version)
3.进入到svn的资源目录 (cd /home/svndir)
4.创建svn资源库 (svnadmin create <repositories_name>:  建立repositories库)
5.新增用户  (passwd)
6.配置用户权限 (authz)
7.配置资源库权限 (svnserver.conf)
8.启动或者重启 ( svnserve -d -r  svn资源库目录)
9.测试
```

```
检测svn服务是否正常启动,
    第一通过进程检测
    ps -ef | grep svn
    第二通过端口3690检测
    netstat -lntup | grep 3690
    第三通过文件检测,需要root用户才可以执行
    lsof -i :3690
    
使用svnadmin建立svn项目版本库
  
    创建sadoc版本库
    svnadmin create </xx/repositorie_full_path>

    在当前目录下创建svn仓库(按repositories_name创建目录)
    svnadmin create <repositorie_name> 
    多个项目可以创建多个目录
    repositories
        --repositorie
        --repositorie2
        --repositorie3
    启动是使用repositories目录

    
    配置repositorie,repositorie/conf 目录下为配置文件
        svnserve.conf 
        passwd （svnserve.conf 指定路径）
        authz   (svnserve.conf 指定路径）

        svnserve.conf 进行详细配置
        #--------------------------------------
        anon-access = none //禁止匿名访问
        auth-access = write //认证后有读的权限
        password-db = /xxx/passwd //指定密码文件
        authz-db = /xxx/authz  //指定权限认证文件
        #--------------------------------------


        passwd,authz 多个repositorie可以共用，

    
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
       svnserve -d -r /xxx/repositories
       备注:修改passwd和authz文件不需要重启svn服务而修改svnserve.conf则需要

    svn co 获取代码

    配置passwd,authz,svnserve.conf注意前面不能有空格!

```
参考：
http://www.linuxidc.com/Linux/2017-05/144254.htm
https://www.cnblogs.com/javayu/p/6165312.html

多仓库配置参考：
https://blog.csdn.net/jctian000/article/details/80623621  （推荐）

-----------------------------------------------
默认的资源库是空的
创建主要目录
```bash
mkdir branches
mkdir tags
mkdir trunk
svn add branches trunk tags
svn ci -m 'create branches trunk tags dir'
```
创建branches:
```bash
svn copy svn://xxxx/<project>/trunk svn://xxxx/<project>/branches/<branch_name>  -m "commit info"
```

切换分支： 
```bash
svn sw svn_branch_url
```
合并代码(merge)：
```bash
将svn_branch_url 分支的代码合并到当前分支
svn merge svn_branch_url  
svn diff
svn commit -m "merge info"



将svn_branch_url 分支的代码 合并指定版本的代码到当前分支
svn diff -r v1:v2 svn-branch-url  查看需要的合并的分支的修改
svn merge -r version1:version2    svn_branch_url

svn diff   查看合并了哪些内容
svn commit -m "merge info"



svn merge可以将两个对象的diff体现到本地工作目录上。
两个对象: 这个两个对象可以是同一个svn url的两个revison，也可以是不用的url，比如分支和主干。
diff: diff可以是新增的内容，那么就是将一个对象的内容合并到另外一个对象上去。如果diff是减少的内容，那么就是将一个对象的内容回滚掉。

```
撤销修改
```bash
修改未提交
svn revert [R] .   撤销当前目录下的修改

修改已提交：
svn merge 
svn log 找到需要回滚的版本
查看差异： svn diff -r 20:10 [xxx_file_dir]
回滚： svn merge -r 20:10 xxx_file_dir  (同时可用于升级版本合并代码)
提交回滚： svn commit 
```
diff
```bash
svn diff -r v1:v2 只能看到当前分支相关的diff
svn diff -r v1:v2 svn-branch-url  : 查看指定分支的diff


svn diff branche1  branche2    : 查看两个分支的diff
svn diff 目录   branche2   : 查看当前分支与指定分支的差异（二者目录一致）
```

-----------------------------------------------

撤销add

```
svn revert --depth infinity .   撤销当前目录下add 的所有文件
```







# client

https://www.cnblogs.com/likwo/archive/2010/09/08/1821232.html

```bash
svn revert --recursive folder:  取消add
svn add . --no-ignore --force :递归目录下所有文件
```
日常问题：
```bash
svn错误:a peg revision is not allowed here解决方法
原因说明：需要提交的文件的文件名包含“@”
解决方法：在文件名后加@，并且在中间的@前加\
```