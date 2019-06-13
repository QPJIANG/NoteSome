运行daocker 

```bash
# docker run -d -P training/webapp python app.py 


# docker exec -it <container_id> /bin/bash


# docker run -d -p 5001:5000 training/webapp python app.py

-p 指定端口映射 :  -p <本地端口>:<docer 端口>
-d 后台运行

# docker run hello-world 
命令运行完成后daocker container 退出.
```

docker run 指定镜像时不指定tag 默认为 latest





docker -v : Docker容器启动的时候，如果要挂载宿主机的一个目录，可以用-v参数指定。冒号":"前面的目录是宿主机目录，后面的目录是容器内目录。

参考:<https://blog.csdn.net/hnmpf/article/details/80924494>

```bash
# docker run -it -v /test:/soft -v /data:/data centos:tag /bin/bash

需要挂载多个目录 多次使用-v 参数
1.容器目录不可以为相对路径
2.宿主机目录如果不存在，则会自动生成
3.宿主机的目录如果为相对路径:相对路径指的是/var/lib/docker/volumes/，与宿主机的当前目录无关
4.-v指定一个目录 docker run -it -v /test2 centos /bin/bash
	在/var/lib/docker/volumes 下随机生成的一个目录名
5. 在容器内修改了目录的属主和属组,对应的挂载点也会变化(用户uuid 与宿主机uuid对应的用户相关)
6. 容器销毁了，宿主机上生成的挂载目录不会消失
7.挂载宿主机已存在目录后，在容器内对其进行操作，报“Permission denied”。
	(1) 关闭selinux
	(2) 以特权方式启动容器 ,指定--privileged参数,
		# docker run -it --privileged=true 
```

docker inspect  container_names

"Mounts":{}    显示磁盘挂载