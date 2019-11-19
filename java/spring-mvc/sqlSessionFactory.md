```
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
	 <property name="dataSource" ref="dataSource"/>
	
</bean>
```

```
org.mybatis.spring.SqlSessionFactoryBean

 public void setDataSource(DataSource dataSource) {
    if (dataSource instanceof TransactionAwareDataSourceProxy) {
      this.dataSource = ((TransactionAwareDataSourceProxy) dataSource).getTargetDataSource();
    } else {
      this.dataSource = dataSource;
    }
  }
```



dataSource实现  getTargetDataSource()  可用作动态选择数据库。  [未验证]