





vim 鼠标左键选中文字时显示 VISUAL  : （由于开启了鼠标）

```
编辑 ～/.vimrc 添加如下内容

set mouse-=a
```



记住上次编辑位置

```
"remember last update or view postion"
 " Only do this part when compiled with support for autocommands
 if has("autocmd")
 " In text files, always limit the width of text to 78 characters
 autocmd BufRead *.txt set tw=78
 " When editing a file, always jump to the last cursor position
 autocmd BufReadPost *
 \ if line("'\"") > 0 && line ("'\"") <= line("$") |
 \ exe "normal g'\"" |
 \ endif
 endif
```

