# """
# In any Programming language there are 2 types of errors are possible
# 1.Syntax Errors
# 2.Runtime Errors
#
# 1.Syntax Errors:
#     The Error which is occurred because of Invalid Syntax is called syntax errors.
#
# Ex:1
# x=10
# if x==10
#     print("Hello")
#
# Ex 2:
# print"Hello"
# SyntaxError: Missing parentheses in call to 'print'.
#
# 2.Runtime Error:Exceptions
# While Executing the program if something goes wrong because of the end user input or
# programming logic or memory problem etc then we will get run time errors
#
# Ex 1:
#
# print(10/0)
#
# Ex: 2
# x=int(input("Enter the Number:"))
# print(x)
# Enter the Number:ten
# ValueError: invalid literal for int() with base 10: 'ten'
#
# Note : Exception Handling Concept is applicable for Runtime Errors but not for Syntax Errors
# """
# #What is Exception:
# """
# An unwanted and unexpected event that disturbs the normal flow of a program is called as exception
#
# Ex 1:
# print(10)
# print(20)
# print(30)
# print(10/0)
# print(50)
#
# Types of Exception
#     ZeroDivisionError
#     TypeError
#     ValueError
#     FileNoFoundError
#     EOFError
#     SleepingError
#     TyrePuncherError
# """
# print(10)
# print(20)
# print(30)
# try:
#     print(10/0)
# except:
#     print("Can't Divide 10 by 0")
# print(50)
#
# """
# Exception handling does not mean repairing exception.We have to define alternative way
# to continue rest of a Program normally.
#
# IQ:
# What is Exception
# What is the Purpose of Exception Handling : The main Objective is Graceful Termination
# What is the Meaning of Exception Handling:
# """
# #Default Exception Handling in Python.
# """
# 1. Every Exception in python its an Object.For Every Exception type corresponding classes
# are available.
# 2.Whenever exception occurres internally PVM will create corresponding exception object and
# check for handling code.if handling code is not available then python interpreter will
# terminate the program abnormally and the corresponding exception info
# 3. Rest of the program will not be executed
#
# """
# #Customized Exception Handling by using try and Exceptblock:
# """
# Syntax : try:
#             Risky Code
#           except XXXX:
#             Handling Code/Alternative Code
#
# """
# #without try-except
# # print("Statement-1")
# # print(10/0)
# # print("Statement 3")
#
# #with try-except
# print("Statement-1")
#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
#
# print("Statement 3")

# #Control flow in try-except:
# """
# try:
#     stmt-1
#     stmt-2
#     stmt-3
# except XXX:
#     stmt-4
# stmt-5
#
# Case 1: If there is no exception 1,2,3,5 Normal termination
# Case 2: if there is exception rises at stmt-2, Corresponding exception handling block is matched.
#             1,4,5 Normal Termination
# Case 3: if there is exception rises at stmt-2, Corresponding exception handling block is not matching
#             1, Abnormal termination
# Case 4: if there is an exception occures at statement 4 or 5 it will be an abnormal termination.
# """
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("The Exception Raised and its description is",msg)
#
# # Try with multiple except block:
# #Ex 1:
# try:
#     x=int(input("Enter the First Number :"))
#     y=int(input("Enter the Second Number :"))
#     print(x/y)
# except ZeroDivisionError:
#     print("Can't Divide with Zero")
# except ValueError:
#     print("Please Provide the Valid input")
#
# #Ex 2:
# try:
#     x=int(input("Enter the First Number :"))
#     y=int(input("Enter the Second Number :"))
#     print(x/y)
# except ArithmeticError:
#     print("Arithmetic Error")
# except ZeroDivisionError:
#     print("Can't Divide with Zero")
#
# #SIngle Except block that can handle multiple exceptions
# try:
#     x=int(input("Enter the First Number :"))
#     y=int(input("Enter the Second Number :"))
#     print(x/y)
# except (ValueError,AttributeError,ArithmeticError,ZeroDivisionError,LookupError) as msg:
#     print(msg)

#Default Except Block:
"""
We can use default except block to handle any type of exception
We can use default except block to print normal error message
"""
# try:
#     x=int(input("Enter the First Number :"))
#     y=int(input("Enter the Second Number :"))
#     print(x/y)
#
# except ArithmeticError:
#     print("Arithmetic Error")
#
# except :
#     print("Default Except Block : Plz Provide Valid input only")


#Finally
"""
1. Its not recommended to maintain cleanup code inside try block because there
is no guarantee for the execution of every statement inside try block
2. Its not recommended to maintain cleanup code inside except block, becaus if there
is no exception then except block won't be executed.
3. Hence i want to keep my clean up code in some place, Irrespective of exception raises 
or not raises and whether its handled or not handled. Our code should be executed this is nothing 
but finally block
4.The main purpose of finally block is to maintain cleanup code.

Syntax:
try:
    Risky code
except:
    Handling Code
finally:
    cleanup code
    
"""
#Case 1 if there is no exception
try:
    print("try")
except:
    print("except")
finally:
    print("finally")

#Case 2 if there is an exception raised but handled
# try:
#     print("try")
#     print(10/0)
# except ZeroDivisionError:
#     print("except")
# finally:
#     print("finally")
#
# #Case 3 if there is an exception raised but not handled
# try:
#     print("try")
#     print(10/0)
# except NameError:
#     print("except")
# finally:
#     print("finally")
#
# #In only case finally block won't be executed. os._exit(0) ==> Entire PVM it will shutdown
# import os
# try:
#     print("try")
#     os._exit(0)
# except NameError:
#     print("except")
# finally:
#     print("finally")

#Nested try-except-finally
"""
try:    
    try:
    except 
    finally
except
finally
"""
# try:
#     print("Statement-1")
#     print("Statement-2")
#     print("Statement-3")
#     try:
#         print("Statement-4")
#         print(10 / 0)
#         print("Statement-5")
#         print("Statement-6")
#     except ValueError:
#         print("Statement-7")
#     finally:
#         print("Statement-8")
#         print("Statement-9")
#
# except ValueError:
#     print("Statement-10")
# finally:
#     print("Statement-11")
#     print("Statement-12")

#How to define and Raise customized Exception
"""
Syntax: 
class classname(predefined exception class name)
    def __init__(self,arg):
        self.arg=arg

class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
"""
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Enter the age:"))
if age>60:
    raise TooOldException("You are toold and still you can find a girl and marry")
elif age<18:
    raise TooYoungException("You are too Young and wait till you find a girl ")
else:
    print("Will get back to you with matching profile and will email you")