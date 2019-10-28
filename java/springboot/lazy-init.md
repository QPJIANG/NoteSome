for spring mvc conf xml:

```
spring配置默认default-lazy-init为false，当配置为true时sping不会再去加载整个对象实例图，大大减少了初始化的时间，减少了spring的启动速度。


使用 @Scheduler 时, beans 的 default-lazy-init为true , 将导致任务在web 启动后不运行.
解决办法:
1. 声明bean 并设置:lazy-init="false"	
2. default-lazy-init 设置为false



1.<beans />                <bean />            						immediately  
2.<beans />                <bean lazy-init="true" />   				lazy       
3.<beans />                <bean lazy-init="false"/>   				immediately  
4.<beans default-lazy-init="true"/>  <bean />          				lazy   
5.<beans default-lazy-init="true"/>  <bean lazy-init="true" />     	lazy   
6.<beans default-lazy-init="true"/>  <bean lazy-init="false" />    	immediately   
7.<beans default-lazy-init="false"/>  <bean />             			immediately   
8.<beans default-lazy-init="false"/>  <bean lazy-init="true" />    	lazy   
9.<beans default-lazy-init="false"/>  <bean lazy-init="false" />   	immediately  

beans 嵌套beans : 以外层的lazy-init为准.
```

