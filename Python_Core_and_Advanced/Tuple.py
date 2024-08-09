t=10,20,30,40
print(t)
print(type(t))

#create empty tuple
t1=()
print(type(t1))

list=[100,200,300]
t2=tuple(list)
print(t2)

# Mathematical Operation
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
t4=t1*4
print(t4)

t=(40,50,60,2,899,43)
t1=sorted(t)
print(t1)

t2=sorted(t,reverse=True)
print(t2)

print(min(t2))
print(max(t2))

#Tuple Packing and Unpacking:
#Tuple packing means here we are packing the variables in to tuple
a=10
b=20
c=30
d=80
t=a,b,c,d
print(t)
print(type(t))

# Tuple unpacking means we are assigning the tuple values to different variables.
w,x,y,z=t
print(w,z)

#Tuple comprehensions: It is not supported by Python
t=(x**2 for x in range(1,6))
print(t)
print(type(t))
for i in t:
    print(i)

