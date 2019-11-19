
spring.xml
```
<bean id="dcookieSerializer" class="xxxxxxxx.XXXXCookieSerializer"/>
<bean class="org.springframework.session.web.http.CookieHttpSessionStrategy">
		<property name="cookieSerializer" ref="dcookieSerializer"/>
</bean>
```

可参考： org.springframework.session.web.http.DefaultCookieSerializer  实现接口：CookieSerializer

