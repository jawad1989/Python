# python doesnt has a private keyword
# if we want to make a variable private we add _ before variable as a convention
# self._name
# self._age

class TestPrivate():
    name = 'jawad_saleem'
    ID = 100
    
    def __init__(self,b,c) -> None:
        self.b = b
        self.__c = c

    def get_c(self):
        return self.__c
    
    def get_id(self):
        return self.ID

    def __im_private(self):
        return self.name

    def test(self):
        return 'test'

    def test_private(self):
        # return self.test()
        return self.__im_private()
        # return self.name


D = TestPrivate(3,4)
print("Accessing Private Attributes in the Main Code: ", D._TestPrivate__c)
print("accessing class var from method: ",D.get_id())

print("Accessing private method from public function: ",D.test_private())
# print(D.b)
print("accessing private var from public method: ",D.get_c())
# print(D.__c)
# print(D.ID)
# print(D.test_private())