class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(self.fname, self.lname)

class Pilot(Person):
    
    def __init__(self, fname, lname, aircraft_type):
        self.fname = fname
        self.lname = lname
        self.aircraft_type = aircraft_type
    
    def print_type(self):
        print(self.aircraft_type)




p1 = Person('Tom','Smith')
p1.print_name()

p2 = Pilot('Mark', 'Mcd','Seaking')
p2.print_name()
p2.print_type()