# #Case 1
# import math
# print(math.pi)
#
# #Case 2
# import math as m
# print(m.pi)
#
# #Case 3
# from math import pi
# print(pi)
#
# #Case 4
# from math import pi as x
# print(x)
#
# #Case 5
# from math import *
# print(sin(60))
# print(tan(30))
#
#
# x1=100
#
# def m1():
#     x=100
#     y=200
#     print("Hello")
#
# class Test:
#     pass
#
# import Mathematical
# print(dir(Mathematical))
#

#Random Module:

#random() ==> 0<x>1
from random import *
for i in range(5):
    print(random())

#randint() ==> This function will generate integer value between 2 numbers
from random import *
for i in range(10):
    print(randint(10,50))

#uniform() : it will generate the random floating value between 2 given sequence number
from random import *
for i in range(5):
    print(uniform(1,10))

print("***********************************")
#randrange([start],stop,[step])
from random import *
for i in range(5):
    #print(randrange(10))
    #print(randrange(1,11))
    print(randrange(0, 100,20))

#choice() Function :
#this function will not generate random number
#but it will return random object from the given list/tuple
list=["Sunny","Pinny","Binni","Hello","QAC","Munni"]
for i in range(10):
    print(choice(list))

