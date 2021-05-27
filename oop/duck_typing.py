class Dog():
    def speak(self):
        print("woof")

class Cat():
    def speak(self):
        print("Meow")

class Animal():
    def Sound(self, animal):
        animal.speak()


d = Dog()
c = Cat()
a = Animal()

a.Sound(d)
a.Sound(c)
