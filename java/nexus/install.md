

nexus 3: maven 管理私服

安装使用参考： <https://my.oschina.net/xiaominmin/blog/2050604>



下载地址：

<https://www.sonatype.com/download-oss-sonatype>



安装：

解压 nexus



安装成功后有两个默认账号admin、anonymous，其中admin具有全部权限默认密码admin123；anonymous作为匿名用户，只具有查看权限

本地maven库配置settings.xml

```xml
<settings>

  <pluginGroups>
    <pluginGroup>org.sonatype.plugins</pluginGroup>
  </pluginGroups>

 <servers>
    <server>
      <id>nexus</id>
      <username>admin</username>
      <password>admin123</password>
    </server>
  </servers>

<mirrors>
    <mirror>
      <id>nexus</id>
      <mirrorOf>*</mirrorOf>
      <url>http://localhost:8081/repository/maven-public/</url>
    </mirror>
    <mirror>  
      <id>repo2</id>  
      <mirrorOf>central</mirrorOf>  
      <name>Human Readable Name for this Mirror.</name>  
      <url>http://repo2.maven.org/maven2/</url>  
    </mirror>

  </mirrors>

<profiles>
<profile>
      <id>nexus</id>
      <repositories>
        <repository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </repository>
      </repositories>
     <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://central</url>
          <releases><enabled>true</enabled></releases>
          <snapshots><enabled>true</enabled></snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>

  </profiles>
  <activeProfiles>
    <activeProfile>nexus</activeProfile>
  </activeProfiles>
</settings>
```



工程配置pox.xml

```xml
<distributionManagement>
  <repository>
      <id>nexus</id>
      <name>Releases</name>
      <url>http://localhost:8081/repository/maven-releases</url>
    </repository>
    <snapshotRepository>
      <id>nexus</id>
      <name>Snapshot</name>
      <url>http://localhost:8081/repository/maven-snapshots</url>
    </snapshotRepository>
  </distributionManagement>





<build>
    <defaultGoal>compile</defaultGoal>
    <finalName>page</finalName>
    <plugins>
        <plugin> 
            <groupId>org.apache.maven.plugins</groupId> 
            <artifactId>maven-surefire-plugin</artifactId>  
            <configuration>  
                <skip>true</skip>  
            </configuration> 
        </plugin>
        <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.3</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
    </plugins>
  </build>
```

