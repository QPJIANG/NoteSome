鉴于国内网络问题，后续拉取 Docker 镜像十分缓慢，我们可以需要配置加速器来解决，我使用的是网易的镜像地址：http://hub-mirror.c.163.com。

​	新版的 Docker 使用 /etc/docker/daemon.json（Linux）

 	或者 %programdata%\docker\config\daemon.json（Windows） 来配置 Daemon。

请在该配置文件中加入（没有该文件的话，请先建一个）：

 ```
  {
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
  }
 ```



列举镜像:

```
# docker image ls
# docker images -a
```



查找镜像:

```
docker search 关键字

eg:
# docker search centos
NAME                               DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
centos                             The official build of CentOS.                   5395                [OK]                
ansible/centos7-ansible            Ansible on Centos7                              121                                     [OK]
jdeathe/centos-ssh                 CentOS-6 6.10 x86_64 / CentOS-7 7.5.1804 x86…   110                                     [OK]
.................................................................

```



拉取镜像:

```
# docker pull 镜像名   默认latest
# docker pull 镜像名:tag

eg:
# docker pull centos
Using default tag: latest
latest: Pulling from library/centos
Digest: sha256:b5e66c4651870a1ad435cd75922fe2cb943c9e973a9673822d1414824a1d0475
Status: Downloaded newer image for centos:latest

```

删除镜像:

```
# docker image rm centos:latest
Error response from daemon: conflict: unable to remove repository reference "centos:latest" (must force) - container d2a788c60caa is using its referenced image 9f38484d220f

强制删除
# docker image rm centos:latest -f
Untagged: centos:latest
Untagged: centos@sha256:b5e66c4651870a1ad435cd75922fe2cb943c9e973a9673822d1414824a1d0475
Deleted: sha256:9f38484d220fa527b1fb19747638497179500a1bed8bf0498eb788229229e6e1


```



### 创建镜像两种方式:

- 1.从已经创建的容器中更新镜像，并且提交这个镜像
- 2.使用 Dockerfile 指令来创建一个新的镜像



#### 1. 更新镜像

更新镜像之前，我们需要使用镜像来创建一个容器。

```
1. 运行镜像
2. 修改container
3. 提交container 得到新的镜像


eg:
运行镜像:
# docker run -d -it centos
查看运行状态
# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
093b1127c08c        centos              "/bin/bash"         4 seconds ago       Up 2 seconds                            festive_keller
进入docker container 修改
# docker exec -it 093b1127c08c /bin/bash

提交镜像
# docker commit -m="has update" -a="test" 093b1127c08c centos7/java:0.1
sha256:eb63dd7210fcc2f1317ee33564fd7b0cbc240437ce8d1230705a4e447d32d8e0

查看镜像列表
# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos7/java        0.1                 eb63dd7210fc        7 seconds ago       697MB
centos              latest              9f38484d220f        2 months ago        202MB


```

```
docker commit

-m:提交的描述信息
-a:指定镜像作者
093b1127c08c：容器ID
centos7/java:0.1   :指定要创建的目标镜像名(image:tag)

```

