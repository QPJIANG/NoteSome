```xml 
<dependency>  
    <!-- 排除一些不需要同时下载的依赖jar  -->
 	<groupId>xxx</groupId>  
    <artifactId>xxx</artifactId>  
    <version>${xxxx.version}</version>  
    <exclusions>  
    	<exclusion> 
        	<groupId>x</groupId>  
            <artifactId>xx</artifactId>  
        </exclusion>
     </exclusions>
</dependency>

<!--排除所有依赖的jar-->
<exclusions>
    <exclusion>
        <groupId>*</groupId>
        <artifactId>*</artifactId>
    </exclusion>
</exclusions>
```

一般在包冲突或项目瘦身时使用.