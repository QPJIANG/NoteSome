```
spring ioc

<context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>......./spring.xml</param-value>
</context-param>


spring mvc:
controller扫描，静态资源路径映射，response和视图模板配置。
interceptor，viewResolver，exceptionResolver，applicaitonContext


<servlet>
    <servlet-name>dispatcher</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>........./applicationContext.xml</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
</servlet>
```

