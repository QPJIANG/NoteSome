software source:


archlinuxcn:

	仓库主地址：http://repo.archlinuxcn.org/

	使用方法：在 /etc/pacman.conf 文件末尾添加以下两行（或者从后边的链接中选择一个镜像）：

	[archlinuxcn]
	Server = http://repo.archlinuxcn.org/$arch
	之后安装 archlinuxcn-keyring 包以导入 GPG key。

multilib:
	Enabling
		To use the multilib repository, uncomment the [multilib] section in /etc/pacman.conf (Please be sure to uncomment both lines):

		[multilib]
		Include = /etc/pacman.d/mirrorlist
		Then upgrade the system and install the desired multilib packages.(pacman -Syu)

		Tip: Run pacman -Sl multilib to list all packages in the multilib repository. 32-bit library package names begin with lib32-.
	Disabling
		To revert to a pure 64-bit system:

		Execute the following command to remove all packages that were installed from multilib:

		# pacman -R $(paclist multilib | cut -f1 -d' ')
		If you have conflicts with gcc-libs reinstall the gcc-libs package and the base-devel group.

		Comment out the [multilib] section in /etc/pacman.conf:

		#[multilib]
		#Include = /etc/pacman.d/mirrorlist
		Then upgrade the system.

