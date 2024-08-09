# list=[100,"Punith","Chaitra","Amog",29.96,"True",False]
# print(list)
# print(len(list))
# print(list[-7])
# #print(list[10])
#
# #slice Operator
# # list2= list1[start:stop:step]
# print(list[::-1])
# print(list[1:2:3])
# print(list[-1::])
# print(list[1::])
#
# #Adding elements to list list.append() , list.remove()
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1
#
# print('******for loop*******')
# for x in list:
#     print(x)
#
# l=[0,2,3,5,7,8,4,6,9,1,4,6,2,1,2,39,10]
# for i in l:
#     if i%2==0:
#         print(i,end=' ')
# print()
#
# l1=["A","B","C"]
# z=len(l1)
# for i in range(z):
#     print(l1[i],"is present at the positive index :",i,"and the negative index is :",i-z)
#
# #count()
# print(l.count(2))
#
# #index()
# print(l.index(1))
# print(l.index(10))
# #print(l.index(100))
#
# #WAP to add elements to the list upto 100 which are divisible by 9
# list1=[]
# for i in range(100):
#     if i%9==0:
#         list1.append(i)
# print(list1)

# list=[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
# list.insert(2,299)
# print(list)
# list.append(100)
# print(list)
#
# #differnce between append() and Insert()
#
# #Extend() function
# order1=["Egg Rice","Tomato Rice","Polovo","Veg Fried rice"]
# order2=["Gobi","Pani Puri","Laddu","Ice Cream"]
# print(id(order1)," ",id(order2))
# print(order1)
# order1.extend(order2)
# print(order1)
#
# #pop()
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
# print(order1.pop())
#
#
# #I want to remove Particular object/Element
# order1=["Egg Rice","Tomato Rice","Polovo","Veg Fried rice"]
# print(order1.pop(0))
# print("***********************************************************")
# #pop() and remove()
# print(order1)
# print(order1.pop())
# order1.remove("Tomato Rice")
# print(order1)
#
# #Reverese():
# l=[10,30,20,8,6,19,89]
# print(l)
# l.reverse()
# print(l)
#
# #sort
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.sort(reverse=True)
# print(l)
#
# l1=["Dog","Cat","Mouse"]
# print(l1)
# l1.sort()
# print(l1)
#
# #here we should have homogeneous elements
# l2=["Dog","Cat","Mouse",20,80,99,5]
# print(l2)
# l2.sort()
# print(l2)

#list aliasing :
# The process of giving another reference variable name to the exiting list is called as aliasing
# x=[10,20,30,40]
# print(id(x))
# print(x)
# y=x
# print(id(y))
# print(y)
# x[0]=100
# print(x)
# print(y)
#
# #cloning  1==>slicing and copy()
#
# a=[10,20,30,40]
# b=a[::]
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# a[1]=2000
# print(a)
# print(b)
#
# c=a.copy()
# print(c)
#
# #difference between = operator and copy()
# x=["Dog","Cat","Rat"]
# y=["Dog","Cat","Rat"]
# z=["DOG","CAT","RAT"]
# print(x==y)
# print(id(x),id(y),id(z))
# print(x==z)
# print(x!=z)
#
# #memebership in , not in
# print("dog" in x)
# print("Dog" not in z)
#
# x.clear()
# print(x)
#
# #Nested list
# n=[10,20,30,[40,50,[60,70]]]
# print(n)
# print(n[3][2][1])

#List Comprehensions:
# it's a very easy and compact way of creating a list objects from iterable objects
# (Like list,tuple, Dictionary ,range) based on some condition
#Syntax ==> list=[expression for item in list if condtion]

s=[x*x for x in range(1,11)]
print(s)
print(type(s))

s1=[x for x in range(1,11)]
print(s1)
print(type(s1))

#Even numbers
s2=[x for x in range(1,11) if x%2==0]
print(s2)
print(type(s2))

words=["Nag","Basava","Kiran","Punith","Amog","Rohit"]
l=[w[0] for w in words]
print(l)

num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[i for i in num1 if i not in num2]
print(num3)

vowels=['a','e','i','o','u']
Name="qacirclesoftwaretrainingacademy"