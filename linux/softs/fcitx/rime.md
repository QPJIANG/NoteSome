中州韵输入法

```
	fcitx-rime
```

配置	(参考：<https://gist.github.com/lotem/2981316>)

~/.config/fcitx/rime/default.custom.yaml

```
patch:
  "menu/page_size": 9
  ascii_composer/good_old_caps_lock: true
  ascii_composer/switch_key:
    Caps_Lock: noop
    Shift_L: commit_code

```

```
# inline_ascii 在輸入法的臨時西文編輯區內輸入字母、數字、符號、空格等，回車上屏後自動復位到中文
# commit_text 已輸入的候選文字上屏並切換至西文輸入模式
# commit_code 已輸入的編碼字符上屏並切換至西文輸入模式
# 設爲 noop，屏蔽該切換鍵

~/.config/fcitx/rime/build 下有各schema对应的默认配置 
```

