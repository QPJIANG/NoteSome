

 <finalName>demo</finalName>   指定打包生产的文件名，默认会带版本号

添加 assembly,  

mainClass：  指定jar 运行时的main 函数。  （普通maven 项目打包为可运行jar 可用）



```xml
<build>
    <finalName>demo</finalName>
    <plugins>
      <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <configuration>
          <appendAssemblyId>false</appendAssemblyId>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
          <archive>
            <manifest>
              <mainClass>com.xxx.xxx.App</mainClass>
            </manifest>
          </archive>
        </configuration>
        <executions>
          <execution>
            <id>make-assembly</id>
            <phase>package</phase>
            <goals>
              <goal>assembly</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
```

