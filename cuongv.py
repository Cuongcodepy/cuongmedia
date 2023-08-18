import time
import random
import os,sys

def cuong():
	  a="\033[1;91m=\033[1;97m="*30
	  for i in range(len(a)):
	    sys.stdout.write(a[i])
	    sys.stdout.flush()
	    time.sleep(0.001)
def taixiu():	    
	  a=input("\033[1;94m[ tài ] --- \033[1;95m[ xỉu ] :")
	  os.system('clear')
	  print ("           bản quyền thuộc: m.fb/cuongvipfb.pro")
	  cuong()
	  nn=random.randint(3,18)
	  print ("             [ tài ]-----(", nn, ")------[ xỉu ]")
	  cuong()
	  if nn>10:
	  	k='tai'
	  	if a==k:
	  		print("\033[1;94m              [ tài ]", nn, "bạn thắng ")
	  	else:
	  		print ("\033[1;94m             [ tài ]", nn, "bạn thua ")
	  else:
	  	if nn<10:
	  		k1='xiu'
	  		if a==k1:
	  			print("\033[1;94m               [ xỉu ]", nn, "bạn thắng")
	  		else:
	  			print("\033[1;94m              [ xỉu ]", nn, "bạn thua")

def phien():
		  for io in range(-20,0):
		  	print("\033[1;91m█", str(io), "giây để bắt đầu phiên mới", end='\r')
		  	time.sleep(0.2)
		  	print("\033[1;92m█", str(io), "giây để bắt đầu phiên mới", end='\r')
		  	time.sleep(0.2)
		  	print("\033[1;93m█", str(io), "giây để bắt đầu phiên mới", end='\r')
		  	time.sleep(0.2)
while True:
	cuong()
	taixiu()
	phien()