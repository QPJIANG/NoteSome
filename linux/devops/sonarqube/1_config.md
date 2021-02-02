```
conf/sonar.properties
```



```
创建数据库，并配置数据库连接信息

sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
sonar.jdbc.username=sonarqube
sonar.jdbc.password=sonarqube
```





```
sonar-scanner \
  -Dsonar.projectKey=jhbi \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://192.168.2.231:9000 \
  -Dsonar.login=577bfdb908c2f52cf42a2e0b31345c1dabd8c0a4
  
  
sonar-scanner \
  -Dsonar.projectKey=jhinsight_trunk \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://192.168.2.231:9000 \
  -Dsonar.login=dbf57a42908b1edae6d4eecca6ab53abfd7298ec
```

```
mvn sonar:sonar \
  -Dsonar.host.url=http://192.168.2.231:9000 \
  -Dsonar.login=577bfdb908c2f52cf42a2e0b31345c1dabd8c0a4
```

