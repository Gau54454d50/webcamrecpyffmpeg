from subprocess import *
from time import *

localtime=asctime(localtime(time()))
localtime=localtime.replace(" ", "")
localtime=localtime.replace(":","")
command='ffmpeg -i rtsp://localhost:8554/ -s 1280x720 -codec:v mpeg4 -acodec copy '+str(localtime)+'video.avi'
Popen(command,shell=True)
print("recording")	


