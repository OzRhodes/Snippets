# Encapsulation
# 
class Cars:
    
    def __init__(self,speed, color):
        
        self.__speed = speed
        self.__color = color
        
    def set_speed(self,speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed

ford = Cars(250, 'green')
nissan = Cars(300, 'red')
toyota = Cars(180, 'blue')

# without encapsulation we can access speed variable directly - bad
# change speed to __speed from speed
ford.speed = 500  # no longer works but does set a speed value
print(ford.speed) # but does create and set a new speed value

print(ford.get_speed())
ford.set_speed(600)
print(ford.get_speed())




