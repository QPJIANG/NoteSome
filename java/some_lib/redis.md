参考: <https://www.cnblogs.com/qlqwjy/p/8562703.html>



maven:

```xml
<!-- jedis依赖 , 使用时选择合适的版本-->
<dependency>
<groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>2.7.1</version>
</dependency>
<dependency>
<groupId>org.springframework.data</groupId>
    <artifactId>spring-data-redis</artifactId>
    <version>1.6.2.RELEASE</version>
</dependency>



<!-- 用于序列化的包 , 使用时选择合适的版本-->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
    <version>2.1.0</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.1.0</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-annotations</artifactId>
    <version>2.1.0</version>
</dependency>
```

config:redis.properties

```
#访问地址  
redis.host=127.0.0.1  
#访问端口  
redis.port=6379  
#注意，如果没有password，此处不设置值，但这一项要保留  
redis.password=  
  
#最大空闲数，数据库连接的最大空闲时间。超过空闲时间，数据库连接将被标记为不可用，然后被释放。设为0表示无限制。  
redis.maxIdle=300  
#连接池的最大数据库连接数。设为0表示无限制  
redis.maxActive=600  
#最大建立连接等待时间。如果超过此时间将接到异常。设为-1表示无限制。  
redis.maxWait=1000  
#在borrow一个jedis实例时，是否提前进行alidate操作；如果为true，则得到的jedis实例均是可用的；  
redis.testOnBorrow=true
```

spring config:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.springframework.org/schema/beans" xmlns:context="http://www.springframework.org/schema/context"
    xmlns:aop="http://www.springframework.org/schema/aop" xmlns:tx="http://www.springframework.org/schema/tx"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-3.0.xsd http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-3.0.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-3.0.xsd ">

    <!-- 连接池基本参数配置，类似数据库连接池 -->
    <context:property-placeholder location="classpath:redis.properties"
        ignore-unresolvable="true" />
    
    <!-- redis连接池 -->  
    <bean id="poolConfig" class="redis.clients.jedis.JedisPoolConfig">
        <property name="maxTotal" value="${redis.maxActive}" />
        <property name="maxIdle" value="${redis.maxIdle}" />
        <property name="testOnBorrow" value="${redis.testOnBorrow}" />
    </bean>

    <!-- 连接池配置，类似数据库连接池 -->
    <bean id="jedisConnectionFactory"
        class="org.springframework.data.redis.connection.jedis.JedisConnectionFactory">
        <property name="hostName" value="${redis.host}"></property>
        <property name="port" value="${redis.port}"></property>
        <!-- <property name="password" value="${redis.pass}"></property> -->
        <property name="poolConfig" ref="poolConfig"></property>
    </bean>

    <!--redis操作模版,使用该对象可以操作redis  -->  
    <bean id="redisTemplate" class="org.springframework.data.redis.core.RedisTemplate" >    
        <property name="connectionFactory" ref="jedisConnectionFactory" />    
        <!--如果不配置Serializer，那么存储的时候缺省使用String，如果用User类型存储，那么会提示错误User can't cast to String！！  -->    
        <property name="keySerializer" >    
            <bean class="org.springframework.data.redis.serializer.StringRedisSerializer" />    
        </property>    
        <property name="valueSerializer" >    
            <bean class="org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer" />    
        </property>    
        <property name="hashKeySerializer">    
            <bean class="org.springframework.data.redis.serializer.StringRedisSerializer"/>    
        </property>    
        <property name="hashValueSerializer">    
            <bean class="org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer"/>    
        </property>    
        <!--开启事务  -->  
        <property name="enableTransactionSupport" value="true"></property>  
    </bean >   


    <!-- 下面这个是整合Mybatis的二级缓存使用的 -->
    <bean id="redisCacheTransfer" class="cn.qlq.jedis.RedisCacheTransfer">
        <property name="jedisConnectionFactory" ref="jedisConnectionFactory" />
    </bean>

</beans>
```

note:

```
被缓存的类需要实现序列化接口 Serializable
```

