ImportError: libffi.so.5: cannot open shared object file: No such file or directory



```bash
# rpm -q libffi
libffi-3.0.13-18.el7.x86_64

# find / -name libffi*.so
/usr/lib64/libffi.so

# ln -s libffi.so libffi.so.5
```

