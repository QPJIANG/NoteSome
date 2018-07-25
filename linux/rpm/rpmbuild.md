```
Usage: rpmbuild [OPTION...]

Build options with [ <specfile> | <tarball> | <source package> ]:
  -bp                           build through %prep (unpack sources and apply patches) from <specfile>
  -bc                           build through %build (%prep, then compile) from <specfile>
  -bi                           build through %install (%prep, %build, then install) from <specfile>
  -bl                           verify %files section from <specfile>
  -ba                           build source and binary packages from <specfile>
  -bb                           build binary package only from <specfile>
  -bs                           build source package only from <specfile>
  -tp                           build through %prep (unpack sources and apply patches) from <tarball>
  -tc                           build through %build (%prep, then compile) from <tarball>
  -ti                           build through %install (%prep, %build, then install) from <tarball>
  -ta                           build source and binary packages from <tarball>
  -tb                           build binary package only from <tarball>
  -ts                           build source package only from <tarball>
  --rebuild                     build binary package from <source package>
  --recompile                   build through %install (%prep, %build, then install) from <source package>
  --buildroot=DIRECTORY         override build root
  --clean                       remove build tree when done
  --nobuild                     do not execute any stages of the build
  --nodeps                      do not verify build dependencies
  --nodirtokens                 generate package header(s) compatible with (legacy) rpm v3 packaging
  --noclean                     do not execute %clean stage of the build
  --nocheck                     do not execute %check stage of the build
  --rmsource                    remove sources when done
  --rmspec                      remove specfile when done
  --short-circuit               skip straight to specified stage (only for c,i)
  --target=CPU-VENDOR-OS        override target platform

Common options for all rpm modes and executables:
  -D, --define='MACRO EXPR'     define MACRO with value EXPR
  --undefine=MACRO              undefine MACRO
  -E, --eval='EXPR'             print macro expansion of EXPR
  --macros=<FILE:...>           read <FILE:...> instead of default file(s)
  --noplugins                   don't enable any plugins
  --nodigest                    don't verify package digest(s)
  --nosignature                 don't verify package signature(s)
  --rcfile=<FILE:...>           read <FILE:...> instead of default file(s)
  -r, --root=ROOT               use ROOT as top level directory (default: "/")
  --dbpath=DIRECTORY            use database in DIRECTORY
  --querytags                   display known query tags
  --showrc                      display final rpmrc and macro configuration
  --quiet                       provide less detailed output
  -v, --verbose                 provide more detailed output
  --version                     print the version of rpm being used

Options implemented via popt alias/exec:
  --with=<option>               enable configure <option> for build
  --without=<option>            disable configure <option> for build
  --buildpolicy=<policy>        set buildroot <policy> (e.g. compress man pages)
  --sign                        generate GPG signature (deprecated, use command rpmsign instead)

Help options:
  -?, --help                    Show this help message
  --usage                       Display brief usage message
```

```
rpmbuild -ba 'spec文件路径'

/root/rpmbuild/SOURCES   源码存放路径
/root/rpmbuild/SPECS     spec 文件路径

打包完成会生成：/root/rpmbuild/RPMS

```

```
引用：
	https://blog.csdn.net/u012373815/article/details/73257754
	https://fedoraproject.org/wiki/How_to_create_an_RPM_package/zh-cn

xxx.spec 

Name:           hellorpm           #名字为源码tar.gz 包的名字 
Version:        1.0.0             #版本号，一定要与tar.gz包的一致哦 
Release:        1%{?dist}         #释出号，也就是第几次制作rpm 
Summary:       helloword   #软件包简介，最好不要超过50字符 

License:        GPL                   #许可，GPL还是BSD等  
URL:            #可以写一个网址 
Packager:       abel 
Source0:        %{name}-%{version}.tar.gz   
#定义用到的source，也就是你的源码

BuildRoot:      %_topdir/BUILDROOT         
#这个是软件make install 的测试安装目录.

BuildRequires:  gcc,make                           #制作过程中用到的软件包 
Requires:       python-apscheduler >= 2.1.2-1.el7,python-daemon >= 1.6-1.el7  #软件运行依赖的软件包，也可以指定最低版本如 bash >= 1.1.1 
%description                #描述，随便写                 
%prep                          ＃打包开始                    
%setup -q                      #这个作用静默模式解压并cd                               


%build              #编译制作阶段，主要目的就是编译，如果不用编译就为空 
./configure \                                     
 %{?_smp_mflags}          #make后面的意思是：如果就多处理器的话make时并行编译 

%install                        #安装阶段                        
rm -rf %{buildroot}             #先删除原来的安装的，如果你不是第一次安装的话 
 cp -rp %_topdir/BUILD/%{name}-%{version}/*  $RPM_BUILD_ROOT 
#将需要需要打包的文件从BUILD 文件夹中拷贝到BUILDROOT文件夹下。

#下面的几步pre、post、preun、postun 没必要可以不写 
%pre        #rpm安装前制行的脚本 

%post       #安装后执行的脚本 

%preun      #卸载前执行的脚本 

%postun     #卸载后执行的脚本 

%clean #清理段,删除buildroot 
rm -rf %{buildroot} 


%files  #rpm要包含的文件 
%defattr (-,root,root,-)   #设定默认权限，如果下面没有指定权限，则继承默认 
/etc/hello/word/helloword.c           #将你需要打包的文件或目录写下来

###  7.chagelog section  改变日志段 
%changelog 
```

