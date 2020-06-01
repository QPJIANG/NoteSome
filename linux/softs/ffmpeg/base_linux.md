Linux
```
查看设备：
ffmpeg -hide_banner -devices

D: 输入设备
E: 输出设备



查看设备支持的参数
 ffmpeg -h demuxer=<设备>
 ffmpeg -h demuxer=fbdev
 
 设备说明：
 	x11grab： 屏幕输出
 
 
 
 屏幕录制：
 ffmpeg -f x11grab -framerate 30 -video_size 1024*800 -i :0.0 out.mp4
 
 -i :0.0+300,200    
 	:0.0  display 号： 可通过echo $DISPLAY 获得。
 	300		开始坐标x
 	200		开始坐标y
```

