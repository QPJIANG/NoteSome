参考： https://www.cnblogs.com/GodBug/p/7890311.html



1、Mac下编译Linux, Windows平台的64位可执行程序：

```
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build test.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build test.go
```

2、Linux下编译Mac, Windows平台的64位可执行程序：

```
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build test.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build test.go
```

3、Windows下编译Mac, Linux平台的64位可执行程序：

```
SET CGO_ENABLED=0SET GOOS=darwin3 SET GOARCH=amd64 go build test.go
SET CGO_ENABLED=0 SET GOOS=linux SET GOARCH=amd64 go build test.go
```

生成单个二进制文件

```
go build -o outputpath/outputfile  go_entrance_file.go      
需要编译多个命令，指定不同的入口文件，及不同的输出文件。
```





开发中编译：

```
设置环境变量： GOPATH，GOBIN

go install go_source_file.go
```

