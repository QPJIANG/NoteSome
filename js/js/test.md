###  解决js相同的正则多次调用test()返回的值却不同的问题

参考：<https://www.jb51.net/article/148529.htm>

这是因为正则reg的g属性，设置的全局匹配。RegExp有一个lastIndex属性，来保存索引开始位置。

**第一种方案**是将g去掉，关闭全局匹配。

**第二种**就是在每次匹配之前将lastIndex的值设置为0。

reg.lastIndex = 0;