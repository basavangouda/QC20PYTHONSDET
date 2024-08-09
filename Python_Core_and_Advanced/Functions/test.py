# # #Parameters
# def wish(name):
#     print("Hello",name," Good Morning")
#
# wish("Guest")
# wish("QACircle")
#
# #Return Statement
# def add(x,y):
#     return x+y
#
# result=add(100,200)
# print("The Sum is ",result)
# print("The sum is =", add(200,400))
#
# #Write a function to check whether given number is odd /Even
# def even_odd(num):
#     if num%2==0:
#         print(num,"Is a Even number")
#     else:
#         print(num,"Is not an even number")
#
# even_odd(10)
# even_odd(20)
# even_odd(33)
#
# #Write a function to find factorial of  given number
# #5 = 5*4*3*2*1 ==> 120
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result
#
# print(fact(10))
# for i in range(1,6):
#     print("The Factorial of ",i,"is :",fact(i))
#
# #Return multiple values from the Function
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
#
# x,y=sum_sub(2000,400)
# print("The sum is =",x)
# print("The sub is =",y)
#
# #Types of Arguments
# """
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments
# """
# #1. Positional Arguments ==> These arguments are passed to the function in a correct positional order
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
#
# x,y=sum_sub(2000,400)
# print("The sum is =",x)
# print("The sub is =",y)
#
# x,y=sum_sub(400,2000)
# print("The sum is =",x)
# print("The sub is =",y)
# print("*******************************************************")
# #2. Keyword Arguments
# def wish(name,msg):
#     print("Hello ",name,msg)
#
# wish(name="QACircle", msg="Good Morning")
# wish(msg="Good Morning",name="QACircle")
#
# print("*******************************************************")
# #3. Default Arguments
# def wish(name="Guest"):
#     print("Hello",name,"Good Night")
#
# wish()
# wish("Basava")
#
# #Note :
# # def wish(name="Guest",msg="Good Morning"): #===> Valid
# #     pass
# # def wish1(name,msg="Tata Bye bye"): #===>Valid
# #     pass
# # def wish2(name="Guest",msg): #===>In-Valid
# #     pass
#
# print("*******************************************************")
# #4. Variable Length Arguments
# """
# We can pass any number of arguments to our function , Such type of
# arguments are called variable length arguments
#
# We declare with * symbol as follows
# def f1(*n):
#
# We can call this function and passy any number of arguments including Zero number
#
# Internaly all the values represented as Tuple
# """
# def sum(*n):
#     total=0
#     for i in n:
#         total=total+i
#     print("The sum is =",total)
#
# sum()
# sum(100,200,300,400,500)
# sum(10.5)
#
# #can we mix variable length argument with positional arguments
# # def f1(n1,*s):
# #     print(n1)
# #     for s1 in s:
# #         print(s1)
# #
# # f1(100)
# # f1(100,"A",200,"B",800)
# #
# # def f1(*s,n1):
# #     print(n1)
# #     for s1 in s:
# #         print(s1)
# #
# # f1(100,300,n1=1000)
# # f1(100,"A",200,"B",800,n1=2000)
#
# #types of Variables
# a=10 #global
# #global variables can be accessed in all functions of that moduel.
# def f1():
#     print(a)
#     b=20 #local
#     #local variable are local to this function ,can access inside function
#     #Local variables can't accessed outside of function
#     print(b)
#
# def f2():
#     print(a)
#     #print(b)
#
# f1()
# f2()
#
# print("************************************")
# def f3():
#     global a
#     a=100
#     print(a) #local
#     print(globals()['a']) #global
#
# def f4():
#     print(a)
#
# f3()
# f4()
#
# #Recursive functions: A function calls itself is know as Recursive function
# """
# factorial(3)==>3*factorial(2)
#             ==>3*2*factorila(1)
#             ==>3*2*1*factorila(0)
#             ==>3*2*1*1
#             ===>6
#
# factorial(n)=n*factorial(n-1)
# """
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
#
# print(factorial(5))
#
# #lambda function : Anonymous Functions
# """
# some time we can declare a function without any name, such type of nameless
# functions are called as anonymous functions or lambda functions
#
# main purpose is one time usage and we can write lengthy code is one line
#
# Normal Function:
# def square(n):
#     return n*n
#
# Lambda Function
#     lambda n:n*n
#
# Syntax : lambda argument_list:expression
# """
# #Lambda function to find square of a number
# s=lambda n:n*n
# print("The Square of 4 =",s(4))
# print("The Square of 4 =",s(12))
#
# s1=lambda a,b:a+b
# print("The sum of two values is =",s1(10,20))
#
# s3=lambda a,b:a if a>b else b
# print("The biggest number is =",s3(100,2000))
#
# #************String Program***************
# s="aaabbcccd"
# """Output = Output:
#   a:3
#   b:2
#   c:3
#   d:1
# """
# d={}
# x=0
# for i in s:
#     if i not in d:
#         d[i]=1
#     elif i in d:
#         d[i]=d[i]+1
#
# print(d)

#filter(), map() , reduce()
#filter()
#Without using lambda function
# def isEven(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
#
# l1=[0,5,10,15,25,20,33,30]
#
# l2=list(filter(isEven,l1))
# print(l2)
#
# #with using lambda
# l3=list(filter(lambda x:x%2==0,l1))
# print(l3)
# l4=list(filter(lambda x:x%2!=0,l1))
# print(l4)

# #map() function
# #without using lamda
# l=[1,2,3,4,5]
#
# def double(x):
#     return x*2
#
# l1=list(map(double,l))
# print(l1)
#
# #with Lamda
# l2=list(map(lambda x:2*x,l))
# print(l2)
# l3=list(map(lambda x:x*x,l))
# print(l3)
#
# l10=[10,20,30]
# l11=[10,20,30]
# l4=list(map(lambda x,y:x*y,l10,l11))
# print(l4)

# from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)
# print("*************************")
# from functools import *
# result=reduce(lambda x,y:x+y,range(1,101))
# print(result)

def Outer():
    print("Outer function started Executing")
    def inner():
        print("Inner function started Executing")
    print("Outer function is calling inner function")
    inner()

Outer()

