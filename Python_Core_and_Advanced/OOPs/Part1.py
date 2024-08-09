# # class Student:
# #     """This is a Student class with required data"""
# #
# #     def m1(self):
# #         print("Hello")
# #
# # print(Student.__doc__)
# # help(Student)
# # s1=Student()
# # s2=Student()
# # s3=Student()
# # print(id(s1),id(s2),id(s3))
#
# #What is Object
# """
# Physical existence of a class is nothing but Object.
# We can create any number of Objects for class
#
# Syntax : referenceVariable=classname()
#
# """
#
# #Types of Variables are Available
# """
# 1.Instance Variables(Object Level Variables)
# 2.Static Variable(Class Level Variables)
# 3.Local Variables(Method Level Variables)
#
# """
# #Types of Methods which are available in the Python.
# """
# 1.Instance Method
# 2.Class Method
# 3.Static Method
# """
#
# # What is Reference Variable :
# # The Variable which can be used to refer an Object is called reference Variable
#
# class Student:
#
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.marks=marks
#         self.rollno=rollno
#
#     def talk(self):
#         print("Hello my name is :",self.name)
#         print("My rollno is:",self.rollno)
#         print("My Marks are :",self.marks)
#
#
#
# s=Student("Girish",121,80)
# s2=Student("Amogh",420,35)
# s.talk()
# print(s.name,s.rollno,s.marks)
# s2.talk()
# print(s2.name,s2.rollno,s2.marks)
#
# #Self Variable ==>
# """
# self is the default variable which is always pointing to the current object(like this keyword in Java)
# By using this self variable we can access instance variables and instance methods of Object
#
# Note:
# 1. self should be first parameter inside the constructor
#     def __init__(self):
# 2.self should be first parameter inside the instance method
#     def talk(self)
# """
#
# #Constructor Concept:
# """"
# 1. Constructor its a special method in Python
# 2. The name of a constructor always should be __init__(self)
# 3.Constructor will be executed automatically at the time of object creation
# 4.The main purpose of constructor is to declare and initialize instance variables
# 5.Per Object Constructor will be executed only once
# 6. Constructor can take at least one argument(at least self)
# 7. Constructor is optional and if we are not providing any constructor then python
#     ===> will create default constructor internally
#
#
# """
# #Example 1:
# class Test:
#
#     def __init__(self):
#         print("Constructor is executed")
#
#     def m1(self):
#         print("Method is executing")
#
# t=Test()
# t.m1()
# t.m1()
# t.m1()
# t1=Test()
# t2=Test()
# t3=Test()
#
# #Example 2:
# class Student:
#
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.marks=marks
#         self.rollno=roll
#
#     def display(self):
#         print("Student name is : {}\nRollNo is : {}\nMarks are :{}".format(self.name,self.rollno,self.marks))
#         self.z=100
#
# s=Student("Girish",121,80)
# s.display()
# print(s.z)
# s.d=200
# print(s.d)

#What is the difference between Method and Constructor

#Types of Variables are Available
"""
1.Instance Variables(Object Level Variables)
2.Static Variable(Class Level Variables)
3.Local Variables(Method Level Variables) 

"""
import sys

# Where we can declare instance Variables
"""
1. inside a constructor by using self variable
2. Inside instance method using self Variable
3.Outside of class using object reference variable

"""
# class Student:
#
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.marks=marks
#         self.rollno=roll
#
#     def display(self):
#         print("Student name is : {}\nRollNo is : {}\nMarks are :{}".format(self.name,self.rollno,self.marks))
#         self.z=100
#
# s=Student("Girish",121,80)
# s.display()
# print(s.z)
# s.d=200
# print(s.d)

# How to delete instance variable
"""
Within the class 
del self.variableName

Outside a class
del objectreference.variableName

"""
# class Student:
#       x=100
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.marks=marks
#         self.rollno=roll
#         #del self.rollno
#
#     def display(self):
#         print("Student name is : {}\nRollNo is : {}\nMarks are :{}".format(self.name,self.rollno,self.marks))
#         self.z=100
#
# s=Student("Girish",121,80)
# s.display()
# print(s.z)
# s.d=200
# del s.d
# print(s.d)

#Static Variable :
"""
1. If the value of a variable is not varied from object to object, 
    Such type of variables we call it has Static Variable
2. We have to declare within a class directly but outside of Methods.
3. For the total class only one copy of static variable will be created and shared
    ==>by all the objects 
4. We can access the static Variable either by class name or by Object Reference.
    But recommended to to use class Name.
"""
# class Test:
#     x=10
#
#     def __init__(self):
#         self.y=100
#
# t1=Test()
# t2=Test()
#
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# Test.x=899
# t1.y=999
# print(t1.x,t1.y)
# print(t2.x,t2.y)

#Where i can declare and intialize static Variable :
"""
1. In general directly within a class but outside of any methods
2. Inside a constructor by using class name
3. Inside instance method by using class name
4. Inside class method by using class name/cls Variable 
5. Inside static method by using class name 
"""
# class Test:
#     x=10
#
#     def __init__(self):
#         self.y=100
#         Test.b=2000
#
#     def m1(self):
#         Test.c=3000
#         print(Test.x)
#
#     @classmethod
#     def m2(cls):
#         cls.d=4000
#         Test.e=5000
#         del Test.e
#     @staticmethod
#     def m3():
#         Test.f=6000
#
# print(Test.__dict__)
# t=Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# t.m2()
# print(Test.__dict__)
# t.m3()
# print(Test.__dict__)

# class Customer:
#     """Customer class with Banking Operation"""
#     bankname="QACircleBank"
#
#     def __init__(self,name,balance=0.0):
#         self.name=name
#         self.balance=balance
#
#     def deposit(self,amt):
#         self.balance=self.balance+amt
#         print("Balance After deposit :",self.balance)
#
#     def withdraw(self,amt):
#         if amt>self.balance:
#             print("Insufficient Funds...Can't Perform the Operation")
#             sys.exit()
#         self.balance=self.balance-amt
#         print("Balance After withdraw :", self.balance)
#
# print("Welcome to",Customer.bankname)
# name=input("Enter the Name")
# c=Customer(name)
# c.deposit(10000)
# c.withdraw(5000)
# c.withdraw(5000)
# while True:
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Choose your Option")
#     if option=='d' or option=='D':
#         amt=float(input("Enter the Amount"))
#         c.deposit(amt)
#     elif option=='w' or option=='W':
#         amt = float(input("Enter the Amount"))
#         c.withdraw(amt)
#     elif option=='e' or option=='E':
#         print("Thank you for Banking ")
#         sys.exit()
#     else:
#         print("Invalid Option ...Plz Choose Valid Option")

# #Types of Methods which are available in the Python.
# """
# 1.Instance Method
# 2.Class Method
# 3.Static Method
# """
#
# #1.Instance Method
# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.marks=mark
#
#     def m1(self):
#         print(self.name,self.marks)
# s=Student("BSBjw",100)
# s.m1()
#
# #2.Class Method
# """
# 1. Inside the method implementation if we are using only class variable(Static Variable)
# then such type of methods we should declare as class method
# 2. We can declare class Method explicitly by using @classmethod decorator
# 3.For class method we have to pass cls a variable at the time of declaration
# 4.We can call class method by using class name/Object reference variable
#
# """
# class Animal:
#     Lgs=4
#     @classmethod
#     def walk(cls,name):
#         print("{} walks with {} legs ...".format(name,cls.Lgs))
#
# Animal.walk("Dog")
# Animal.walk("Cat")
#
# #Write a program to count no of Objects created for class
# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#
#     @classmethod
#     def noOfObjects(cls):
#         print("The Number of Objects created for Test class",cls.count)
#
#
# t1=Test()
# t2=Test()
# Test.noOfObjects()
# t3=Test()
# t4=Test()
# t5=Test()
# Test.noOfObjects()

# #Getter and Setter Methods
# """
# We can  set and get the values of instance variables by using getter and setter methods
#
# Setter Method:
# Setter method is used to set the Values of instance Variables.
#
# Syntax:
# def setVariable(self,variable):
#     self.variable=Variable
#
# Ex:
# def setName(self,name):
#     self.name=name
#
# Getter Method:
# Setter method is used to get the Values of instance Variables.
#
# Syntax:
# def getVariable(self):
#     return self.variable
#
# Ex:
# def getName(self):
#     return self.name
# """
# class Student:
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
# n=int(input("Enter the number of Students"))
# for i in range(n):
#     s=Student()
#     name=input("Enter the Name")
#     s.setName(name)
#     marks=input("Enter the Marks")
#     s.setMarks(marks)
#
#     print("Hi my name is :",s.getName())
#     print("My Marks are :",s.getMarks())

#Static Method
"""
1. In general these methods are general utility methods
2. Inside these methods we won't use any instance or class variables
3. Here we don't provide self or cls arguments at the time of declaration
4. We can declare static method explicitly by using @staticmethod decorator
5. We can access static method by using classname or object reference 

"""
# class QACircleMath:
#
#     @staticmethod
#     def add(x,y):
#         print("The sum is :",x+y)
#
#     @staticmethod
#     def sub(x, y):
#         print("The substract value is :", x - y)
#
#     @staticmethod
#     def mul(x, y):
#         print("The product is :", x * y)
#
#     @staticmethod
#     def div(x, y):
#         print("The division is :", x / y)
#
#     @staticmethod
#     def avg(x, y):
#         print("The avg is :", x + y/2)
#
# QACircleMath.add(100,200)
# QACircleMath.sub(200,100)
# QACircleMath.mul(10,20)
# QACircleMath.div(200,5)
# QACircleMath.avg(2000,4999)

# #Passing Member of One class to Another class
# #we can pass member of one class inside another class
# class Employee:
#
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#
#     def display(self):
#         print("The Employee Number is :",self.eno)
#         print("The Employee Name is :", self.ename)
#         print("The Employee Salary is :", self.esal)
#
# class Test:
#     def modify(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
#
# e=Employee(100,"Basava",10000)
# Test.modify(e)

#Inner Classes :
"""
Some times we can declare class inside another class , Such type of classes we call it has
inner classes 

Without existing one type of Object, There is no chance of existing another type of an Object.

Without existing Car Object there is no chance of existing Engine Object.Hence
Engine Class should be the part of Car class 
class Car:
    class Engine

#Without existing University Object there is no chance of existing college Object
class University:
    class College: 
        class departments:

"""
class Outer:
    def __init__(self):
        print("Outer class object is created")
    class inner:
        def __init__(self):
            print("Inner class object is created")

        def m1(self):
            print("Inner class Method")

#case 1
o=Outer()
i=o.inner()
i.m1()

#Case 2
Outer().inner().m1()

class Human:
    def __init__(self):
        self.name='Sunny'
        self.head=self.Head()
        self.brain=self.Brain()


    def display(self):
        print("Hello ",self.name)

    class Head:
        def talk(self):
            print("Talking .....")

    class Brain:
        def think(self):
            print("Thinking")

h=Human()
h.display()
h.head.talk()
h.brain.think()

#Garbage Collection
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

#Distructors : Cleanup activities
import time
class Test:
    def __init__(self):
        print("Object Initializing")

    def __del__(self):
        print("Full fill last wish and perform cleanup activities")

t=Test()
t=None
time.sleep(5)
print("End of an application")

#Write a Program to check number of reference variables created for an Object
import sys
class Test:
    pass

t1=Test()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))
#For every object, Python internally maintain one default reference variable is self