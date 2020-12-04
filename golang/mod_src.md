

```
https://www.cnblogs.com/saolv/p/12081899.html
```

```
在go mod初始化的项目目录下执行go get package，会将package下载到$GOPATH/pkg目录下安装



非go mod项目，执行go get package，只是将package下载到$GOPATH/src/...目录下安装
export GO111MODULE=off ,后执行 go get package，将package下载到$GOPATH/src/...目录下
```





非go mod 项目： 从 $GOPATH/src 下查找依赖。