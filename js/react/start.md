### 全局安装Webpack, Babel, Webpack-dev-server：

```
npm install babel webpack webpack-dev-server -g
```

### 在项目中安装 react, react-dom

```
npm install react react-dom --save
```

### 在项目中安装 Babel 转换器，需要用到插件 babel-preset-react, babel-preset-latest，latest 即最新的 ES 规范，包括了 Async/Await 这些新特性。

```
npm install babel-loader babel-core babel-preset-react babel-preset-latest --save
```

### 配置webpack，编辑webpack.config.js

```
module.exports = {
    entry: './main.js', // 入口文件路径
    output: {
        path: '/',
        filename: 'index.js'
    },
    devServer: {
        inline: true,
        port: 3333
    },
    module: {
        loaders: [
            {
                test: /\.js$/, // babel 转换为兼容性的 js
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'latest']
                }
            }
        ]
    }
}
```

### 配置 npm scripts, 编辑 package.json，在"scripts"属性处添加一行：

```
"scripts": {
   "start": "webpack-dev-server"
},
```