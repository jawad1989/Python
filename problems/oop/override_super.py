class Shape:
    def __init__(self, sname) -> None:
        self.sname = "Shape"
    
    def getName(self):
        return self.sname

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + ", " + self.xsname)


circle = XShape("Circle");
print(circle.getName())