```python
import redis
pool = redis.ConnectionPool(host=host, port=port,db=0)
client = pool.getConnect()
pip = client.pipeline()
client.info()



```

