"""
Encapsulation :  Its one of the fundaments of OOPS concept.it describes idea
wrapping data and the methods to work on the data with one unit and we put the
restriction accessing the variables and methods directly to prevent the modification
of data.For this purpose ww will make Variables as Private and Protected Members

Abstraction:
The process of hiding the internal functionality of a function from the users.The
user only interact with basic implementation of function, but inner working is hidden.
User familiar with "What function does" but he don't know "How it does"

Abstract Method:
Sometime we don't know about implementation, still we declare a method. Such type
of methods we call it has abstract method. Abstract method is having only declaration
but not the implementation.

We can declare abstract method in Python with @abstractmethod decorator

@abstractmethod
def m1(self): pass

@abstractmethod is present inside abc module, Hence compulsory we should import
abc module, otherwise we will get error
"""
#EX 1 ====> We will get Errror
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass

#Ex 2===>
# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass

#Ex 3
# from abc import *
# class Fruit:
#     @abstractmethod
#     def taste(self):
#         pass

#Abstract class
"""
Sometimes implementation of class in incomplete, such type of partially implemented
classes are called abstract classes.
Every abstract class in python should be derived from ABC class which is present in abc module.
"""
# #Case 1
# from abc import *
# class Test :
#     pass
#
# t=Test()
#
# #Case 2
# from abc import *
# class Test(ABC) :
#     pass
#
# t1=Test()

#Case3
# from abc import *
# class Test(ABC) :
#     @abstractmethod
#     def m1(self):pass
#
# t2=Test()
#Can't instantiate abstract class Test without an implementation for abstract method 'm1'
#Case 4
from abc import *
class Test() :
    @abstractmethod
    def m1(self):print("Hello")

t3=Test()
t3.m1()

"""
Conslusion : if a class contains atleast one abstract method and if we are
            extending ABC class then instantiation(Object Creation) not possible

abstract class with abstract method instantiation is not possible

Parent class abstract method should be implemented in child class.otherwise we can't
instantiation is not possible in child class.if you try to create child class object
you will get error

"""
from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass


class Bus(Vehicle):
    def noofwheels(self):
        return 6

b=Bus()
print(b.noofwheels())

class Auto(Vehicle):
    def noofwheels(self):
        return 3

a=Auto()
print(a.noofwheels())

#Abstract class can contain both abstract method and non-abstract method
"""
Interface : 
In general if abstract class contains only abstract methods such type of abstract class
is considered as interface
"""
from abc import *
class DBInterface(ABC):

    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass


class Oracle(DBInterface):
    def connect(self):
        print("Connecting to Oracle Database")

    def disconnect(self):
        print("Disconnecting to Oracle Database")

class MySQL(DBInterface):
    def connect(self):
        print("Connecting to MySQL Database")

    def disconnect(self):
        print("Disconnecting to MySQL Database")

o=Oracle()
o.connect()
o.disconnect()
# dbname=input("Enter the Database Name")
# classname=globals()[dbname]
# x=classname()
# x.connect()
# x.disconnect()

"""
# Concrete class Vs Abstract class Vs Interface
1.If we don't know anything about implementation just we have requirement specification
    then we should go for interface

2. If we are talking about implementation but completely then we should go for 
    abstract class (Partially implemented class)

3. If we are talking about implementation completely and ready to provide service
    which is required.Then we should go for concrete class

"""
from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass

    @abstractmethod
    def m2(self): pass

    @abstractmethod
    def m3(self): pass

class Abscls(CollegeAutomation):
    def m1(self):print("M1 Method Implementation")

    def m2(self):print("M2 Method Implementation")

class Concrete(Abscls):
    def m3(self):print("M3 Method Implementation")

c=Concrete()
c.m1()
c.m2()
c.m3()

#Public , Protected, Private attributes(Variables):
#==> This is a public variable we can access anywhere within the class and outside of a class.
x="QACircle"

"""
Protected Variable can be accessed within the class anywhere but
from outside class only in child class. Protected variable should be specified
or Prefixed with _ symbol 
Syntax = _Variablename=Value
_name="QACircle" 
"""

"""
Private Variables can be accessed only within the class. From outside of a class
we can't access. We can declare private variable explicitly by prefixing 
2 underscore Symbols

Syntax: __Variablename=Value
__name="QACircle"
"""
class Test:
    x=10
    _y=20
    __z=30
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

t1=Test()
t1.m1()
print(Test.x)
print(Test._y)
#print(Test.__z)

# How access Private Variable from outside of class
#indirectly way of accessing objectreference._classname__variablename
print(t1._Test__z)

"""
String Overriding
1. __str__() Method 
2.Whenever we are printing Object Reference Variable internally 
__str__() method will be called which is returning string the 
following format : <__main__.Student object at 0x000001825B4522D0>
3. TO return meaningful string representation we have to Overrid __str__() Method
"""
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
        return f'This is Student with name:{self.name} and RollNo:{self.rollno}'

s1=Student("Diskshita","10")
print(s1)