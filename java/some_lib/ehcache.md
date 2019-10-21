maven

```xml
 <!-- https://mvnrepository.com/artifact/net.sf.ehcache/ehcache -->
    <dependency>
      <groupId>net.sf.ehcache</groupId>
      <artifactId>ehcache</artifactId>
      <version>2.10.6</version>
    </dependency>
    <!--  slf4j-nop: resolve error: SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder". -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-nop</artifactId>
      <version>1.7.2</version>
    </dependency>

```



ehcache.xml   (位于class_path 下)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ehcache xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://ehcache.org/ehcache.xsd">

        <!-- 磁盘缓存位置   -->
        <diskStore path="java.io.tmpdir/ehcache"/>
        <!-- <diskStore path="/tmp/ehcache"/> -->
    
        <!-- 默认缓存 -->
        <!-- <defaultCache maxEntriesLocalHeap="10000" eternal="false" timeToIdleSeconds="120" timeToLiveSeconds="120" maxEntriesLocalDisk="10000000" diskExpiryThreadIntervalSeconds="120" memoryStoreEvictionPolicy="LRU"/> -->
        <!-- helloworld缓存 -->
        <!-- <cache name="helloworld" maxElementsInMemory="1000" eternal="false" timeToIdleSeconds="5" timeToLiveSeconds="5" overflowToDisk="false" memoryStoreEvictionPolicy="LRU"/> -->

        <!-- <diskStore path="/tmp"/> -->
        <defaultCache maxElementsInMemory="10000" eternal="false" timeToIdleSeconds="60" timeToLiveSeconds="60" overflowToDisk="true" maxElementsOnDisk="1000000" diskPersistent="false" diskExpiryThreadIntervalSeconds="120" memoryStoreEvictionPolicy="LRU"/>
        <cache name="myCache" eternal="false" maxElementsInMemory="10000" maxElementsOnDisk="1000000" timeToIdleSeconds="120" timeToLiveSeconds="10" overflowToDisk="true" diskPersistent="false" diskSpoolBufferSizeMB="100" memoryStoreEvictionPolicy="LFU"/>

        <cache name="datasetCache" eternal="false" maxElementsInMemory="10000" maxElementsOnDisk="1000000" timeToIdleSeconds="120" timeToLiveSeconds="10" overflowToDisk="true" diskPersistent="false" diskSpoolBufferSizeMB="100" memoryStoreEvictionPolicy="LFU"/>

</ehcache>

```

java 使用:

```java
// Create a cache manager
CacheManager cacheManager = new CacheManager();

// get the cache called "datasetCache"
Cache cache = cacheManager.getCache("datasetCache");

// create a key to map the data to
String key = "greeting";

// Create a data element
Element putGreeting = new Element(key, "Hello, World!");

// Put the element into the data store
cache.put(putGreeting);

// Retrieve the data element
Element getGreeting = cache.get(key);

// Print the value
System.out.println(getGreeting.getObjectValue());

```

spring 使用: 

 参考:

<https://blog.csdn.net/feiyangtianyao/article/details/90692021>

<https://www.cnblogs.com/Jimc/archive/2018/09/21/9685350.html>

```xml
<bean id="ehcache"
    class="org.springframework.cache.ehcache.EhCacheManagerFactoryBean">
    <property name="configLocation" value="classpath:ehcache.xml" />
</bean>

<bean id="cacheManager" class="org.springframework.cache.ehcache.EhCacheCacheManager">
	<property name="cacheManager" ref="ehcache" />
</bean>

<cache:annotation-driven cache-manager="cacheManager" />

```

