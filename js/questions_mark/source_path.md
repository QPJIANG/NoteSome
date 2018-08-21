问题描述：
```
	npm run build 打包后的html 文件，引用js,css 使用绝对路径，导致资源访问失败。
```
解决方法：
```
	config/index.js 中找到 build 配置：
	assetsPublicPath: '/' 改为 assetsPublicPath: '',
```