import numpy as np
import cv2
import os
from time import *
import socket
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
i=2 

    
ltime=asctime(localtime(time()))
ltime=ltime.replace(" ", "")
ltime=ltime.replace(":","")
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname) 
vcap = cv2.VideoCapture("rtsp://"+str(ip)+":8554/", cv2.CAP_FFMPEG)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
killme=ltime
out = cv2.VideoWriter(str(killme)+'tmc.avi',fourcc, 20.0, (640,480))
while(vcap.isOpened()):    
    ret, frame = vcap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        print('started recording')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        file1 = open("myfile.txt","r+")
        s=file1.read() 
        file1.close()
        print(s)
    if str(s) =="ok "  :
        print('recording stopped')
        vcap.release()
        out.release()
        cv2.destroyAllWindows()  
        file1 = open("myfile.txt","w")
        file1.write("Hello")
        file1.close()
        print("mkc")
        break      
    print("lololololol")
    # Release everything if job is finished
    