import socket
from subprocess import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
i=2
while i>0:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))

            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data) 
                    print(data)
                    j=data
    
            if int(j)==0: 
		            script='python3 newrecord.py &'
		            Popen(script,shell=True)
	        
            if int(j)==1:
		            script1='python3 newstoprec.py &'
		            Popen(script1,shell=True)