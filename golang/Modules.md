go v1.11开始支持的[go Modules](https://github.com/golang/go/wiki/Modules)

Go Modules具有一些优点：

- 不必须将项目目录放在GOPATH中
- 不使用vendor目录，而是统一安装到`$GOPATH/pkg/mod/cache`
- build/run时，自动析出项目import的包并安装

go env 查看变量：

$GOPATH  默认为  ${HOME}/go   , go/pkg /mode目录下缓存 依赖包

部分包由于网络原因可能不能下载：

```bash
export GOPROXY="https://athens.azurefd.net"
（这里使用了微软提供的代理）
```





<https://segmentfault.com/a/1190000018536993>

文件依赖引用发生变化：

```go
// 项目下的模块名引入：  go mod init <模块名> ， import <模块名>/模块
```

自定义项目下的包引用：

```go
模块名： go mod init 指定的模块名
包名： 项目目录下的相对目录。
import <模块名>.<包名>
```

