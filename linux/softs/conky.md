```bash
# pacman -S  conky
# pacman -S  conky-manager


conky -c <configfile>
```

conky 配置

```bash
#${image /home/ninja/Pictures/Wallpapers/icons/hacked90.png -p 70,5}

background yes
use_xft yes
xftfont Monospace:size=8
xftalpha 1.0
update_interval 3.0
update_interval_on_battery 12.0
total_run_times 0
own_window yes
own_window_type normal
own_window_transparent no
own_window_class conky-semi
own_window_hints undecorated,below,sticky,skip_taskbar,skip_pager
own_window_argb_visual yes
own_window_argb_value 0
double_buffer yes
format_human_readable yes
short_units yes
minimum_size 240 5
maximum_width 3500
default_bar_size 0 9
draw_shades no
draw_outline no
draw_borders no
draw_graph_borders yes
default_color green
default_shade_color FF0000
default_shade_color1 181717
default_outline_color 0000ff
alignment top_right
gap_x 58
gap_y 20
no_buffers yes
uppercase no
cpu_avg_samples 2
pad_percents 0
override_utf8_locale no

color1 EF5A29
color2 DF6C0A
color3 EF5A2F
color4 EF5A29


own_window_colour 000000
TEXT

${font Monospace Regular:size=9}${color green}Base ${color1} ${hr 2}
${color3}$font$sysname  $kernel  $alignr  $machine
Uptime $alignr${uptime}
File System $alignr${fs_type}

${font Monospace Regular:size=9}${color green}NETWORK ${color1}${hr 2}
${color3}
Internal IP:${alignr}${addr enp0s25 }
Download:${alignr}${downspeed enp0s25 }
${downspeedgraph enp0s25  FFEF00 } 
${upspeedgraph enp0s25  FFEF00 }
Upload:${alignr}${upspeed enp0s25 }

${font Monospace Regular:size=9}${color green}CPU  ${color1}${hr 2}
${color3}
CPU TOTAL USAGE:$alignr${cpu cpu0}%
${cpubar cpu0}
CPU1:  $alignr${cpu cpu1}%
${cpubar cpu1}
CPU2:  $alignr${cpu cpu2}%
${cpubar cpu2}
CPU3:  $alignr${cpu cpu3}%
${cpubar cpu3}
CPU4:$alignr${cpu cpu4}% 
${cpubar cpu4}

${font Monospace Regular:size=9}${color green}RAM ${color1}${hr 2}
${color3}
RAM: ${alignc}$mem / $memmax $alignr ${memperc}%
$membar
SWAP $alignc ${swap} / ${swapmax} $alignr ${swapperc}%
${swapbar}

${font Monospace Regular:size=9}${color green}DISK ${color1}${hr 2}
${color3}
/: ${alignr}${fs_used /} / ${fs_size /}
${fs_bar /}
/home: ${alignr}${fs_used /home} / ${fs_size  /home} 
${fs_bar /home}
/data: ${alignr}${fs_used /data} / ${fs_size  /data} 
${fs_bar /data}
/disk/1: ${alignr}${fs_used /disk/1} / ${fs_size  /disk/1} 
${fs_bar /disk/1}
/disk/2: ${alignr}${fs_used /disk/2} / ${fs_size  /disk/2} 
${fs_bar /disk/2}

${font Monospace Regular:size=9}${color green}PROCESSORS CPU ${color1}${hr 2}
${color3}
${top name 1} $alignr ${top pid 1} ${top cpu 1}%
${top name 2} $alignr ${top pid 2} ${top cpu 2}%
${top name 3} $alignr ${top pid 3} ${top cpu 3}%
${top name 4} $alignr ${top pid 4} ${top cpu 4}%
${top name 5} $alignr ${top pid 5} ${top cpu 5}%
${hr 2}

${font Monospace Regular:size=9}${color green}PROCESSORS RAM ${color1}${hr 2}
${color3}
${top_mem name 1} $alignr  ${top pid 1}  ${top_mem mem_res 1}
${top_mem name 2} $alignr  ${top pid 2}  ${top_mem mem_res 2}
${top_mem name 3} $alignr  ${top pid 3}  ${top_mem mem_res 3}
${top_mem name 4} $alignr  ${top pid 4}  ${top_mem mem_res 4}
${top_mem name 5} $alignr  ${top pid 5}  ${top_mem mem_res 5}
${hr 2}



```

```
# cpu 额定频率
${freq_g cpu0}
${freq_g cpu2}
......

# 系统名
$sysname  
# 内核版本
$kernel
# arch
$machine
# 开机时长
${uptime}
# ip
${addr <网卡名> }
# 下载速度
${downspeed <网卡名> }
# 上次速度
${upspeed <网卡名> }
# 网速图
${downspeedgraph <网卡名>  FFEF00 } 
${upspeedgraph <网卡名>  FFEF00 }
# 单 cpu 利用率，编号0： 整体值，单个cpu编号从1 开始
${cpu cpu0}%
${cpu cpu1}%
....
${cpubar cpu0}
${cpubar cpu1}
.....
# 当前cpu 频率 ，编号从1 开始
${freq_g (1)}GHz 
${freq_g (2)}GHz 
....
# cpu 图：编号0： 整体值，单个cpu编号从1 开始
${cpugraph cpu0 100,300}

#已使用内存
${mem}
# 总内存
$memmax
# 内存利用率
${memperc}%

$memmax
# 内存使用bar
${membar 5,}
# top cpu
${top name 1} $alignr ${top pid 1} ${top cpu 1}%
# top ram
${top_mem name 1} $alignr  ${top pid 1}  ${top_mem mem_res 1}
```

