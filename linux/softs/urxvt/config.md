```
!!$HOME/.Xresources
URxvt.preeditType:Root
!!调整此处设置输入法
URxvt.inputMethod:fcitx
!!颜色设置
URxvt.depth:32
!!中括号内数表示透明度
URxvt.inheritPixmap:true
URxvt.background:#000000
URxvt.foreground:#ffffff
URxvt.colorBD:Gray95
URxvt.colorUL:Green
URxvt.color1:Red2
URxvt.color4:RoyalBlue
URxvt.color5:Magenta2
URxvt.color8:Gray50
URxvt.color10:Green2
URxvt.color12:DodgerBlue
URxvt.color14:Cyan2
URxvt.color15:Gray95
!!URL操作
URxvt.urlLauncher:chromium
URxvt.matcher.button:1
Urxvt.perl-ext-common:matcher
!!滚动条设置
URxvt.scrollBar:False
URxvt.scrollBar_floating:False
URxvt.scrollstyle:plain
!!滚屏设置
URxvt.mouseWheelScrollPage:True
URxvt.scrollTtyOutput:False
URxvt.scrollWithBuffer:True
URxvt.scrollTtyKeypress:True
!!光标闪烁
URxvt.cursorBlink:True
URxvt.saveLines:3000
!!边框
URxvt.borderLess:False
!!字体设置
Xft.dpi:96
URxvt.font:xft:Source Code Pro:antialias=True:pixelsize=18,xft:WenQuanYi Zen Hei:pixelsize=18
URxvt.boldfont:xft:Source Code Pro:antialias=True:pixelsize=18,xft:WenQuanYi Zen Hei:pixelsize=18

Xft.rgba: rgb
Xft.hinting: true
Xft.hintstyle: hintslight

! 实现ctrl+shift+c/v的复制粘贴
URxvt.iso14755: false
URxvt.iso14755_52: false
URxvt.keysym.Shift-Control-V: eval:paste_clipboard
URxvt.keysym.Shift-Control-C: eval:selection_to_clipboard
```

生效

```
xrdb -load ~/.Xresource
```



```
参考：
https://www.cnblogs.com/vachester/p/5649813.html
https://segmentfault.com/a/1190000020859490
```
