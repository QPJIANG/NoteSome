```
takeown /F C:\$Windows.~BT\* /R /A
icacls C:\$Windows.~BT\*.* /T /grant administrators:F 

rmdir /S /Q C:\$Windows.~BT\
```

