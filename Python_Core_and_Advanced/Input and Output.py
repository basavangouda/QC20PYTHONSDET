#input()
#Example 1
#Write a program to read employee dat from the keyboard and display the info
# eno=input("Enter the employee Number")
# ename=input("Enter the Employee Name")
# esal=float(input("Enter the employee salary"))
# eadd=input("Enter the employee address")
# married=bool(input("Employee Married ?True|False"))
#
# print("Employee No =",eno)
# print("Employee Name =",ename)
# print("EMployee Salary=",esal)
# print("Employee Address=",eadd)
# print('Employee Marriage Status=',married)

#Example 2
# num=5
# for x in num:
#     eno = input("Enter the employee Number")
#     ename = input("Enter the Employee Name")
#     esal = float(input("Enter the employee salary"))
#     eadd = input("Enter the employee address")
#     married = bool(input("Employee Married ?True|False"))
#
#     print("Employee No =", eno)
#     print("Employee Name =", ename)
#     print("EMployee Salary=", esal)
#     print("Employee Address=", eadd)
#     print('Employee Marriage Status=', married)

#eval() ==> It is a function take's the string and evaluate the result
# x=eval("10+20+30.0")
# print(x)
# print(type(x))

# z=eval(input("Enter the expression"))
# print(z)

# y=eval(input("Enter the list"))
# print(type(y))
# print(y)

#split()
#write a program read 3 numbers from keyboard and
# number should be separated by ; and print sum of all value
# a,b,c=[int(x) for x in input("Enter 3 numbers").split(";")]
# print('Sum of all 3 numbers =',a+b+c)

#write a program read 3 floating numbers from keyboard and
# number should be separated by , and print sum of all value
# a,b,c=[float(x) for x in input("Enter 3 numbers").split(",")]
# print('Sum of all 3 numbers =',a+b+c)

#Output Statements:
#print() ==Its a function to display the output

#form ==>1 print() without any argument
print() #==> It will just print new line character

#form ==>2 print(String)
print("Hello World")
print("Hello \n World")
print("Hello\tworld")

#form ==>3 print() with variable number of arguments
x,y,z=100,120,240
print("The Values are =",x,y,z)

#Default output separated by space. if we want we can specify separtor using "sep" attribute
print("The Values are =",x,y,z,sep=",")
print("The Values are =",x,y,z,sep="=")
print("The Values are =",x,y,z,sep="#")

#form ==>4 print() with end attribute
print("Hello")
print("QACircle")
print("Basavanagouda")
print("Stop python class we want go and sleep")

#I want all four output in one line
print("Hello",end=' ')
print("QACircle",end=' ')
print("Basavanagouda",end=" ")
print("Stop python class we want go and sleep")

#form ==>5 print(Object)
list=[100,200,300]
t=120,340,110
print(list)
print(t)

#form ==>6 print(string , Variable list)
s="QACircle"
a=3
s1="Python"
s2="Java"
print("Hello",s,"Your age is",a)
print("You are teaching",s1," and ",s2)

#form ==>7 print(formatted STring)
"""
%i ==>int 
%d===>int 
%f ==>float
%s ==>String

syntax print("formatted string"%(Variable list))

"""
a=10
b=20
c=30
print("a value is %i"%a)
print("b value is %d and c Value is %d" %(b,c))

s="Basava"
list=[10,20,30]
print("Hello %s....The list of items are %s" %(s,list))

#form ==>8 print() with replacement operator {}
name="Basava"
gf="Dingi"
salary=20000
print("Hello {0} your salary is {2} and how will maintain your gf {1} expenses".format(name,gf,salary))
print("Hello {x} your salary is {z} and how will maintain your gf {y} expenses".format(x=name,y=gf,z=salary))