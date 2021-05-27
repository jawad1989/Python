class Player:
    teamName = 'Liverpool'  # class variables
    name = 'Jawad'

    def __init__(self, n):
        self.n = n  # creating instance variables
        self.name = n

    def get_team(self):
        return self.name

    def get_team(self,a):
        return 2 + a

    def get_team(self, a, b):
        return 2 + a + b

p1 = Player('Mark')
# print(p1.get_team())
# print(p1.get_team(4))
print(p1.get_team(4,5))
print(Player.name)


# Example 2
class Parent:
    def prn(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        self.a = Parent()

    def prn(self):
        print("Child")


temp = Child()
temp.a.prn()