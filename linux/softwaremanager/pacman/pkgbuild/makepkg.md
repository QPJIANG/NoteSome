Arch的打包系统和别的Linux发行版不一样，用ABS系统(Arch Build System)把源代码打包成

.pkg.tar.gz / .pkg.tar.xz 才能安装。



创建`PKGBUILD`文件，也可复制PKGBUILD模板（位于/usr/share/pacman/PKGBUILD.proto）到工作目录或复制一个类似包的PKGBUILD。

复制要编译的脚本到创建的目录中，修改编译脚本。然后在该目录下运行：

> $ makepkg -s

makepkg工具会寻找PKGBUILD文件，根据该文件编译并生成一个*.pkg.tar.gz的文件包，Archlinux采用pacman管理安装包。最后用pacman安装编译生成的包。

```
# pacman -U  *.pkg.tar.gz
```

```
/etc/makepkg.conf 打包配置文件
```

```
makepkg
makepkg --syncdeps
makepkg --install
makepkg --clean
```



```
编写： PKGBUILD
生成软件包： makepkg -s
安装软件包： sudo pacman -U <软件包>
```

PKGBUILD 文件说明

```
# Maintainer: 软件维护者用户信息 <邮箱>

#包名
pkgname=		

# 软件版本
pkgver=

pkgrel=1
epoch=1

# 软件包描述
pkgdesc=""

# 软件架构
# arch=('i686' 'x86_64')
arch=(x86_64)

# 软件网站
url=

# 许可类型
license=('GPL')


groups=()
depends=()
makedepends=()
checkdepends=()

# 软件依赖
optdepends=(
	'依赖包1'
	'依赖包2'
)

provides=()
conflicts=()
replaces=()
backup=()
options=()


install=
changelog=

#源码，可以是本地包，也可以是网络包
source=("./$pkgname-$pkgver.tar.gz")

# 源码 md5sum (未填写makepkg 校验将不通过)
md5sums=(ce4c0......)

# 可替代md5sum
sha256sums=

validpgpkeys=()

# ${srcdir}： 源码目录，会默认创建src 目录，将源码解压到src 目录。
# ${pkgdir} ： 打包目录： 会默认创建"pkg/包名" 目录

prepare() {
	cd "${srcdir}"
}

# 打包步骤
package() {
	# 编译源码
	cd "${srcdir}"
	make
	# 创建安装相关目录
	mkdir -p "${pkgdir}/usr/bin"
	
	#将相关文件放入对应目录
	cp xx "${pkgdir}/usr/bin"
}
```



```
有道词典：


# Maintainer: yesuu zhang <yesuu79@qq.com>

pkgname=youdao-dict
pkgver=1.1.0
pkgrel=2
pkgdesc='YouDao Dictionary'
arch=('i686' 'x86_64')
url='http://cidian.youdao.com/index-linux.html'
license=('GPL3')
depends=(
	'desktop-file-utils'
	'hicolor-icon-theme'
	'python'
	'python-pyqt5'
	'python-requests'
	'python-xlib'
	'python-pillow'
	'tesseract-data-eng'
	'tesseract-data-chi_tra'
	'tesseract-data-chi_sim'
	'python-lxml'
	'python-xdg'
	'python-webob'
	'qt5-webkit'
	'qt5-graphicaleffects'
	'qt5-quickcontrols'
)
install=youdao-dict.install
source=('youdao-arch.patch')
source_i686=('http://codown.youdao.com/cidian/linux/youdao-dict_1.1.0-0~i386.tar.gz')
source_x86_64=('http://codown.youdao.com/cidian/linux/youdao-dict_1.1.0-0~amd64.tar.gz')
sha256sums=('ab1e8cf2b38c459c60af5e47814a022ad485d2e2c0ae257ffae4c03174e703a6')
sha256sums_i686=('d1ff404f1e465d6a196b566294ddfea1a1bfe4568226201b65d74236407152fc')
sha256sums_x86_64=('5c3a5ed105238e2fad181704fd99815c4275bf546136f99e817614188794dc07')

prepare() {
	cd "${srcdir}/src"
	patch -Np2 -i "${srcdir}/youdao-arch.patch"
}

package() {
	cd "${srcdir}"
	mkdir -p "${pkgdir}/usr/bin"
	mkdir -p "${pkgdir}/usr/share/youdao-dict"
	mkdir -p "${pkgdir}/usr/share/applications"
	mkdir -p "${pkgdir}/usr/share/dbus-1/services"
	mkdir -p "${pkgdir}/usr/share/icons/hicolor/48x48/apps"
	mkdir -p "${pkgdir}/usr/share/icons/hicolor/scalable/apps"
	mkdir -p "${pkgdir}/etc/xdg/autostart"
	cp -r src/* "${pkgdir}/usr/share/youdao-dict"
	cp -r data/hicolor/* "${pkgdir}/usr/share/icons/hicolor/"
	cp data/youdao-dict.desktop "${pkgdir}/usr/share/applications/"
	cp data/youdao-dict-autostart.desktop "${pkgdir}/etc/xdg/autostart/"
	cp data/com.youdao.backend.service "${pkgdir}/usr/share/dbus-1/services/"
	chmod 755 "${pkgdir}/usr/share/youdao-dict/main.py"
	chmod 755 "${pkgdir}/usr/share/youdao-dict/youdao-dict-backend.py"
	ln -sf /usr/share/youdao-dict/main.py "${pkgdir}/usr/bin/youdao-dict"
}



```



```
解压软件包
$ tar -I zstd -xvf archive.tar.zst 
```

