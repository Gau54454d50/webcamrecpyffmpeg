from subprocess import *
i=1
while i>0:
    script='python3 client.py &'
    Popen(script,shell=True)