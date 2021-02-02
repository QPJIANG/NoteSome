

https://zhuanlan.zhihu.com/p/336277248

```
1. 下载 qemu.x86_64.qcow2.xz 并解压，得到qcow2 文件（qemu虚拟机磁盘文件）

2. 定制： Ignition
	2.1 编写配置yaml
	2.2 通过fcct 工具将yaml 转成Ignition（json）  命令： fcct -o xxx.ign xxxxx.yaml
	
3. 使用ignation 和 qcow2 文件创建和启动虚拟机。
```

fcct: 工具下载 https://github.com/coreos/fcct/releases

yaml 配置： 

参考： https://docs.fedoraproject.org/en-US/fedora-coreos/producing-ign/  https://docs.fedoraproject.org/en-US/fedora-coreos/fcct-config/

Writing the FCC file
Copy the following example into a text editor:

```yaml
variant: fcos
version: 1.2.0
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - ssh-rsa AAAA...
```

Replace the above line starting with ssh-rsa with the contents of your SSH public key file.

Save the file with the name example.fcc. （fcc 为yaml 格式）

用户密码，支持，ssh 和 hash ， passwd_hash 

core 用户： 可通过sudo su 切换到root

```yaml
storage:
  files:
    - path: /etc/hostname
      mode: 0644
      contents:
        inline: coreos
    - path: /etc/NetworkManager/system-connections/ens2.nmconnection
      mode: 0600
      contents:
        inline: |
          [connection]
          id=ens2
          type=ethernet
          interface-name=ens2
          [ipv4]
          address1=192.168.10.30/24,192.168.10.1
          dns=192.168.2.254;
          dns-search=
          dhcp-hostname=coreos
          may-fail=false
          method=manual

```





```
FCC file structure
The FCC file follows YAML syntax and contains the following top-level nodes:

variant: specifies fcos as the operating system

version: specifies the version of fcct

ignition: specifies a remote configuration (for convenience or for platforms that do not allow for the ingestion of large configuration files)

storage: provisions storage and configures the filesystem

systemd: controls systemd units

passwd: configures users
```



install.sh (root) 

```sh
IGNITION_CONFIG="ign file path"
IMAGE="qcow2 file path"
VM_NAME="vm_name"
VCPUS="2"
RAM_MB="2048"
DISK_GB="10"
STREAM="stable"

## 网卡配置的hostonly： --network network=hostonly
## 磁盘空间检查不通过（磁盘不足）： --check disk_size=off
virt-install --connect="qemu:///system" --name="${VM_NAME}" --vcpus="${VCPUS}" --memory="${RAM_MB}" \
        --os-variant="fedora-coreos-$STREAM" --import --graphics=none \
        --disk="size=${DISK_GB},backing_store=${IMAGE}"  --check disk_size=off\
        --network network=hostonly \
        --qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}"

```

启动进入系统后跟目录不可写：切换到root 执行  chattr -i /