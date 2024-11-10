# bandit.labs.overthewire.org
# bandit0
# 2220
#


mantissa_string = '@bandit.labs.overthewire.org -p 2220'

with open('bandit.txt', 'w') as file:
	for i in range(32):
		line = 'bandit'+str(i)+mantissa_string+'\n'
		file.write(line)
			    
	

