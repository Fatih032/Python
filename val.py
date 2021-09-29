import math
import os
import random
import re
import sys




lst = []
 
# number of elements as input
n = int(input("Kaç sayı gireceksiniz: "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input(str(i+1)+". Sayıyı giriniz:"))
 
    lst.append(ele) # adding the element

print(lst)
     
swapcount = 0

    # Write your code here
for i in range(0, n):
    
    for i in range(0, n-1):
        if(lst[i]>lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapcount=swapcount+1
    if(swapcount==0):
        break
print("yer değiştirme sayısı :",swapcount)
print(lst)