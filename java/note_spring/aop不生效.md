```
spring（applicationContext）：aop 放在此处不生效

SpringMVC（webApplicationContext）：aop

i18n 配置 放在applicationContext或webApplicationContext都可以
```



```xml
<aop:aspectj-autoproxy proxy-target-class="true" />

<!--处理切入点对应的处理类-->
<bean id="dealBean"  class="com.jhinno.insight.common.ResultInterceptor"/>

<aop:config proxy-target-class="true">
<!--切面-->
        <aop:pointcut id="dealPointcut" expression="execution(* com.example..*(..)) and @annotation(org.springframework.web.bind.annotation.RequestMapping)"/>
        
<!--切入点-->
        <aop:aspect order="3" ref="dealBean" >
            <aop:around method="aroundMethod" pointcut-ref="dealPointcut" />
        </aop:aspect>
    </aop:config>
```

