import os, fnmatch

def findReplace(directory, find, replace, filePattern):
	for path, dirs, files in os.walk(os.path.abspath(directory)):
		for filename in fnmatch.filter(files, filePattern):
			filepath = os.path.join(path, filename)
			with open(filepath, "r") as f:
				s = f.read()
				s = s.replace(find, replace)
				with open(filepath, "w") as f:
					f.write(s)
                
findReplace("some_dir", "find this", "replace with this", "*.flietype")
