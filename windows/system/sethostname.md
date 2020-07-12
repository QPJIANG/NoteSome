

```
@echo off
:: 修改计算机名,win7 可用
echo 修改计算机名
echo.
set /p name=请输您的计算机名：
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName" /v ComputerName /t reg_sz /d %name% /f >nul 2>nul
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters" /v "NV Hostname" /t reg_sz /d %name% /f >nul 2>nul
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters" /v Hostname /t reg_sz /d %name% /f >nul 2>nul
echo.
echo 修改计算机名完毕

pause>nul
```

机器名可设置为域名或ip.

计算机属性中修改会校验机器名，部分格式的输入不能通过。

