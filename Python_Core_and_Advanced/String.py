#How to access the string Characters
#1. By using indexing
#2. By using slice operator [2:-1]
# s="QACircle"
# print(s[:5])

#WAP to access characters of a string in a forward direction and backword direction
# print("====forward direction=======")
# i=0
# n=len(s)
# while i<n:
#     print(s[i],end='')
#     i+=1
# print()
# print("====backword direction=======")
# i=-1
# n=len(s)
# while i>=-n:
#     print(s[i],end='')
#     i-=1


#Checking membership operator
# s=input("Enter the string")
# sub=input("Enter the sub string")
# if sub in s:
#     print("Test Pass")
# else:
#     print("Test Fail")

#Removing space from the string
# s="     QACircle"
# print(s)
# s2=s.lstrip()
# print(s2)
#
# s3="QACircle      "
# print(s3)
# s4=s3.rstrip()
# print(s4)
#
# s5="       QACircl123                "
# s6=s5.strip()
# print(s6)

#Find the substring
# s="Welcome to QACircle Software Training Academy"
# print(s.find("qacircle"))
# print(s.find("Soft"))

#index(): index() works exactly same as find() but it will through error
#if the substring is not available
# s="Welcome to QACircle Software Training Academy"
# sub=input("Enter the Sub String")
#print(s.index(sub)) ==> ValueError

# try:
#     n=s.index(sub)
#     print(n)
# except:
#     print("Sub String is not found")
# else:
#     print("String Found")

#counting substring in the given string
s="Welcome to QACircle Software Training Academy"
sub='a'
print(s.count(sub))

s1="aaaabababbabbbbbabbaababbabba"
print(s1.count("ab"))
print(s1.count("abb"))
print(s1.count("aa"))
print(s1.count("aaa"))

#Replacing of String with another String
s="Learning Python coding is Very Very difficult"
print(s)
s1=s.replace("difficult","Easy")
print(s1)
print(id(s),"=====",id(s1))

#Splitting of String
s="Learning Python coding is Very Very Easy"
l=s.split()
print(l)
for i in l:
    print(i)

s1="02-07-2024"
x=s1.split("-")
print(x)

#Joining of a String
"""
Syntax= s=separator.join(group of string) 

Group of String ==list, tuple etc
"""
l=["sunny","Bunny","Chinni"]
x="=".join(l)
print(x)

t="hyderabad",'Bangalore',"Chennai",'Mumbai'
s=":".join(t)
print(s)

#Changing the Case of a String
s="QACircle Software Training Academy"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())

#Check the type of Character present in a string :
s1="1233445qacircle$"
s2=""
s3="1234"
s4="1234hhdsnsxf"
print(s1.isalnum())
print(s4.isalnum())
print(s3.islower())
print(s3.isnumeric())
print(s2.isupper())
print(s2.isspace())

#Checking the starting and ending part of the string
s="QACircle Software Training Academy"
print(s.startswith("academy"))
print(s.startswith("QAC"))
print(s.startswith("Q"))
print(s.startswith("QACircle"))
print(s.endswith("Academy"))

#Formatting the String
# name="BG"
# wife="Kavya"
# bg_age=30
# salary=10000
# print(name,wife,bg_age,salary)
# print('Hi {} your wife name is {} and your age is {} and your Monthly salry is {}'.format(salary,bg_age,name,wife))
# print('Hi {2} your wife name is {3} and your age is {1} and your Monthly salry is {0}'.format(salary,bg_age,name,wife))

#Some Programs related to String
# input="QACircle"
# Output="elcriCAQ"

#Approach 1
# print(input[::-1])

#Approach 2
# print("".join(reversed(input)))

#Approach 3
# for i in input[::-1]:
#     print(i,end='')
# print()

#Approach 4
# i=len(input)-1
# target=""
# while i>=0:
#     target=target+input[i]
#     i=i-1
# print(target)

#Write a Program to Reverese order of Words
# input="Learning Python is Very Easy"
# output="Easy Very is Python Learning"
# l=input.split()
# print(l)
# i=len(l)-1
# l1=[]
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# print(l1)
# Output=" ".join(l1)
# print(Output)


#Write a Program to Reverese the content of each Words
input="Learning Python is Very Easy"
output="gninraeL nohtyP si yreV ysaE"
l=input.split()
print(l)
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
print(l1)
Output=" ".join(l1)
print(Output)

#WAP to print characters present in Odd position and Even position from the given string
s="QACircle"
print("Characters Present in the Even position",s[0::2])
print("Characters Present in the Odd position",s[1::2])
