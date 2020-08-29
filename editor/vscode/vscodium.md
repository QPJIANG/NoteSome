



```
vscodium 使用单独的应用仓库，有些扩展找不到（比如sftp）
修改 resources/app/product.json 使用vscode 扩展仓库

修改： extensionsGallery 属性

修改前：

"extensionsGallery": {
	"serviceUrl": "https://open-vsx.org/vscode/gallery",
	"itemUrl": "https://open-vsx.org/vscode/item"
  },
  
修改后：

"extensionsGallery": {
        "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
        "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
        "itemUrl": "https://marketplace.visualstudio.com/items",
        "controlUrl": "https://az764295.vo.msecnd.net/extensions/marketplace.json",
        "recommendationsUrl": "https://az764295.vo.msecnd.net/extensions/workspaceRecommendations.json.gz"
  },
  
重启vscodium可使用vscode 扩展仓库

```

