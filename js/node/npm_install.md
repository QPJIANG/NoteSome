npm 与cnpm 用法基本一致。



```
npm的包安装分为本地安装（local）、全局安装（global）两种，从敲的命令行来看，差别只是有没有-g而已

本地： 就项目路径而言，就是package.json 所在的目录。
全局：npm install <package_name> -g  , 安装之后所有项目可用（部分包包含命令工具，命令所在目录会加入到 PATH 中，命令行里可直接键入命令使用）

```



```
package.json

包含项目属性：name，version ,author,description (部分配置可选)
包含项目打包，运行，调用：scripts （可选）
包含项目运行依赖：dependencies （可选）
包含项目开发依赖:devDependencies （可选）
engines （可选）
browserslist （可选）
。。。。
```



```
npm init

初始化js 项目：生成package.json

```

```
依赖包安装

(本地安装，执行npm 目录 与package.josn 同级)
npm install <package_name> --save命令会添加条目到package.json的dependencies中。
npm install <package_name> --save-dev命令会添加条目到package.json的devDependencies中。
包安装位置： package.json 同级目录的node_modules 目录下。


```

