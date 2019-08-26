file:VMware-Workstation-Full-12.0.0-2985596.x86_64.bundle
密钥：5A02H-AU243-TZJ49-GTC7K-3C61N


uninstall:
```
# vmware-installer -l

# vmware-installer --uninstall-product vmware-workstation
```


vmware fail to run:
    Virtual Network Device:
    vmnet

    cd /usr/lib/vmware/modules/source
    tar -xvf vmnet.tar
    cd vmnet-only
    vim netif.c
    
    update the follow code :
    
    #if LINUX_VERSION_CODE >= KERNEL_VERSION(3, 18, 0) || defined(NET_NAME_USER)
       dev = alloc_netdev(sizeof *netIf, deviceName, NET_NAME_USER, VNetNetIfSetup);
    #else
        dev = alloc_netdev(sizeof *netIf, deviceName, VNetNetIfSetup);
    #endif
    
    =====>>>>>
    
    //#if LINUX_VERSION_CODE >= KERNEL_VERSION(3, 18, 0) || defined(NET_NAME_USER)
    //   dev = alloc_netdev(sizeof *netIf, deviceName, NET_NAME_USER, VNetNetIfSetup);
    //#else
    dev = alloc_netdev(sizeof *netIf, deviceName, VNetNetIfSetup);
    //#endif
    
    tar -uvf vmnet.tar vmnet-only
    
    run vmware again: net be ok



```
Failed to build vmnet.  Failed to execute the build command.

https://github.com/mkubecek/vmware-host-modules/releases
解压：
创建压缩包：
# tar -cf vmmon.tar vmmon-only
# tar -cf vmnet.tar vmnet-only
先备份 /usr/lib/vmware/modules/source/
# sudo cp *.tar /usr/lib/vmware/modules/source/
$ sudo vmware-modconfig --console --install-all




```

