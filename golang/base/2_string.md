```
strings.Join(a []string, sep string) string // 拼接

s := []string{"hello", "word", "xxx"}
fmt.Println(strings.Join(s, "-")) // hello-word-xxx

```

字符串分割：

```
strings.Fields(s string) []string				// 按空格分割
strings.FieldsFunc(s string, f func(rune) bool) []string   // 自定义分割函数

Split(s, sep string) []string						// 分割，段尾不保留分割字符
strings.SplitAfterN（s,step string,n int） []string // 分割成几段，保留分割字符在段尾
strings.SplitAfter（s, sep string）[]string		  // 分割成几段，保留分割字符在段尾
strings.SplitN(s, sep string, n int) []string // 分割成几段，段尾不保留分割字符
```



```go
用于类型转换
strconv

```

