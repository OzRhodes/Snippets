# json snippets

import json

json_str = '{"name": "Bob", "languages": ["Python", "Java"]}'


person = '{"name": "Bob", "languages": ["English", "French"]}'

# load from string. json.loads

person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}

print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

# from file json.load

import json

with open('path_to_file/person.json') as f:
  data = json.load(f)
  

# Convert dict to json

import json

person_dict = {
	'name': 'Bob', 
	'age': 12, 
	'children': None
	}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)


#writing json to a file

import json

person_dict = {
	"name": "Bob",
	"languages": ["English", "Fench"],
	"married": True,
	"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
  
  
#printing json in a pretty format with indents and sorted keys
import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))
