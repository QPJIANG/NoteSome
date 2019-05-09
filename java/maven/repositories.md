### 参考:<https://www.cnblogs.com/ctxsdhy/p/8482725.html>

1、在mirrorOf与repositoryId相同的时候优先是使用mirror的地址

2、mirrorOf等于*的时候覆盖所有repository配置

3、存在多个mirror配置的时候mirrorOf等于*放到最后

4、只配置mirrorOf为central的时候可以不用配置repository

### 配置了 repositories,会优先考虑冲repositories配置的镜像下载依赖.

repositories:

```
<releases><enabled>true</enabled></releases>告诉Maven可以从这个仓库下载releases版本的构件，
<snapshots><enabled>false</enabled></snapshots>告诉Maven不要从这个仓库下载snapshot版本的构件。
禁止从公共仓库下载snapshot构件是推荐的做法，因为这些构件不稳定，且不受你控制，你应该避免使用。
如果你想使用局域网内组织内部的仓库，你可以激活snapshot的支持。
```

