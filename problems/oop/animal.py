class Animal:
    
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound
   
    def Animal_details(self):
        print("Name: ", self.name)
        print("Sound: ", self.sound)
        


class Dog(Animal):
   
    def __init__(self, name, sound, family) -> None:
        super().__init__(name, sound)
        self.family = family
    
    def Animal_details(self):
        super().Animal_details()
        print("Family: ",self.family)


class Sheep(Animal):

    def __init__(self , name, sound, color) -> None:
        super().__init__(name, sound)
        self.color = color
   
    def Animal_details(self):
        super().Animal_details()
        print("Color: ",self.color)


# code to test your implementation
# uncomment this code when you want to test your implementation

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print("")

s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()

print("Write your solution in the classes above.")

