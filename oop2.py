# A simple class framework inheritance
#polymorphic area method

import math

class Shape:
    
    def __init__(self,measure):
        
        self.measure = measure
    def area(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
        
    #polymorphic area
    def area(self):
        return math.pi * self.radius**2




class Rectangle(Shape):
    
    def __init__(self, length = 1, width = 1):
        
        self.width = width
        self.length = length
    #polymorphic area
    def area(self):
        return self.width * self.length
    

c1=Circle(1)
print(c1.area())
r1 = Rectangle(2,3)
print(r1.area())