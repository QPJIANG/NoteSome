glide install:

```
curl https://glide.sh/get | sh   
	add  cmd glide to PATH
or
go get github.com/Masterminds/glide
```



glide usage:

```
glide create	初始化项目并创建glide.yaml文件.  (在项目根目录下执行，生成glide.yaml)
glide init	初始化项目并创建glide.yaml文件.(在项目根目录下执行，生成glide.yaml)
glide update	更新解析下载包依赖
glide up	更新解析下载包依赖
glide install	安装包
glide get	获取单个包
　　--all-dependencies 会下载所有关联的依赖包
　　-s 删除所有版本控制，如.git
　　-v 删除嵌套的vendor
glide name	查看依赖名称
glide list	查看依赖列表
glide help	帮助
glide --version查看版本

glide mirror set [original] [replacement]	替换包的镜像
glide mirror set [original] [replacement] --vcs [type]	替换包的镜像
glide mirror remove [original]	移除包的镜像
glide mirror list	获取包的镜像列表
--------------------- 
作者：风.foxwho 
来源：CSDN 
原文：https://blog.csdn.net/fenglailea/article/details/79107124 
版权声明：本文为博主原创文章，转载请附上博文链接！
```

