```
使用`:=`的时候要确保左值没有被定义过
:=  会创建局部变量  （当要给全局变量赋值时要注意）
在函数中，简洁赋值语句 := 可在类型明确的地方代替 var 声明。
函数外的每个语句都必须以关键字开始（var, func 等等），因此 := 结构不能在函数外使用。

https://tour.go-zh.org/


变量的初始化
    变量声明可以包含初始值，每个变量对应一个。
    如果初始化值已存在，则可以省略类型；变量会从初始值中获得类型。


变量未赋值，默认值：
    数值类型为 0，
    布尔类型为 false，
    字符串为 ""（空字符串）。
    

数值常量是高精度的值。
	一个未指定类型的常量由上下文来决定其类型。

初始化语句和后置语句是可选的。
	for ; sum < 1000; {

for 是 Go 中的 “while”
	sum := 1
	for sum < 1000 {
		sum += sum
	}
无限循环
	如果省略循环条件，该循环就不会结束，因此无限循环可以写得很紧凑。
	for {
	}
	
if 语句与 for 循环类似，表达式外无需小括号 ( ) ，而大括号 { } 则是必须的
if 语句可以在条件表达式前执行一个简单的语句。该语句声明的变量作用域仅在 if 之内。（在最后的 return 语句处使用 v 看看。）
    func pow(x, n, lim float64) float64 {
        if v := math.Pow(x, n); v < lim {
            return v
        } else {
            fmt.Printf("%g >= %g\n", v, lim)
        }
        // 这里开始就不能使用 v 了
        return lim
    }
    
switch:switch 的 case 无需为常量，且取值不必为整数
Go 自动提供了在这些语言中每个 case 后面所需的 break 语句。 除非以 fallthrough 语句结束，否则分支会自动终止。
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
而如果switch没有表达式，它会匹配true。
如果case带有fallthrough，程序会继续执行下一条case,不会再判断下一条case的expr,当前case fallthrough 后的语句不会执行

pow[] 
for i, v := range pow {
// i 下标
// v value
}
for i := range pow{
	// 只有下标
}

----------------------------------------------
map[<keytype>]<value_type>

type Vertex struct {
	Lat, Long float64
}
var m map[string]Vertex
func xxxxx() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

elem, ok := m[key]
若 key 在 m 中，ok 为 true ；否则，ok 为 false。若 key 不在映射中，那么 elem 是该映射元素类型的零值。

---------------------------------------------------
函数作为参数
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

compute(<func_name>)

函数的闭包(与 js 闭包类似)

------------------------------------
 go 无类，有结构体
 
 类型（接收者）+函数  组合构成了类似类的结构。
 接收者的类型定义和方法声明必须在同一包内
 不能为内建类型声明方法（接收者不能为内建类型）。
 指针接收者：可改变接收者类型。
 普通接收者：不能改变接收者类型。
------------------------------------
 接口：
 普通类型转为接口类型，通过接口类型调用函数。（需普通类型实现了接口类型对应的函数。同时需要区分指针类型与普通类型）
type Abser interface {
	Abs() float64
}
func (f MyFloat) Abs() float64
func (v *Vertex) Abs() float64
var a Abser
f := MyFloat(-math.Sqrt2)
v := Vertex{3, 4}

a = f  // a MyFloat 实现了 Abser
a = &v // a *Vertex 实现了 Abser

// 下面一行，v 是一个 Vertex（而不是 *Vertex）
// 所以没有实现 Abser。
//a = v
a.Abs()
------------------------------------
接口可能等于空指针（函数调用中需要判断），接口有 ：接口值，类型

空接口可保存任何类型的值。（因为每个类型都至少实现了零个方法。）
var i interface{}
i=xxxx  


类型断言 提供了访问接口值底层具体值的方式。
t := i.(T)
t, ok := i.(T)
若 i 保存了一个 T，那么 t 将会是其底层值，而 ok 为 true。
否则，ok 将为 false 而 t 将为 T 类型的零值。

类型选择：类型选择中的声明与类型断言 i.(T) 的语法相同，只是具体类型 T 被替换成了关键字 type。
switch v := i.(type) {
case T:
    // v 的类型为 T
case S:
    // v 的类型为 S
default:
    // 没有匹配，v 与 i 的类型相同
}


fmt 包中定义的 Stringer 是最普遍的接口之一。
type Stringer interface {
    String() string
}
Stringer 是一个可以用字符串描述自己的类型。fmt 包（还有很多包）都通过此接口来打印值
与 fmt.Stringer 类似，error 类型是一个内建接口：

type error interface {
    Error() string
}

------------------------------------
------------------------------------




```

