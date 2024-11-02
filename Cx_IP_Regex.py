#
import re

def Validate_It(IP):
 
    # Regex expression for validating IPv4
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
	

    p = re.compile(regex)
	
    # Checking if it is a valid IPv4 addresses
    if (re.search(p, IP)):
        return "Valid IP"
 	
    # Return Invalid
    return "Invalid IP"
 

 
 
def main():
# IP addresses to validate
	IP = "254.120.223.13"
	print(Validate_It(IP))
 
	IP = "0.0.1.400"
	print(Validate_It(IP))

if __name__ == '__main__':
	main()
