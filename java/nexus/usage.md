上次jar 到私服 nexus



1. 创建仓库和用户

   ```
   nexus: 默认用户admin 默认密码：admin123   （为了安全建议首次使用时进行修改）
   ----------------------------------------------------
   Repository->Repositories： 下创建仓库
   
   java maven 私服仓库: 类型选择 maven2(hosted)
   仓库名： 仓库id
   发布策略： 选allow redepoly
   
   填写好后保存，在 Repositories列表中，url 表示仓库地址。
   ----------------------------------------------------
   Security -> Roles
   添加角色：自定义用户权限
   
   Security -> Users 
   添加用户： 配置角色授权
   ```

   

2. 配置maven

   ```
   在settings.xml 中配置服务器用户名密码 (可以是全局的也可以是用户级的)
   
   <server>   
       <id>仓库id</id>   
       <username>admin</username>
       <password>admin123</password>   
   </server>
   
   ```

   

3. 发布jar

   ```
   mvn deploy:deploy-file 
   -DgroupId=包goupid
   -DartifactId=包id
   -Dversion=包版本号
   -Dpackaging=jar 
   -Dfile=jar包路径
   -Durl=仓库地址
   -DrepositoryId=仓库id（与settings 中一致）
   ```

   ```
   如果要把构建部署至私服中，需要在构建的 pom.xml 文件增加 distributionManagement 配置项. 配置见install.md
   ```

   

