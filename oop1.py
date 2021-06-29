# A simple class framework

class Instructors:
    '''Instructor class _ Im a docstring holding information printed with help'''
    
    # Variables
    companyName = 'Capstan Blue'
    
    def __init__(self,course = 'Null'):
        
        self.course = course
    def printname(self):
        print(self.course)
        
        
    def printinfo(self):
        print('My company name is ', Instructors.companyName)

elearning = Instructors('testcourse')
help(Instructors)
print(type(elearning)) # get type
elearning.printname()
print(elearning.course)
