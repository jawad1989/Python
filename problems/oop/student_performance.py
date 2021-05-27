class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy  = phy
        self.chem = chem
        self.bio  = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def Percentage(self):
        p = (self.totalObtained()/300)*100
        return float(p)

std = Student('Mark', 80, 90, 40)
print(std.Percentage())