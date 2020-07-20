from subprocess import *
from time import *
i=1 
while i>0:
	print("enter 1 for recording, 2 to stop")
	j=input("enter no")
	if int(j)==1: 
		script='python3 1.py &'
		Popen(script,shell=True)
	elif int(j)==2:
		script1='python3 stoprec.py &'
		Popen(script1,shell=True)
