# """
# Decorator is a function which can take function as argument and extends its
# functionality and return the modified function with extended functionalities.
#
# """
# #Ex 1:
# def decor(func):
#     def inner(name):
#         if name=="Bhavya":
#             print("Hello",name," Bad Morning")
#         else:
#             func(name)
#     return inner
#
# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")
#
# wish("Girish")
# wish("Bhavya")
# wish("Amogh")
#
# print("******************************")
# #Example 2
# #How to call same function with Decorator and without Decorator
# def decor(func):
#     def inner(name):
#         if name=="Bhavya":
#             print("Hello",name," Bad Morning")
#         else:
#             func(name)
#     return inner
#
# def wish(name):
#     print("Hello",name,"Good Morning")
#
# wish("Girish") #Decorator wont be executed
# wish("Bhavya") #Decorator wont be executed
#
# modified_function=decor(wish)
#
# modified_function("Girish")
# modified_function("Bhavya")
#
# #Ex 3
# def make_pretty(func):
#     def inner():
#         print("I got Decorated")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am Ordinary")
#
# ordinary()
#
# #Ex 4
# print("@@@@@@@@@@@@Smart Division with Decorator Function@@@@@@@@@@@@@@@@@@")
# def smart_divide(func):
#     def modification(a,b):
#         print("I am going to divide",a,"and",b)
#         if b==0:
#             print("Whoops! can't divide")
#             return
#         return func(a,b)
#     return modification
#
# @smart_divide
# def divide(a,b):
#     print(a/b)
#
# divide(2,5)
# divide(2,0)
#
# #Decorator Chaining
# def star(func):
#     def inner(*args,**kwargs):
#         print("*"*15)
#         func(*args,**kwargs)
#         print("*"*15)
#     return inner
#
# def percentage(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner
#
#
# @percentage
# @star
# def printer(msg):
#     print(msg)
#
# printer("Hello")
#
# # Generator Function
# """
# Generator Function is a function which is responsible to generate sequence of
# values. We can write the generator function just like ordinary function,but it
# uses yield keyword to return the values
# """
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#
# g=mygen()
# print(type(g))
#
# print(next(g))
# print(next(g))
# print(next(g))
#
# """"
# In Normal Collection we will get Memory Error,
#    ===> Because it will first store the data and the process for execution
#
# In Case of Generator we will not Memory Error,
#    ===> Because it will first Process the data for execution and then store it
#
# Normal Collection will take more time for execution
#
# But Generator will take less time for execution.
#
# """
# #Normal Collection
# y=[i*i for i in range(10000000000000000000000000000000000000)]
# print(type(y))
# print(y)
#
# #Generator
# x=(i*i for i in range(10000000000000000000000000000000000000))
# print(type(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#

#Ex 2 Write a Program to generate first n numbers
def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1

l=firstn(5)
print(type(l))
print(l)
for x in l:
    print(x)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# Ex 3: Write a program to generate fibonacci Series
# Ex==>0,1,1,2,3,5,8,13
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i>100:
        break
    print(i)


assert 100==100,"Both are not equal"

def square(x):
    return x*x

assert square(4)==16,"The square of 4 is 16 but not matching"
assert square(4)==12,"The square of 4 is 16 but not matching"