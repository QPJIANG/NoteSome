参考：

 <https://www.cnblogs.com/ralap7/p/9093480.html>

<https://www.cnblogs.com/baodaren/p/5174496.html>



```
1. 关键字inline 必须与函数定义体放在一起才能使函数成为内联，仅将inline 放在函数声明前面不起任何作用。
2. inline只适合函数体内代码简单的函数数使用，不能包含复杂的结构控制语句例如while、switch，并且内联函数本身不能是直接递归函数(自己内部还调用自己的函数)。
3. 内联是以代码膨胀（复制）为代价，仅仅省去了函数调用的开销，从而提高函数的执行效率。

以下情况不宜使用内联：
（1）如果函数体内的代码比较长，使用内联将导致内存消耗代价较高。
（2）如果函数体内出现循环，那么执行函数体内代码的时间要比函数调用的开销大。
```



```
将内联函数放在头文件里实现是合适的,省却你为每个文件实现一次的麻烦.
而所以声明跟定义要一致,其实是指,如果在每个文件里都实现一次该内联函数的话,那么,最好保证每个定义都是一样的,否则,将会引起未定义的行为,即是说,如果不是每个文件里的定义都一样,那么,编译器展开的是哪一个,那要看具体的编译器而定.所以,最好将内联函数定义放在头文件中. 
```

```
现在的CPU上都有cache，紧凑的代码在chache中保存的时间更长，这样cache命中的机会更高。
如果某个A函数未定义为inline，并且被很多其它函数调用，那个这个A函数很大的可能会长期被保存在cahe中，这样CPU对代码的执行速度会提高很 多。如果A函数被定义为了inline函数，代码分散各个调用函数中，这样每次指定都不命中都需要去内存把代码拷贝到cache中，然后执行，造成很大的 抖动。
更深一层的理解，当函数整个函数编译为的汇编代码，函数调用的上下文切换占用了大多的时间的时候，可以考虑把此函数定义为inline函数。   

```

```
高频函数，cache命中有利于提高性能。（函数调用存在上下文切换时间）
inline 函数将代码分发到调用的函数，来减少函数调用上下文切换的时间，但同时增加了 把内存代码拷贝到cache 的时间消耗（内存命中降低）。
需要衡量函数调用与函数内联的时间消耗来决定使用哪种。
```



编译器相关： 

参考：https://www.jianshu.com/p/9cdea930c818

```
对gcc来说，inline只是建议，具体是否展开，还要看其他因素。比如没有使用相关优化选项，则不会内联。如果使用了相关优化选项，如-finline-functions，-O等，有时gcc也会对那些简单的函数自动内联，即使那些函数并没有定义内联。
```

```
static inline的内联函数，一般情况下不会产生函数本身的代码，而是全部被嵌入在被调用的地方。
如果不加static，则表示该函数有可能会被其他编译单元所调用，所以一定会产生函数本身的代码。
所以加了static，一般可令可执行文件变小。内核里一般见不到只用inline的情况，而都是使用static inline。


另一种说法：
1、首先，inline函数是不能像传统的函数那样放在.c中然后在.h中给出接口在其余文件中调用的,因为inline函数其实是跟宏定义类似，不存在所谓的函数入口。

2、因为第一点，会出现一个问题，就是说如果inline函数在两个不同的文件中出现，也就是说一个.h被两个不同的文件包含，则会出现重名，链接失败所以static inline 的用法就能很好的解决这个问题，
使用static修饰符，函数仅在文件内部可见，不会污染命名空间。
可以理解为一个inline在不同的.C里面生成了不同的实例，而且名字是完全相同的
```

