s={10,20}
print(type(s))

s1=set()
print(type(s1))

l=[100,200,200,300,400,100,300]
s3=set(l)
print(s3)

# Important Methods
s3.add(1000)
print(s3)
s3.remove(1000)
print(s3)
#whenever i want add multiple elements then i go for update (iterable objects)
l=[10,20,30]
s3.update(l)
print(s3)

#difference between add() and update()
#copy()
s={100, 200, 10, 300, 400, 20, 30}
print(id(s))
print(s)
s1=s.copy() #clone
print(id(s1))
print(s1)

#pop()
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

#discard()
s={100, 200, 10, 300, 400, 20, 30}
s.discard(100)
print(s)
s.discard(1000)
print(s)

# difference between remove() and discard()
# difference pop(),remove() and discard()

#clear()
s.clear()
print(s)


#Mathematical operation on the set:
x={10,20,30,40}
y={30,40,50,60}

#union()
print(x.union(y))
print(y.union(x))

#intersection()
print(x.intersection(y))
print(y.intersection(x))

#difference()
print(x.difference(y))
print(y.difference(x))

#symmetric_difference()
print(x.symmetric_difference(y))

#membership operator :
s=set("qacircle")
print(s)
print('q' in s)
print('z' in s)

# Set Comprehensions by Python
s={x*x for x in range(5)}
print(s)
s1={x**2 for x in range(10,20,2)}
print(s1)

#write a program to eliminate the duplicate elements present in the list
l=["QAC","BG","QAC","BG",100,200,2021,'May',15]
s=set(l)
print(s)

#Use for loop
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)

print(l1)

#write a program to print the vowels present in the given word
vowels={'a','e','i','o','u'}
Name="qacirclesoftwaretrainingacademy"