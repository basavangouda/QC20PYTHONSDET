"""
int()
float()
str()
bool()
complex()

"""
#print("Hello")

#int() ==> we can use this function to convert from other type into int type
print(int(1234.4567))
print(int(True))
print(int(False))
print(int("10"))
print(int(0b1111))

#Here we will get error ==> ValueError: invalid literal for int()
# with base 10: '0b1111'
#print(int("0b1111"))

#Here we will get error ==> TypeError: int()
#print(int(10+5j))

#Here we will get error ==>ValueError: invalid literal for int()
# with base 10: '10.5'
#print(int("10.5"))

#Here we will get error ==>ValueError: invalid literal for int() with
# base 10: 'ten'
#print(int("ten"))
print("***********************************************************")
#Float()
print(float(10))
print(float(True))
print(float("10"))
print(float("20.7888888888888888888888888888888888888888888888888888888888"))
#print(float("ten")) #ValueError: could not convert string to float: 'ten'
#print(float("0b1111")) #ValueError: could not convert string to float: 'ob1111'
#print(float(10+8j)) #TypeError: float() argument must be a string or a real number, not 'complex'
print(float(0b1111))

#complex()
#form 1==> complex(x)
print(complex(True))
print(complex(20))
print(complex("10"))
print((complex(10.6)))
print(complex("20.7"))
#print(complex("ten")) ===>ValueError: complex() arg is a malformed string

print("***********************************************************")
#form 2 ==> complex(x,y)
print(complex(True,True))
print(complex(20,-2))
print((complex(10.6,89)))
print(complex(20.7,79))
#print(complex("ten")) ==> Value Error

print("***********************************************************")
#bool()
print(bool(10))
print(bool(-2))
print(bool(0))
print(bool(0.0))
print(bool(0.1234))
print(bool("Hello"))
print(bool(""))
print(bool(0+0j))
print(bool(0+10j))
print(bool("True"))
print(bool("False"))
print("***********************************************************")
#Str()
print(str(10))
print(str(True))
print(str(10+5j))
print(str(10.5))
print("***********************************************************")
a=256
print(id(a))
b=256
print(id(b))
c=257
print(id(c))
d=257
print(id(d))