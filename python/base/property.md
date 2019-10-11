

参考：<https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208>

```
property

class property([fget[, fset[, fdel[, doc]]]])
参数
    fget -- 获取属性值的函数
    fset -- 设置属性值的函数
    fdel -- 删除属性值函数
    doc -- 属性描述信息

变量=property([fget[, fset[, fdel[, doc]]]])  

class().变量  调用fget 读取值
class().变量=xxx  调用 fset 设置值

@property 修饰函数,函数名为变量，该函数功能与 fget 一致 (函数只有一个参数self)
@变量.setter  修饰函数,该函数功能与 fset 一致,函数第二个参数为赋值参数（第一个参数为self）
@变量.deleter  修饰函数,该函数功能与 fdel 一致(函数只有一个参数self)

```

