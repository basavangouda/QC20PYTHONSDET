#10 Pattern 10
""""
EDCBA
EDCBA
EDCBA
EDCBA
EDCBA
"""
n=int(input("Enter the number"))
for i in range(1,n+1):
   for j in range(1,n+1):
      print(chr(65+n-j),end='')
   print()
