#Creating emptly Dictionary
d={}
print(d)
print(type(d))

# Another wayof creating empty dictionary
d1=dict()
print(d1)
print(type(d1))

#add objects /Key-Value pairs to dictionary
d[100]="Basava"
d[200]="Chaitra"
d[300]="Amogh"
d[400]='Girish'
print(d)
print(d[300])

#Write a program to enter name and % of marks in dictionary and
#display the information
# x={}
# n=int(input("Enter the number of Students"))
# i=1
# while i<=n:
#     name=input("Enter the name of Student")
#     marks=input("Enter the % of Marks")
#     x[name]=marks
#     i=i+1
#
# print(x)
# print("     Name of a student","\t\t","% of Marks")
# for z in x:
#     print("\t\t",z,"\t\t",x[z])

#Update the Dictionary:
print(d)
d[100]="BG"
print(d)
d[1000]="QAC"
print(d)

#How to delete the elements from the dictionary
#del d[key]

del d[1000]
print(d)

#Clear Dictionary
# d.clear()
# print(d)

#Delete Whole Dictionary
# del d
# print(d)

#Get the Key's of a dictionary
print(d.keys())

#get the Value associated to the particular Key
print(d.get(1000))
print(d.get(100))

#Lets assign default Value
print(d.get(9000,"Hi Guest"))

#pop()
# print(d.pop(100))
# print(d)
# print(d.pop(1000))

#popitem()
# print(d)
# print(d.popitem())
# print(d)
# print(d.popitem())
# print(d)
# print(d.popitem())
# print(d)

#Get the dictionary Values ?
print(d.values())

#Use dictionary to return list of tuple representing key-value pair
#[(key,value),(key,value),(key,value)]
l=[]
for k,v in d.items():
    l.append((k,v))
print(l)

d1=d.copy()
print(d1)
print(id(d),id(d1))

#Write a program to print the sum of values by taking dictionary
#as input
# d=eval(input('Enter the dictionary'))
# s=sum(d.values())
# print("The sum of Values is =",s)

#Dictionary Comprehension:
double={x:2*x for x in range(1,6)}
print(double)