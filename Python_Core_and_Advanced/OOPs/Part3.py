# #1. Operator Overloading
# #We can use same operator or Methods for different purposes
# #Ex 1
# # print(10+20)
# # print("QAC"+"ircle")
# #
# # #Ex 2
# # print(10*20)
# # print("QACircle"*20)
#
# #We can use deposit() method to deposit cash or cheque or dd
# """
# deposit(cash)
# depossit(cheque)
# deposit(dd)
# """
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
#
# """
# Note:
# 1. We can overload + Operator to work with Book Object also
#    i.e Python supports Operator Overloading
# 2. For Evry method there will be a magic method will be available.
#   To overload any operator we have to override that method in our class
# 3. Internally + Operator implements __add__() Method.This method is called magic
#     method of + Operator.We have to Override this Method
#
# """
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def __gt__(self, other):
#       return self.marks>other.marks
#
#     def __le__(self,other):
#         return self.marks <= other.marks
#
#
# print("10>20=",10>20)
# s1=Student("Basava",100)
# s2=Student("Girish",90)
# print("s1>s2=",s1>s2)
# print("s1<s2=",s1<s2)
# print("s1>=s2=",s1>=s2)
# print("s1<=s2=",s1<=s2)
#
# #Overload multiplication Operator to work on EMployee Objects:
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def __mul__(self, other):
#         return self.salary*other.days
#
# class Timesheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#
# e=Employee("Amogh",500)
# t=Timesheet("Amogh",25)
# print("The Monthly Salary is",e*t)
#
# #Method Overloading
# """
# 1.If 2 Methods having same name but different types of arguments then those methods
# we call it has Overloaded Methods
# Ex:
#     m1(int a)
#     m1(float d)
#
# 2. But in Python Method Overloading is not possible
# 3.if we try to declare Multiple Methods with same name and different number arguments
# then python will always consider only last/latest method
# """
# class Test:
#     def m1(self):
#         print("This is no argument Method")
#
#     def m1(self,a):
#         print("This is one argument Method")
#
#     def m1(self,a,b):
#         print("This is two argument Method")
#
# t=Test()
# t.m1(20,30)
#
# #Demo Program with Default Arguments
# class Addition:
#     def sum(self,a=None,b=None,c=None,d=None):
#         if a!=None and b!=None and c!=None and d!=None:
#             print("The sum is =",a+b+c+d)
#         elif a!=None and b!=None and c!=None:
#             print("The sum is =", a + b + c )
#         elif a!=None and b!=None:
#             print("The sum is =", a + b)
#         else:
#             print("Please provide 2 or 3 or 4 arguments")
#
# a=Addition()
# a.sum()
# a.sum(100,200,300)
# a.sum(100,200,300,400)
# #a.sum(100,200,300,400,500)
#
# #Program with Variable number of Arguments
# class DifferentArguments:
#     def sum(self,*a):
#         total=0
#         for i in a:
#             total=total+i
#         print("The Sum is =",total)
#
# d=DifferentArguments()
# d.sum(10)
# d.sum(100,200,10,12.5,6,8,9)
#

# #   Constructor Overloading
# """
# Constructor Overloading is not possible in Python
# If we define multiple constructor then the last constructor will be considered
# """
# class Test:
#     def __init__(self):
#         print("No arg Constructor")
#
#     def __init__(self,a):
#         print("One arg Constructor")
#
#     def __init__(self,a,b,c):
#         print("Three arg Constructor")
#
# t=Test(100,200,300)

#Overriding :
"""
Method Overriding :
1.Whatever the members are available in the parent class by default are available in the child class
through inheritance. if child class is not satisfied with parent class implementation then
child class will be allowed to redefine those methods in child class based on our requirements
THis Concept is called overriding
2. Python supports both Method and Constructor Overriding
"""
# class Person:
#     def property(self):
#         print("Gold+Land+Cash+Power")
#
#     def House(self):
#         print("3 BHK House")
#
#
# class child(Person):
#     def House(self):
#         print("4 BHK New House with Modern Interiers")
#
# c=child()
# c.property()
# c.House()
#
# # Constructor Overriding :
# class A:
#     def __init__(self):
#         print("Parent Constructor")
#
# class B(A):
#     pass
#     # def __init__(self):
#     #     print("Child Constructor")
#
# b=B()
#
# #Demo Program to call Parent class Constructor by using super():
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#
#     def display(self):
#         print("Employee name ",self.name)
#         print('EMployee Age ',self.age)
#         print("EMployee Number ",self.eno)
#         print("Employee Salary ",self.esal)
#
# e1=Employee("Arun",48,"q234",30000)
# e1.display()


