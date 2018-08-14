参考： https://www.cnblogs.com/wolf-song/p/7708472.html

下载 :

``` markdown
1. jdk
2. hadoop
3. spark
```


系统配置：

``` markdown
1. jdk 配置
2. 节点免密登录配置
3. 关闭selinux
4. 关闭防火墙
```


安装hadoop:

``` markdown
1. 解压压缩包
2. 配置配置文件
	PATH:
		hadoop/etc/hadoop 
	FILES: 
		Core.xml
		Hdfs-site.xml
		Mapred-site.xml
		Yarn-site.xml
		Slaves 
3. 配置运行环境变量
	hadoop-env.sh yarn-env.sh
4. 分发
5. 初始化启动:
	bin/hdfs namenode -format
	sbin/start-dfs.sh
6. jps  检查启动情况
```
安装Spark:

``` stylus
1. 配置系统环境
	/etc/profile
	export SPARK_HOME=/XXX
	export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
2. 配置spark:
	conf/spark-env.sh
	export SPARK_MASTER_IP=sparkmaster
	export SPARK_MASTER_PORT=7077
	export SPARK_WORKER_CORES=1
	export SPARK_WORKER_INSTANCES=1
	export SPARK_WORKER_MEMORY=512M
	export SPARK_LOCAL_IP=ip     # 每个节点的ip

3. slave 配置：
	conf/slaves
	host1
	host2
```




