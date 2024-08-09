# #Conditional Statements
# """
# if  condition: statement
#
# or
# if Condition :
#     statement-1
#     statement-2
#     statement-3
#
# """
# name=input("Enter the name")
# if name=="QACircle":
#     print("Welcome to QACircle Training Program")
# print("Who are you")
#
# #if-else
# name=input("Enter the name")
# if name=="QACircle":
#     print("Welcome to QACircle Training Program")
# else:
#     print("Hello Guest How can i help you")
# print("How are you")
#
# #if-elif-else
# """
# if condition 1 :
#     Action-1
# elif condition 2:
#     Action-2
# elif condition 3:
#     Action-3
# else:
#     Default Action
#
# """
# brand=input("Enter your brand Name")
# if brand=="RC":
#     print("Its a children's brand")
# elif brand=='KF':
#     print("Its not that much kick")
# elif brand=='TB':
#     print('Buy one get one')
# else:
#     print("We don't encourage other brand names")
#
# #WAPT find bigger number by reading 2 values from the keyboard
# #WAPT find bigger number by reading 3 numbers from the keyboard
# n1=100
# n2=200
# if n1>n2:
#     print("The bigger number is =",n1)
# else:
#     print("The Bigger number is=",n2)
#
# #WAPT check whether given number is present in the range between 1 to 100
# n=int(input("Enter the number"))
# if n>=1 and n<=100:
#     print("The number ",n," is present between 1 to 100")
# else:
#     print("The number ", n, " is not present between 1 to 100")

#Iterative Statements
"""
if we want to execute a group of statements multiple times then
we should go for iterative statements

for:
if we want to execute some elements in sequence order (string or Collection)
then we go with forloop

Synatx  for x in sequence:
            body

sequence ==> it can be string or any collection
body ==> it will execute every element present in the sequence
"""
# s="Sunny Leone"
# for x in s:
#     print(x)
#
#
# s="Sunny Leone"
# y=len(s)
# i=0
# for x in s:
#     print("The character ",x,"present at +ve index is",i,"and -ve index is ",i-y)
#     i=i+1
#
# for x in range(10):
#     print("Hello")
#
# #Print only Odd numbers (0 to 20)
# for x in range(21):
#     if x%2!=0:
#         print(x)

#WAPT display the numbers from 10 to 1 in descending order
# for x in range(10,0,-1):
#     print(x)

#WAP to print sum of list
# list=eval(input("Enter the list"))
# sum=0
# for x in list:
#     sum=sum+x
# print("The sum of list is :",sum)

#While Loop
"""
if we want to execute a group of statements iteratively until some condition false,
then we should go for while loop 
Syntax : while condition:
            body
"""
#Print the numbers from 1 to 10
print("******************Executing while loop*****************")
# x=1
# while x<=10:
#     print(x)
#     x=x+1

#WAPT to display sum of first n numbers
# n=int(input("Enter number"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("The sum of first",n,"Numbers are :",sum)

#Write a program for propt user until they enter QACircle:
# name=""
# while name!='QACircle':
#     name=input("Enter the name")
# print("Thank for the confirmation")

#PIN Generation 3 attempts : Assignment

#Infinite loop
# while True:
#     print("Hello QACircle")

#Nested loop
#Some times we take a oneloop inside another loop we call it has nested loop.
# for i in range(4):
#     for j in range(4):
#         print("i=",i,"j=",j)


#Transfer Statements
#break :we can use break statement inside loops to break loop execution based on some condition


# for x in range(10):
#     if x==8:
#         print("Please don't print this value")
#         break
#     print(x)

# cart=[10,100,200, 500,250,460]
# for item in cart:
#     if item>=500:
#         print("Please remove this product from the cart and i will not pay money")
#         break
#     print(item)

#Continue :
#We can use the continue statement to skip the current iteration and contine for next iteration
# cart=[10,100,200, 500,250,460]
# for item in cart:
#     if item>=500:
#         print("Please remove this product from the cart and i will not pay money")
#         continue
#     print(item)

#WAPT ptint only odd numbers from 0 to 9
# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

#loops with else block
"""
1==>Inside loop execution, if break statement not executed, then only else part will
 be executed.
 
2. else means loop without break
 
"""
# cart=[10,100,200, 50,250,460]
# for item in cart:
#     if item>=500:
#         print("Please remove this product from the cart and i will not pay money")
#         break
#     print(item)
# else:
#     print("All the products successfully ordered")

#pass statement
def m1():
    pass

if True:
    pass

for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass

x=100
print(x)
del x
#print(x)

y=1000
print(y)
y=None
print(y)

