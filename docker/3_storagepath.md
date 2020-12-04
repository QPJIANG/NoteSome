

参考: https://blog.csdn.net/wenwenxiong/article/details/78728696

```
sudo docker info | grep "Docker Root Dir"  查存储路径

1. 停docker 服务
2. 移动docker目录
3. 将移动后的目录软连接到移动前的目录
4. 启动docker 服务
```



```
systemctl status docker 查service 文件 (/usr/lib/systemd/system/docker.service)


ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 
结尾加 --graph
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --graph  存储路径

```

