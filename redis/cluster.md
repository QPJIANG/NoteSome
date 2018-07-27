参考： https://www.cnblogs.com/mafly/p/redis_cluster.html

一.

```
redis.conf 关键配置：

port 9001（每个节点的端口号）
daemonize yes
bind 192.168.119.131（绑定当前机器 IP）
dir /usr/local/redis-cluster/9001/data/（数据文件存放位置）
pidfile /var/run/redis_9001.pid（pid 9001和port要对应）
cluster-enabled yes（启动集群模式）
cluster-config-file nodes9001.conf（9001和port要对应）
cluster-node-timeout 15000
appendonly yes

配置好后启动所有节点
```

二.

```
ruby 相关软件安装：
yum install ruby
yum install rubygems
gem install redis 
```

三. 创建集群

```
redis/bin/redis-trib.rb create --replicas 1 node1_ip:node1_port node2_ip:node2_port ......
```

四.查看集群状态及简单使用

```
redis-cli -c -h node_ip -p port
-c: 连接到集群
> cluster info
> cluster nodes
> set key value   : 会自动跳转到保存key 的节点
> keys *  :只能看到当前节点的keys
> get key :得到key 并跳转到保存该key 的节点。
```

集群管理参考：https://blog.csdn.net/qq_37595946/article/details/78069298

