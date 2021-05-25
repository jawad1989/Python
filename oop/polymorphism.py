# is the ability (in programming) to present the same interface for differing underlying forms (data types).
# in Python: object classes can share the same method name

class User():
    def sign_in(self):
        self.user_name = 'jawad'

    def attack(self):
        print('in user attack')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: {self.num_arrows}")


# intances
wizard1 = Wizard('jawad', 90)
archer1 = Archer('Robin', 40)

wizard1.attack()
archer1.attack()


for char in [wizard1, archer1]:
    char.attack()
