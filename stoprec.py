from subprocess import *
kill=['killall -9 ffmpeg']
Popen(kill,shell=True)
print("recording stoped") 
restart=['python3 process.py']
Popen(restart,shell=True) 
