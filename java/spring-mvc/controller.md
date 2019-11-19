参考： https://www.iteye.com/blog/elim-1753271

```
@Controller 用于标记在一个类上，使用它标记的类就是一个SpringMVC Controller 对象。
分发处理器将会扫描使用了该注解的类的方法，并检测该方法是否使用了@RequestMapping 注解。
@Controller 只是定义了一个控制器类，而使用@RequestMapping 注解的方法才是真正处理请求的处理器.
```

