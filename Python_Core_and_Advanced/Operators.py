
'''
===> Operators are the symbol that performs certain operations
===> Python provides the following operators
        1. Arithmetic Operator
        2. Relational Operator or Comparison Operator
        3. Logical Operator
        4. Bitwise Operator
        5. Assignment Operator
        6. Special Operator

'''
# 1. Arithmetic Operator
"""
+ ==> Addition
- ==> Subtraction
* ==> Multiplication
/ ==> Division
// ==>floor Division
%  ==> Modulo Operator
** ==> Exponent Operator Or Power Operator


x=100
y=20
print("x+y =",x+y)
print("x-y =",x-y)
print("x*y =",x*y)
print("x/y =",x/y)
print("x//y =",x//y)
print("x%y =",x%y)
print("x**y =",x**y)
"""

"""
Note ==> 1
print(0/100)
print(100/0)
print(100%0)
"""

"""
#Note ==> 2
a="QACircle"
b="Training Academy"
c=8
print(a+b)
#Here we will get type Error
print(a+c) 
print(b+c)
"""

#Note ==> 3
# a="QACircle"
# b="Training Academy"
# c=8
# print(a+b*c)
# print(a*c)
# print(b*c)
# print(a*b)

"""
#2. Relational Operator or Comparison Operators > , >=, <. <=
#Example 1
a=10
b=20
print(" a > b =",a>b)
print(" a >= b =",a>=b)
print(" a < b =",a<b)
print(" a <= b =",a<=b)
print("**********************************")
#Example 2
x="qacircle"
y="qacircle"
print(" x > y =",x>y)
print(" x >= y =",x>=y)
print(" x < y =",x<y)
print(" x <= y =",x<=y)
print("**********************************")
#Example 3
a=1000
b=200
if a>b:
    print("Test is Pass")
else:
    print("Test Fail")
print("**********************************")

# Chaining of relational operator is possible
print(10>20>30>40>50)
print(10<20<30<40>50)
print("**********************************")
#Equality Operators : == ,!=
print(10==10)
print("QAC"==10)
print("QAC"!=10)
print("QACircle"=="qacircle")
print("QACircle"=="QACircle")
print(10==10==10==10)
print(20==20==10==30)


#3. Logical Operator  and , or, not
#We can apply for all the type

#Boolean Types Behaviour

and ===> if both arguments are True then only result is True
or ===> if atleast one argument is True then result is True
not ==> complement 

x=True
y=False
print(x and x)
print(True and True)
print(y and x)
print(x or y)
print(not x)
print(not y)
"""


#For Non Boolean Type Behaviour
"""
Zero  means False 
Non-Zero means True
empty String it is always treated as False
"""

"""
print(10 and 20)
print(100 and 200)
print(0 and 2000)
print(100 and 0)
print(100 or 0)
print(0 or 2000)
print(not 0)
print(not 100)
print("" and "qacircle")
print("qacircle" and "QACircle")
print("**********************************")
print(" " or "QAC")
print("QAC" or " ")
print("QAC" or "")
print(not "")
print(not " ")
print("**********************************")

#4. Bitwise Operator
We can apply these operators bitwise 
These operators are applicable only for int and boolean type
By mistake if we try to apply any other type then we will get error
===> &  (bitwise and ) if both bits are 1 then only result is 1 otherwise 0
====> | (bitwise or) if atleast one bit is 1 then the result is 1 otherwise 0
====> ^ (Nagation) if bits are different then only result is 1 otherwise 0
====> ~ (Complement Operator) ==> 1 Means 0 and 0 Means 1 
====> >>  (Bitwise Right Shift) 
====> <<  (Bitwise left shift)
"""

""""
print(4&5)
print(10&20)
print(4|5)
print(4^5)
print(6^7)
print(~5)  #(- , +1)
print(~-8) #(- , -1)
print(10>>2)
print(10<<2)
"""

#5. Assignmnet Operators  ==>  =
"""
Assignment operators are used to assign the values to the variables
EX =====>x=10

We can combine assignment operator with some other operators , So we call it has 
compound assignment operators 
+=
-=
*=
/=
//=
**=
|=
&=
^=
>>=
<<=
"""

#Examples
# x=10
# x+=20
# print(x)
#
# y=100
# y**=10
# print(y)

#Ternary Operator or Conditional Operator
#Syntax x = first value if condition else second Value
#Eg ==> 1
# a,b=120,200
# x=a if a>b else b
# print(x)

#Eg ==> 2 Read two inputs from the keyboard and print bigger value
# a=int(input("Enter First Value"))
# b=int(input("Enter Second Value"))
# x=a if a>b else b
# print(x)

#Eg ==> 2 Read two number from the keyboard and print minimum value
# a=int(input("Enter First Value"))
# b=int(input("Enter Second Value"))
# min=a if a<b else b
# print(min)

#Write a program to read 3 numbers from the keyboard and print max value
#Syntax  max_value= first_value if condition and condition else second Value if condition else third value
# x=int(input("Enter the First Value"))
# y=int(input("Enter the Second Value"))
# z=int(input("Enter the Third Value"))
# max_value=x if x>y and x>z else y if y>z else z
# print(max_value)
# print(type(max_value))


#Write a program to read 3 numbers from the keyboard and print min value
#Write a program to read 3 numbers from the keyboard , if 2 numbers are equal validate and print min and max value


#Special Operator
"""
1. Identity Operator
    is 
    is not 
2. Membership Operator
    in 
    not in
"""

a=100
b=100
print(id(a),"===",id(b))
print(a is b)
x=120
y=200
print(x is y)
print(a==b)
print(x is not y)

#Note
#is ==> operator used for address comparison
#== ==> operator used for content comparison

s1="QACircle"
s2='QACircle'
print(s1 is s2)

list1=["one","two","three"]
list2=["one","two","three"]
print(list1 is list2)
print(id(list2))
print(id(list1))
print(list1==list2)

s1="Learning Python is Very Easy"
print("Easy" in s1)
print("easy" in s1)
print("l" not in s1)
print("L" in s1)
print("J" not in s1)

list=["Bunny","Pinny","Billi","Sunny"]
print("sunny" in list)
print("Sunny" in list)
print("bunny" not in list)

#Operator Precedence
# () ==> parentheses
# ** ==>
# * ,/,//,% ==>
# +,- ==>
# << ,>> ==>
# & ==>
# | ==>
# ==,!=,>,>=,<,<= ,is, is not,in , not in
# not ==>
# and ==>
# or ==>
a=10
b=20
c=30
d=40
print((a+b)*c/d)
print(a+(b*c)/d)


