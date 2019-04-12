```
SSH免密码登陆避免首次需要输入yes
ssh -o stricthostkeychecking=no


/etc/ssh/ssh_config文件中的"# StrictHostKeyChecking ask" 为 "StrictHostKeyChecking no"，
sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/' /etc/ssh/ssh_config




警告：POSSIBLE BREAK-IN ATTEMPT
sed -i 's/GSSAPIAuthentication yes/GSSAPIAuthentication no/' /etc/ssh/ssh_config
```

