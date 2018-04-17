###  Edit : /boot/grub/grub.cfg add the follow text for theme

    insmod gfxmenu
    loadfont ($root)/boot/grub/themes/Vimix/unifont-regular-16.pf2
    insmod png
    set theme=($root)/boot/grub/themes/Vimix/theme.txt
    export theme


    befere edit the conf: copy the theme dir to /boot/grub/themes.
    
    file tree:

    /boot/grub/themes $ tree -L 1
    .
    ├── arch-silence
    ├── arch-silence-master.zip
    ├── aurora
    ├── Aurora-Penguinis-GRUB2.tar.gz
    └── Vimix


### Edit : /boot/grub/grub.cfg remove submenu and uselss menuentry for os selectsd