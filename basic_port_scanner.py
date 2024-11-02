
import sys
import socket
from datetime import datetime

# Our target from the command line when the code is run

if len(sys.argv) ==2:
	HOST = sys.argv[1]
	
	
else: 
	print('Invalid arguments...')
	print('Syntax is python3 portscan.py <IPAddr>')
	exit(0)
	
	
# BANNER TO ALERT USER OF ACTIVITY

print('+' * 50)
print('Scanning target: ' + HOST)
print('Started: ' + str(datetime.now()))
print('+' * 50)

#SCANNING PORTS IN RANGE 
#reduced for testing

try:
	for port in range(50,80):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		output = s.connect_ex((HOST,port))
		if output == 0:   #0 - open, 1 - closed
			print(f'Port: {port} is open')
		s.close()
		
except KeyboardInterrupt:
		print('Exiting...KB')
		sys.exit()

except socket.gaierror:
		print('Exiting...DATA')
		sys.exit()
		
except socket.error:
		print('Exiting...Sock Err')
		sys.exit()
	
