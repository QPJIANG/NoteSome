**语法**：<结果类型> := <目标类型> ( <表达式> )

string  []byte

```
// string 转 []byte
bytes_var := []byte("xxxxxx")  

// []byte 转 string
str_var := string(byte_var[:])
```



**语法**： <目标类型的值>，<布尔参数> := <表达式>.( 目标类型 ) // 安全类型断言

<目标类型的值> := <表达式>.( 目标类型 )　　//非安全类型断言

