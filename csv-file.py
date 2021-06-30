import csv


names =[['fred',10],['john',5],['bill',7]]

with open('names.csv','w') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(['name','number'])
	for name in names:
		csv_writer.writerow(name)

# by individual row
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])


# customer delimiters

data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)

#reading a csv
#treat it like a generator getting each row in turn
import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
	
	#Custom delimiters
	
	import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)
        
        
