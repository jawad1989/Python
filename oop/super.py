
class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        self.user_name = 'jawad'

    def attack(self):
        print('in user attack')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self,email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


# intances
wizard1 = Wizard('jawad', 90,"jawad@gmail.com")
print(wizard1.email)

