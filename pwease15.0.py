from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import array2string
from numpy import all
from numpy import zeros
from math import floor
from ast import literal_eval
import csv
import sys
import os

unav=[]

def combine(r1,r2):
    start1=r1[0]
    start2=r2[0]
    end1=r1[1]
    end2=r2[1]
    if start1<=start2<=end1<=end2:
        return (start1,end2)
    if start2<=start1<=end2<=end1:
        return (start2,end1)
    if start2<=start1<=end1<=end2:
        return (start2,end2)
    if start1<=start2<=end2<=end1:
        return (start1,end1)
    return (0,0)

def beacon(sx,sy,bx,by):
    dis=abs(sy-by)+abs(sx-bx)
    ydis=abs(sy-2000000)
    xdis=dis-ydis
    if xdis<=0:
        return
    else:
      unav.append((sx-xdis,sx+xdis))  

def comb():
    for a in unav:
        for b in unav:
            if unav.index(b)!=unav.index(a) and b!=None and a!=None:
                c=combine(a,b)
                if c!=(0,0):
                    unav.remove(a)
                    unav.remove(b)
                    unav.append(c)
                    return False
    return True

#with open('input14modified.txt') as read_obj:
    #data=read_obj.read()
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input15.txt',dtype=str)

for i in data:
    x1=i[2]
    y1=i[3]
    x2=i[8]
    y2=i[9]
    num1=int(x1[2:len(x1)-1])
    #print(num1)
    num2=int(y1[2:len(y1)-1])
    #print(num2)
    n1=int(x2[2:len(x2)-1])
    #print(n1)
    n2=int(y2[2:len(y2)])
    #print(n2)
    beacon(num1,num2,n1,n2)

check=False

while check==False:
    check=comb()

final=0
#print(unav)

for f in unav:
    final=final+(f[1]-f[0])

print(final)
    

