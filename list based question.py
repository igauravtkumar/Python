# -*- coding: utf-8 -*-
"""24 oct.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iUEmRrOd2-kupkT9o-zECjzfJmBg8-TG
"""

#monotanic=> increasing and decresing order

x=0
list=[11,10,12,13]
for index in range(1,len(list)):
  if(list[index])>list[index-1]:
    x=1
    break
if x==1:
  print("not monotonic")

x=0
list=[11,10,9,8]
for index in range(1,len(list)):
  if(list[index])>list[index-1]:
    x=1
    break
  elif (list[index])<list[index-1]:
    x=0
    break
if x==1:
  print("not monotonic")
else:
  print("monotonic")

x=0
list=[1,2,3,4]
for index in range(1,len(list)):
  if(list[index])<list[index-1]:
    x=1
    break
  elif (list[index])>list[index-1]:
    x=0
    break
if x==1:
  print("not monotonic")
else:
  print("monotonic")

#disarium number 89=8**1 + 9**2
num=int(input("Enter The Number :"))
temp=num
a=temp
sum=0
count=0
while num>0:
  num=num//10
  count+=1
count
while temp>0:
  rem=temp%10
  sum=sum+rem**count
  temp=temp//10
  count-=1
if sum==a:
  print("disarium number")
else:
  print("not")

#harshad number ==>
num=int(input("enter the number :"))
temp=num
sum=0
while num>0:
  rem=num%10
  sum=sum+rem
  num=num//10
  div=temp%sum==0
div