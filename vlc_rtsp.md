# To Creat rtsp stream of webcam using vlc media player

1.select the file option on vlc player taskbar

2.select stream option.

3.select capture device and choose /dev/video0 as video device name

4.select stream and select v4l2:///dev/video0 as source in next menu and press next

5.in next menu (destination setup) select rtsp  ,press add and select port 8554 if you don't want to change code .If you can change rtsp link in the code
(details in README.md) choose whichever you want.

6.set profile as Video - H.265 + MP3 (MP4) and next 

7.Press stream to start your stream


