```
-----------------------------------
获取镜像:

-----------------------------------
启动:
docker run -d -p 8088:8088 -v /opt/docker/superset:/home/superset amancevice/superset
docker ps
docker exec -it  def43799758d fabmanager  --help
docker exec -it  def43799758d fabmanager  list-users  --app superset
ls /opt/docker/superset/

# 创建管理员
docker exec -it  def43799758d fabmanager create-admin --app superset

docker exec -it  def43799758d fabmanager  list-users  --app superset

# 更新数据库
docker exec -it  def43799758d superset db upgrade

# 初始化权限
docker exec -it  def43799758d superset init

#载入示例数据
docker exec -it  def43799758d superset load_examples

```

