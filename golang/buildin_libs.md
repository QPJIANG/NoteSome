plugin (build in)

```
加载动态库: 不能卸载
编译lib:
go build -buildmode=plugin plugin.go

import (
	.....
	"plugin"
)

p0, err0 := plugin.Open("plg/plugin.so")
if err0 != nil {
	panic(err0)
}
m0, err0 := p0.Lookup("GetProductBasePrice")
if err0 != nil {
	panic(err0)
}
res0 := m0.(func(int) int)(30)
fmt.Println(res0)

```

