```
/*匿名结构体*/
emp := struct{
        name, address   string
        height, weight   float64
}{
        name:"eagle",  address:"guangdong",  height:172.0,  weight:75.3，
}
// 备注：这里的最后一个逗号（,）必须要有，否则会报错
```

```
/*匿名结构体数组*/
emp := []struct{
        name, address   string
        height, weight   float64
}{
        {name:"eagle",  address:"guangdong",  height:172.0,  weight:75.3,}，
}
// 备注：结尾逗号（,）必须要有，否则会报错
```




```
/*声明结构体*/

type employee struct{
        name,address string
        height,weight float64
}
/*初始化结构体，并赋给变量emp*/
emp ：= employee{name:"eagle",  address:"guangdong",  height:172.0,  weight:75.3,}
```

```
/*嵌套结构体*/
/*声明figure结构体*/
type figure struct {
	height, weight float64
}

/*声明human结构体，里面嵌套figure结构体*/
type human struct {
	name, address string
	figure
}

man := human{name:"eagle", address:"guangdong", figure:figure{height:172, weight:75.3}}
```

