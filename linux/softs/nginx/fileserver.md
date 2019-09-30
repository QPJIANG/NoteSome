参考

<https://blog.csdn.net/wzw_ice/article/details/89414024>

<https://blog.csdn.net/wzw_ice/article/details/89414188>



```
autoindex on;#自动索引
autoindex_localtime on;#自动索引时间
autoindex_exact_size off;#自动索引
```

```
user  root root;
worker_processes auto;

#error_log  logs/error.log;
error_log  logs/error.log  warn;
error_log  logs/info.log  info;

pid        logs/nginx.pid;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';#日志格式

    access_log  logs/access.log  main;

    sendfile        on;#文件发送设置

    keepalive_timeout  65;#超时设置

    #gzip  on;

    server {
        listen       8080; #端口修改
        server_name  localhost;

        charset utf-8;

        #access_log  logs/host.access.log  main;

        location / {
            #root   html;
            #index  index.html index.htm;
            autoindex on;#自动索引
            autoindex_localtime on;#自动索引时间
            autoindex_exact_size off;#自动索引
            
            #如果设置下面，访问是会直接下载文件
            #idefault_type  'application/octet-stream'; 
            #add_header Content-disposition "attachment";
            
            root    /data/file/;	#文件根目录设置
        }
        #error_page  404              /404.html;
        
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
      }
}
```

