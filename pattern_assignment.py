# -*- coding: utf-8 -*-
"""PATTERN ASSIGNMENT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AblM8MSUUYBWrUmEjS9em1vMcSGPZrG9
"""

# 1>
n=5
for i in range(1,n+1):
  num=65
  for j in range(1,i+1):
    print(chr(num),end=" ")
    num+=1
  print()

n=1
for i in range(1,5):
  for j in range(1,i+1):
    if j==1 or i==j:
      print(n,end=" ")
      n+=2
    else:
      print(" ",end=" ")
  print()

n=5
for i in range(n):
  for j in range(i+1):
    if (i+j)%2==0:
      print("1",end=" ")
    else:
      print("0",end=" ")
  print()

n=5
for i in range(n):
  for j in range(i+1):
    if j%2==0:
      print("1",end=" ")
    else:
      print("0",end=" ")
  print()

n=5
for i in range(1,n+1):
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,2*i):
    print("*",end=" ")
  print()

n=5
for i in range(1,n+1):
  for s in range(n-i):
    print(" ",end="")
  for j in range(1,i+1):
    print("*",end=" ")
  print()

n=1
for i in range(1,6):
  for j in range(1,i+1):
    if i==5 or j==1 or i==j:
      print(n,end=" ")
      n+=1
    else:
      print(" ",end=" ")
  print()

n=4
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==1 or i==4 or  j==1  or j==4:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=4
for i in range(1,n+1):
  for j in range(1,n+2):
    if i==1 or i==4 or j==1 or j==5:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=5
num=65
for i in range(1,n+1):
  for j in range(1,i+1):
    print(chr(num),end=" ")
  num+=1
  print()

n=4
for row in range(1,n):
  for col in range(1,row+1):
    print("*",end=" ")
  print()
for row in range(n,0,-1):
  for col in range(1,row+1):
    print("*",end=" ")
  print()

n=4
for i in range(1,n):
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,i+1):
    print("*",end=" ")
  print()
for i in range(n,0,-1):
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,i+1):
    print("*",end=" ")
  print()

n=5
for i in range(n,0,-1):
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,2*i):
    print(j,end=" ")
  print()
for i in range(2,n+1):
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,2*i):
    print(j,end=" ")
  print()

n=5
for i in range(n,0,-1):
  num=65
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,2*i):
    print(chr(num),end=" ")
    num+=1
  print()
for i in range(2,n+1):
  num=65
  for s in range(n-i):
    print(" ",end=" ")
  for j in range(1,2*i):
    print(chr(num),end=" ")
    num+=1
  print()

n=5
for i in range(1,n+1):
  for j in range(1,2*n):
    if  i==5 or j==5 or i+j==6 or j-i==4:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=4
for i in range(n,0,-1):
  for j in range(1,i+1):
    print("*",end=" ")
  for s in range(2*(n-i)):
    print(" ",end=" ")
  for j in range(i,0,-1):
    print("*",end=" ")
  print()
for i in range(n):
  for j in range(i+1):
      print("*",end=" ")
  for s in range(2*(n-i-1)):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")

  print()

n=5
mylist=[]
for i in range(n):
  temp=[]
  for j in range(i+1):
    if j==0 or j==i:
      temp.append(1)
    else:
      temp.append(mylist[i-1][j-1]+mylist[i-1][j])
  mylist.append(temp)
print(mylist)

for i in range(n):
  for s in range(n-i-1):
    print(" ",end="")
  for j in range(i+1):
    print(mylist[i][j],end=" ")
  print()