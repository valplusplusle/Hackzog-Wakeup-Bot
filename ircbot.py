import os
import time
import subprocess

#Testing the internet and kill the bot if connection is down and start when up

hostname = "www.google.de" #example
x=1

while 1:
	response = os.system("ping -c 1 " + hostname)
	#and then check the response...
	if response == 0:
		print hostname, 'is up!'
		if x == 1:
			subp = subprocess.Popen('python /home/pi/wakeupbot/ircbotstart.py', shell=True)
			x = 0
	else:
		print hostname, 'is down!'
		subp.kill()
		time.sleep(30)
		x = 1
	time.sleep(10)	
