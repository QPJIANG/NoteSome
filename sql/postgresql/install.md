二进制包部署：

解压二进制包：

**修改解压内容所有者为数据库管理员。并切换至数据库管理员。**

pgsql/bin 下包含相应命令。

```
创建数据存储目录： mkdir 数据存储目录
```

初始化：

```
bin/initdb -D 数据存储目录
```

启动/停止：

```
bin/pg_ctl -D 数据存储目录 -l logfile start  (-l -l logfile 可不使用用 )

bin/pg_ctl -D 数据存储目录  stop 
```

配置：

```
数据存储目录/postgresql.conf 
配置数据库 连接ip及端口（listen_addresses='*'  # localhost 只能本机访问）

#listen_addresses = 'localhost'         # what IP address(es) to listen on;
                                        # comma-separated list of addresses;
                                        # defaults to 'localhost'; use '*' for all
                                        # (change requires restart)
#port = 5432                            # (change requires restart)


数据存储目录/pg_hba.conf
访问白名单，黑名单

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust



可添加：
host    all             all             192.168.0.0/16            trust
```

psql 配置默认端口和默认连接服务器：

export PGPORT=5432
export PGHOST=localhost



