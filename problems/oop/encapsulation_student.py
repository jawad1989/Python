class Student:
    def setName(self, name):
        self.__name   = name
        
    def getName(self):
        return self.__name
    
    def setRollNumber(self,r):
        self.__RollNumber = r

    def getRollNumber(self):
        return self.__RollNumber
    
s1 = Student()
s1.setName('Mark')
s1.setRollNumber(100)
print(s1.getName())
print(s1.getRollNumber())