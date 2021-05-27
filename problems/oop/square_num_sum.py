class Point():
    def __init__(self, x, y, z) -> None:
        self.x,self.y,self.z = x,y,z
    
    def sqSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2 


p = Point(1,3,5)
print(p.sqSum())

