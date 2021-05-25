class User:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def get_a(self):
        print(f'spells: {self.a} {self.b}')
    
    def test(self):
        print("im in")

class Wizard(User):
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def get_spell(self):
        print(f'spells: {self.c} {self.d}')

   
class Archer(User):
    def __init__(self,e,f):
        self.e = e
        self.f = f

    def get_arrows(self):
        print(f'arrows: {self.e} {self.f}')


class Knight(Wizard,Archer):
    def __init__(self, a,b,c,d,e,f):
        Archer.__init__(self,e,f)
        Wizard.__init__(self,c,d)


js = Knight(1,2,3,4,5,6)
js.get_arrows()
js.get_spell()
js.test()