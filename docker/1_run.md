运行daocker 



```
# docker run -d -P training/webapp python app.py 


# docker exec -it <container_id> /bin/bash


# docker run -d -p 5001:5000 training/webapp python app.py

-p 指定端口映射 :  -p <本地端口>:<docer 端口>
-d 后台运行

# docker run hello-world 
命令运行完成后daocker container 退出.
```

