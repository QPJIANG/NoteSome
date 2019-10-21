.vscode/settings.json

```
// 一个文件使用一个tab
"workbench.editor.enablePreview": false     


// 文件菜单树不显示的文件/目录
"files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/__pycache__": true,
        "**/.DS_Store": true,
        "**/node_modules": true,
        "**/*.pyc": true
    }
```









快捷键设置:

File -> Perferience -> KeyboardShortcuts







```
//文件注释模板： psioniq File Header
   
"psi-header.templates": [
        {
            "language": "*",
            "template": [
                "FileName: <<filename>>",
                "Project: <<projectname>>",
                "",
                "Author: xxx@xxx.com",
                "File Created: <<filecreated('YYYY-MM-DD h:mm:ss ,dddd')>>",
                "",
                "Modified By: <<author>>",
                "Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
                "",
                "Copyright (c) <<filecreated('YYYY')>> xxxxxxxxxx."
            ]
        }
    ],
"psi-header.lang-config": [
        {
            "language": "javascript",
            "begin": "",
            "end": "",
            "prefix": "// "
        },
        {
            "language": "python",
            "begin": "####################################################################################################",
            "end": "####################################################################################################",
            "prefix": "# ",
            "suffix":"#",
            "lineLength":100,
            "replace":[],
            "modAuthor":"Modified By: xxx@xxx.com",
            "modDate":"Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
        }
    ],
"psi-header.changes-tracking":{
        "isActive":true,
        "modAuthor":"Modified By: xxx@xxx.com",
        "modDate":"Last Modified: <<dateformat('YYYY-MM-DD h:mm:ss ,dddd')>>",
        "autoHeader":"autoSave"
    },
```





终端字体不好看(字母间距不一致):    (需要使用等宽字体,monospace 可换为其他可用字体)

```

 // 设置字体可解决问题
 "terminal.integrated.fontFamily": "monospace", 
 // 其他配置
 "terminal.integrated.fontSize": 16,
 "terminal.integrated.copyOnSelection": true,   
 "terminal.integrated.fontWeight":"300",
 "terminal.integrated.fontWeightBold": "100",
 "terminal.integrated.lineHeight": 1.3,
 "terminal.integrated.letterSpacing":0,
 // 字体颜色与背景色
  "workbench.colorCustomizations" : 
    {
        "terminal.foreground" : "#37FF13",
        "terminal.background" : "#2b2424"
    },

```

