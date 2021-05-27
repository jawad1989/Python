* you can initialize list of objects:
```
shapes = [Rectangle(6, 10), Circle(7)]
```
* Class variable
* Instance variable
* Methods  
A method is a group of statements that performs some operations and may or may not return a result.
    * Instance methods
    * Class methods
    * Static methods
* Method Overloading  
Overloading refers to making a method perform different operations based on the nature of its arguments.
```
def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b) 
        print("c =", c)
        print("d =", d)
        print("e =", e)
```
* class methods  
Class methods are accessed using the class name and can be accessed without creating a class object. Decorator @classmethod and cls is used
```
    @classmethod
    def add_numbers(cls, num1, num2):
        # return num1+num2 # with cls param
        return cls('Jawad', num1+num2)
```

* Static Methods  
Static methods can be accessed using the class name or the object name. Decorator @staticmethod is used.  
Used as utility function inside the class or when we do not want the inherited classes.

* Access modifiers:  
Public or Private, they can impose access restrictions on different data members and member functions.  
Private members use the double underscore "__ prefix"  
```
private method def __im_private()
private var  self.__a = a
```

* Information Hiding  
    * Encapsulation: Encapsulation in OOP refers to binding the data and the methods to manipulate that data together in a single unit, that is, class.  
    * Abstraction

* Inheritance:   
    * square is a shape  
    * Existing/Parent/Super class(shape) -> Derived/Child/Sub Class(Square)  
    * In Python, whenever we create a class, it is, by default, a subclass of built-in Python object class  
    * super(): It is used in a child class to refer to the parent class without explicitly naming it
    * Types:  
        Single  
        Multi-level: child, father, grand-father  
        Hierarchical: 2 child 1 father  
        Multiple: 2 parents 1 child  
        Hybrid: vehicle-> Normal,Electic -> hybirdcar

* Polymorphism:  
Is a combination of two Greek words, Poly meaning many and Morph meaning forms. 
    * Duck Typing: polymorphism without inheritance,  If an object quacks like a duck, swims like a duck, eats like a duck or in short, acts like a duck, that object is a duck, extends concept of dynamic typing: Dynamic typing means we can change the type of an object later in the code.  
    * OverRiding: Method overriding is the process of redefining a parent class’s method in a subclass.  
    * OverLoading:
```
 +	__add__ (self, other)
-	__sub__ (self, other)
/	__truediv__ (self, other)
*	__mul__ (self, other)
<	__lt__ (self, other)
>	__gt__ (self, other)
==	__eq__ (self, other)
```  

    *  Abstract Base Classes, or ABC: define a set of methods and properties that a class must implement in order to be considered a duck-type instance of that class. Methods with @abstractmethod decorators must be defined the child class
```
from abc import ABC, abstractmethod

class ParentClass(ABC):

    @abstractmethod
    def method(self)
```

* Class Relationship:  
1) IS A
2) Part Of
3) Has A: Class A and class B have a has-a relationship if one or both need the other’s object to perform an operation, but both class objects can exist independently of each other   
Since Python compiles from top to bottom, make sure you have defined the class before creating an object of that class.

* Association: association is the common term for both the has-a and part-of relationships but is not limited to these.  

* Aggregation:  
Aggregation follows the Has-A model. This creates a parent-child relationship between two classes, with one class owning the object of another.  
In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner.  
In aggregation, the parent only contains a reference to the child, which removes the child’s dependency.

* Composition: Part-Of, A class which creates the object of the other class is known as the owner and is responsible for the lifetime of that object.  
the lifetime of the owned object depends on the lifetime of the owner.  
A car is composed of an engine, tires, and doors. In this case, a Car owned these objects, so a Car is an Owner class and tires, doors, and engine classes are Owned classes.