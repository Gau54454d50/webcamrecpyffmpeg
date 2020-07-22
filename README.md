# webcamrecpyffmpeg

requirements:vlc media player 

record webcam or any other rtsp stream  with timestamp using ffmpeg and python (linux)

server-client interface update

1. start rtsp stream using vlc media player at  rtsp://localhost:8554/ (see vlc_rtsp.md).If you want to record other rtsp stream paste its link in rec.py in place of preceding link.
     
2. run python3 recserver.py 
      
#recieves command from client to start and stop recording

3. run python3 client.py (in different terminal after step 1)

#gives command to server to start and stop recording



