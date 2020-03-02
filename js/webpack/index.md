

https://www.webpackjs.com/

https://www.webpackjs.com/guides/getting-started/



```
组要使用方法参考webpack 官网。
entry： js 入口（chunks）
plugins： 插件: 不同的插件完成不同的功能。
module: {rules: []}  通过不同的loader 处理不同类型的文件
output： entry 编译后生成的文件。
```



```
HtmlWebpackPlugin：  用户生成html,chunks 指定entry 里配置的key. 来完成相应的js 引入。（配置一个html 页面）

var webpack = require('webpack');
# 自动加载模块，无需每处 import 或 require 
new webpack.ProvidePlugin({
    $: 'jquery',
    jQuery: 'jquery'
}),
```



resolve:  引入文件时不用带后缀，同时定义别名 用于导入时简写

```
import xxx from '@/components/xxxx'
```

```
const resolve = dir => path.resolve(__dirname, dir); // 定义函数
```

```
 resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      'vue': 'vue/dist/vue.js',
      '@': resolve('src'),
    }
  }
```

