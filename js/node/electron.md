### start

<https://electronjs.org/docs/tutorial/first-app>



electron 不可用:

```
sudo chown root: xxxxx/node_modules/electron/dist/chrome-sandbox
sudo chmod 4755  xxxxxxx/lib/node_modules/electron/dist/chrome-sandbox
```









### package

```
cnpm install -g electron-prebuilt
cnpm install -g electron-packager

electron-packager <应用目录> <应用名称> <打包平台> --out <输出目录> <架构> <应用版本>
electron-packager . HelloWorld --linux -out ../out  --arch=x64 --app-version=0.0.1 --electron-version=5.0.1

electron-packager ./ --electron-version=5.0.1
```



打包的文件不能执行

```
sudo chown root chrome-sandbox
chmod 4755 chrome-sandbox
```

