# """
# Inheritance
# Has-A Relationship (Composition)
# IS-A Relationship (Inheritance)
#
# Types of Inheritance
#     1.Single Inheritance
#     2. Multi Level Inheritance
#     3. Hierarchical Inheritance
#     4. Multiple Inheritance
#     5. Hybrid Inheritance
#
# MRO (Method Resolution Order)
# super() Method
#
# """
# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#
#     def m1(self):
#         print("Engine Specific Functionality")
#
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2(self):
#         print("Car using engine class functionalities")
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
#
# c=Car()
# c.m2()
#
# #example 2:
# class Car:
#
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#
#     def getinfo(self):
#         print("Car Name is :{} ,Model is :{}, Color is :{}".
#               format(self.name,self.model,self.color))
#
# class Employee:
#     def __init__(self,ename,eno,car):
#         self.ename=ename
#         self.eno=eno
#         self.car=car
#
#     def empinfo(self):
#         print("The Name of an employee is :",self.ename)
#         print("The Employee Number is :",self.eno)
#         print("The Car Information of an employee")
#         self.car.getinfo()
#
# c=Car("I20",2016,"Red")
# e=Employee("Rohit",121,c)
# e.empinfo()

#Is-A Relationship(Inheritance)
""""
1.What ever the variables, Methods and constructors available in parent class by default
  will be available to child classes and we are not required to rewrite.
2.The Main advantage of Inheritance is Code Reusability and we can extend the existing
  functionalities with some more extra functionalities

"""
# class Parent:
#     a=10
#     def __init__(self):
#         self.b=10
#
#     def m1(self):
#         print("Parent class Method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class Class Method")
#
#     @staticmethod
#     def m3():
#         print("Parent class Static Method")
#
# class Child(Parent):
#     def m1(self):
#         super().m1()
#         print("This is a child class instance method")
#
#
# c=Child()
#
# print(c.a)
# print(c.b)
# c.m1()
#
# class P:
#     a=100
#     def __init__(self):
#         self.b=200
#
# class C(P):
#     c=300
#     def __init__(self):
#         super().__init__()
#         self.d=400
#
# c1=C()
# print(c1.a,c1.b,c1.c,c1.d)
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eatdrink(self):
#         print("Eat Biryani and drink Beer")
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#
#     def work(self):
#         print("Coding Python is very very easy just like drinking chilled beer")
#
#     def empinfo(self):
#         print("Employee Name :",self.name)
#         print("Employee Age :",self.age)
#         print("Employee Number", self.eno)
#         print('Employee Salary',self.esal)
#
# e=Employee("Vaishak",25,420,10000)
# e.eatdrink()
# e.work()
# e.empinfo()

print("************************************************************")
#Is-A vd HAS-A
# class Car:
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def getinfo(self):
#         print("\tCar Name :{} \n\tModel :{} \n\tColor :{}"
#                 .format(self.name,self.model,self.color))
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eatdrink(self):
#         print("Eat Biryani and drink Beer")
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal,car):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#         self.car=car
#
#     def work(self):
#         print("Coding Python is very very easy just like drinking chilled beer")
#
#     def empinfo(self):
#         print("Employee Name :",self.name)
#         print("Employee Age :",self.age)
#         print("Employee Number", self.eno)
#         print('Employee Salary',self.esal)
#         print("Employee Car info:")
#         self.car.getinfo()
#
# c=Car("Innove","2.5V","Grey")
# e=Employee("Vaishak",25,420,10000,c)
# e.eatdrink()
# e.work()
# e.empinfo()

# #Types of Inheritance:
# #Single Inheritance
# """
# The concept of Inheriting the properties from once class to another class is
# known as single Inheritance
# """
# class A:
#     def m1(self):
#         print("Parent class Method")
#
# class B(A):
#     def m2(self):
#         print("Child class Method")
#
# b=B()
# b.m1()
# b.m2()
#
# #Multi Level Inheritance
# """
# The Concept of Inheriting the properties from multiple classes in to single class
# with the concept of one after another is know as multilevel inheritance
# """
# class A:
#     def m1(self):
#         print("Parent class Method")
#
# class B(A):
#     def m2(self):
#         print("Child class Method")
#
# class C(B):
#     def m3(self):
#         print("Sub child class Method")
# c=C()
# c.m1()
# c.m2()
# c.m3()
#
# #Hierarchical Inheritance:
# """
# The concept of inheriting the properties from one class into Multiple classes
# which are at the same level is know as Hierarchical Inheritance
# """
class A:
    def m1(self):
        print("A Super class Method")

class B(A):
    def m2(self):
        print("B child class Method")

class C(A):
    def m3(self):
        print("C Child class Method")

b=B()
b.m1()
b.m2()

c=C()
c.m1()
c.m3()
#Multiple Inheritance
"""
The concept of inheriting the properties from  Multiple classes into single class
is know as Hierarchical Inheritance
"""
# class A:
#     def m1(self):
#         print("A Super class Method")
#
# class B:
#     def m2(self):
#         print("B Super class Method")
#
# class C(A,B):
#     def m3(self):
#         print("C Child class Method")
#
# c=C()
# c.m1()
# c.m2()
# c.m3()

# #super()  Method
# """
# super() is a built in method which used to call super class constructors,variables
#  and Methods from the child class.
#
# """
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print('Name',self.name)
#         print("Age",self.age)
#
# class Student(Person):
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.marks=marks
#
#     def display(self):
#         super().display()
#         print("RollNo",self.rollno)
#         print("Marks",self.marks)
#
# s=Student("Muttu",28,20,20000)
# s.display()

class P:
    a=10
    def __init__(self):
        self.b=20
        self._z=200
        print(self.b)

    def m1(self):
        print("Parent class Instance Method")

    @classmethod
    def m2(self):
        print("Parent class Class Method")

    @staticmethod
    def m3():
        print("Parent class Static Method")

class C(P):
    a=888
    print(a)
    def __init__(self):
        self._z=400
        print(self._z)

        self.b=999
        print(self.b)
        super().__init__()
        print(self._z)
        print(self._z)
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c=C()
