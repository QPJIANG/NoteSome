```
将data 目录同步到/bak 目录下： /bak/data
rsync -av --exclude data/a --exclude data/b --exclude data/c data /bak
```

```
同步目录下的内容到目标目录
rsync -av data/  /bak
```

