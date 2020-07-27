import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i=input('enter start to or stop to stop recording')
    if i=='start':
        s.sendall(b'0')
        data = s.recv(1024)
        print('recording started') 
    elif i=='stop':
        s.sendall(b'1')
        data = s.recv(1024)    
        print ("recording stopped")
print('Received', repr(data))
