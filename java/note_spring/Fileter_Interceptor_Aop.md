# 过滤器、拦截器、AOP切面执行顺序

参考 ： https://blog.csdn.net/w1219401160/article/details/81101641



```
过滤器：基于 Servlet，通过函数回调方式实现，可以过滤请求和图片文件等，每个请求一个过滤器只能过滤一次。

拦截器：基于 java 的反射机制，代理模式实现，只能拦截请求，可以访问上下文等对象，功能强大，一个请求可多次拦截。

拦截器是 Spring 中AOP的一种实现方法。另一种方法通过 Pointcut、Advice实现


filter->interceptor->aop
```

