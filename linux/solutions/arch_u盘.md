arch 不识别u盘:

```
手动加载内核模块: usb_storage 
# modprobe usb_storage

#uas 模块可不加载
# modprobe uas

重新插入u盘
---------------------------------------------------------------------------------
卸载内核模块:
# rmmod usb_storage
rmmod: ERROR: Module usb_storage is in use by: uas

# rmmod uas
# rmmod usb_storage

```

