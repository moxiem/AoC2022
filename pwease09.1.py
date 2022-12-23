from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import array2string
from numpy import all
from numpy import zeros
from os import getcwd
import csv
import sys

def oblivion(hay,hax,tay,tax):
    if abs(hay-tay)<=1 and abs(hax-tax)<=1:
        return (tay,tax)
    elif hay==tay and hax<tax:
        return (tay,tax-1)
    elif hay==tay and hax>tax:
        return (tay,tax+1)
    elif hax==tax and hay<tay:
        return (tay-1,tax)
    elif hax==tax and hay>tay:
        return (tay+1,tax)
    elif hax>tax and hay>tay:
        return (tay+1,tax+1)
    elif hax>tax and hay<tay:
        return (tay-1,tax+1)
    elif hax<tax and hay>tay:
        return (tay+1,tax-1)
    else:
        return (tay-1,tax-1)
    
#with open('input7.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input9.txt',dtype=str)

pain=zeros((1000,1000))

hy=[500,500,500,500,500,500,500,500,500,500]
hx=[500,500,500,500,500,500,500,500,500,500]

knot=1
step=0
darkin=None

for i in data:
    step=0
    if i[0]=='U':
        while step<int(i[1]):
            hy[0]=hy[0]+1
            knot=1
            while knot<10:
                darkin=oblivion(hy[knot-1],hx[knot-1],hy[knot],hx[knot])
                #print(darkin)
                hy[knot]=darkin[0]
                hx[knot]=darkin[1]
                knot=knot+1
            step=step+1
            pain[hy[9],hx[9]]=1
    if i[0]=='D':
        while step<int(i[1]):
            hy[0]=hy[0]-1
            knot=1
            while knot<10:
                darkin=oblivion(hy[knot-1],hx[knot-1],hy[knot],hx[knot])
                #print(darkin)
                hy[knot]=darkin[0]
                hx[knot]=darkin[1]
                knot=knot+1
            step=step+1
            pain[hy[9],hx[9]]=1
    if i[0]=='R':
        while step<int(i[1]):
            hx[0]=hx[0]+1
            knot=1
            while knot<10:
                darkin=oblivion(hy[knot-1],hx[knot-1],hy[knot],hx[knot])
                #print(darkin)
                hy[knot]=darkin[0]
                hx[knot]=darkin[1]
                knot=knot+1
            step=step+1
            pain[hy[9],hx[9]]=1
    if i[0]=='L':
        while step<int(i[1]):
            hx[0]=hx[0]-1
            knot=1
            while knot<10:
                darkin=oblivion(hy[knot-1],hx[knot-1],hy[knot],hx[knot])
                #print(darkin)
                hy[knot]=darkin[0]
                hx[knot]=darkin[1]
                knot=knot+1
            step=step+1
            pain[hy[9],hx[9]]=1

count=0
x=0
y=0

while y<1000:
    while x<1000:
        if pain[y,x]==1:
            count=count+1
        x=x+1
    x=0
    y=y+1

print(count)
        
