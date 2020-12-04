vscode 源码跳转依赖godef ， 需要安装godef

improt 自动导入依赖goimports

godef, goimports 安装：

获取 golang.org/x/tools

```
$ go get -u golang.org/x/tools 
将源码下载到 $GOPATH/src/golang.org/x/tools

在$GOPATH/src/golang.org/x/tools 目录下找到

── cmd
│   ├── auth
│   ├── benchcmp
│   ├── bundle
│   ├── callgraph
│   ├── compilebench
│   ├── cover
│   ├── digraph
│   ├── eg
│   ├── fiximports
│   ├── guru
│   ├── html2article
│   ├── present
│   ├── splitdwarf
│   ├── ssadump
│   ├── stress
│   ├── stringer
│   └── toolstash
相应工具的目录，设置GOBIN 变量后执行 go install 

goimports,guru 位于： tools/cmd 下

```

环境配置可参考：<https://www.cnblogs.com/yangxiaoyi/p/9692369.html>

```
 go test 显示详细
 "go.testFlags": ["-v"]
```

```
go get -v github.com/rogpeppe/godef
go install github.com/mdempsky/gocode
go install github.com/uudashr/gopkgs/v2/cmd/gopkgs
go install github.com/stamblerre/gocode
go install golang.org/x/lint/golint
```

```

非go mod 项目，配置 go.gopath ,go.goroot， 将需要查找依赖包的路径写入gopath (linux  : 分割)
通过gopath/src 下找相应的包。

```

