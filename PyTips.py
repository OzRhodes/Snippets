'''
### Std Approach

def main():
	print("Hello World!")


if __name__ == "__main()__"
	main()

###########


# enumerate

names=['tom','dick','harry','oz']

for index,name in enumerate(names):
	print (index,name)
	
# ternary

condition = True

x = 1 if condition else 0

print(x)

# underscores in numbers for easy reading
print(100_000_000)
# 100000000

#context manager to manage resources
#files, db, threads, sockets

with open('file.txt', 'r') as file:
	file_contents = file.read()


#zip
first_names=['tom','dick','harry','oz']
last_names =['smith','jones','watts','rhodes']

for first,last in zip(first_names, last_names):
	print(first + ' ' + last)
	

#unpacking

item =(1,2)

a,b = item

print(a,b)

## _ is an empty variable
a, _ = (3,4)

print(a)

item2 = (1,2,3,4,5,6)

a,b, *c = item2

print(a,b,c)

a,b, *c, d = item2
print(a,b,c,d)


#setattr, getattr
# dynamically add to a class
class Person():
	pass

person = Person()

first_key = 'first'
first_val = 'Oz'

setattr(person, first_key, first_val)

first = getattr(person, first_key)
print(person.first)
print(first)


# type hidden words eg password NOT Pythonista
from getpass import getpass 
username = input('Enter Username: ')
password = getpass('Enter Password: ')

print(username, password)


#python -m
python -m venv venv
# runs the module


# help(module)
# dir(module)
'''
