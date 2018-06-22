```
http://npm.taobao.org/
npm install -g cnpm --registry=https://registry.npm.taobao.org

npm help
npm list
npm install <name> [-g] [--save-dev]
-g：全局安装。 
--save：将保存配置信息至package.json（package.json是nodejs项目配置文件）；
-dev：保存至package.json的devDependencies节点，不指定-dev将保存至dependencies节点；

(cnpm -save 不可用，尽量使用--save)

npm install moduleName # 安装模块到项目目录下
 
npm install -g moduleName # -g 的意思是将模块安装到全局，具体安装到磁盘哪个位置，要看 npm config prefix 的位置。（部分系统需要使用sudo）
 
npm install -save moduleName # -save 的意思是将模块安装到项目目录下，并在package文件的dependencies节点写入依赖。
 
npm install -save-dev moduleName # -save-dev 的意思是将模块安装到项目目录下，并在package文件的devDependencies节点写入依赖。

npm uninstall <name> [-g] [--save-dev] 
```

some module

```
sudo cnpm install -g create-react-app   ; create-react-app appname(只能小写)

moment    
andt
```