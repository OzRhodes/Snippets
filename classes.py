import math

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
         
    def area(self):
        if self.width >0 and self.length >0:
            return self.length * self.width
        
        

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        if self.radius >0:
            return (math.pi)**2 * self.radius


r1 = Rectangle(1,1)
c1 = Circle (1)

print(r1.area())
print(c1.area())
