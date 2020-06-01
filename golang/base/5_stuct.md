```go
type StructType struct {
    var1 type1
    var2 type2
    var3 type3    
}


var varstruct StructType // 声明结构体
```



```go
type User struct{
    name string
    age int
    address string
}

user:= User{name:"测试",age:10} 
user.address="地址"
f.Println(user)


//匿名结构
 person:= struct {
     name string
     age int
 }{name:"匿名",age:1}
 f.Println("person:",person)
```



```
结构体属性名大写开头，否则无法转json
```

