参考：https://blog.csdn.net/liuxin191863128/article/details/53406747/

读入配置文件

```xml
<context:property-placeholder location="classpath:jdbc.properties"/>
```

或者

```xml
<bean id="propertyPlaceholderConfigurer" class="org.springframework,beans.factory.config.PropertyPlaceholderConfigurer">
    <property name="locations">
        <list>
            <value>jdbc.properties<value/>
        </list>
    </property>
</bean>
```

配置文件：

```properties
#jdbc配置 
driverClassName=com.mysql.jdbc.Driver url=jdbc:mysql://localhost:3306/test
username=root 
password=root
```

使用：

```xml
<bean id="dataSource" class="org.springframework,jdbc,datasource.DriverManagerDataSource">
    <property name="driverClassName" value="${driverClassName}"/>
    <property name="url" value="${url}"/>
    <property name="username" value="${username}"/>
    <property name="password" value="${password}"/>
</bean>
```



```
由于Spring容器只能有一个PropertyPlaceholderConfigurer，如果有多个属性文件，这时就看谁先谁后了，先的保留 ，后的忽略。
```



