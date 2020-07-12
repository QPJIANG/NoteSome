
Q:
```
Unable to negotiate with xxx.xxx.xxx.xxx port 22: no matching key exchange method found. Their offer: diffie-hellman-group1-sha1  
```

A:
```
ssh -oHostKeyAlgorithms=+ssh-dss -oKexAlgorithms=+diffie-hellman-group1-sha1 xxx.xxx.xxx.xxx  
```

