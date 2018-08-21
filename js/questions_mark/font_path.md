参考：https://blog.csdn.net/guoscy/article/details/79192065

真实路径应该是
xxx/static/fonts/icomoon.0125455.woff 
浏览器实际加载路径为：
xxx/static/css/static/fonts/icomoon.0125455.woff 
解决方法：
webpack 配置问题
在 build/webpack.prod.conf.js 中 extract :true 改为 fasle即可。

``` less
  module: {
    rules: utils.styleLoaders({
      sourceMap: config.build.productionSourceMap,
      extract: false
    })
  },
```


