



 <build> 下增加

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-war-plugin</artifactId>
    <version>2.5</version>
    <configuration>
        <!-- 逗号分割，打包war 时排除文件 -->
        <excludes>
            **/node_modules/**
        </excludes>
    </configuration>
</plugin>
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>exec-npm-install</id>
            <phase>prepare-package</phase>
            <!-- <phase>generate-sources</phase> -->
            <!-- <phase>initialize</phase> -->
            <goals>
                <goal>exec</goal>
            </goals>
            <configuration>
                <executable>cnpm</executable>
                <arguments>
                    <argument>install</argument>
                </arguments>
                <workingDirectory>${basedir}/src/main/webapp/static</workingDirectory>
            </configuration>
        </execution>
        <execution>
            <id>exec-npm-run-build</id>
            <phase>prepare-package</phase>
            <!-- <phase>generate-sources</phase> -->
            <goals>
                <goal>exec</goal>
            </goals>
            <configuration>
                <executable>cnpm</executable>
                <arguments>
                    <argument>run</argument>
                    <argument>build</argument>
                </arguments>
                <workingDirectory>${basedir}/src/main/webapp/static</workingDirectory>
            </configuration>
        </execution>
        <!-- 其他调用和继续增加 -->
    </executions>
</plugin>
```

