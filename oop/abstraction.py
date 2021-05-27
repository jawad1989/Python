# hiding/extracting information and giving access to what is necessary
# e.g. .count() , len() => we only care about the result not how its built

from abc import ABC, abstractmethod


class ParentClass(ABC):

    @abstractmethod
    def method(self):
        # print('parent')
        pass


class Child(ParentClass):
    def __init__(self, name) -> None:
        self.name = name
      
    def method(self):
        # return super().method()
        print('child')

c = Child('jawad')
c.method()