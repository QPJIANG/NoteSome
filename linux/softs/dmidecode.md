dmidecode:

linux 查看 内存条具体信息, 几根内存条 命令

```
sudo dmidecode | grep -A19 "Memory Device$"
```

```
Total Width:
Data Width:
Size: 
Locator
Bank Locator:
Type:   DDR4/DDR3
Speed:
```

