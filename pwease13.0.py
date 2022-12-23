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


with open('input13.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    data=read_obj.read()

#data=loadtxt('input13.txt',dtype=str)

def parse(puzzle_input):
    return [[literal_eval(line) for line in pair.splitlines()] for pair in puzzle_input.split('\n\n')]

def funcelf(thing1,thing2):
    if type(thing1)==int and type(thing2)==int:
        if thing1<thing2:
            return 1
        elif thing2<thing1:
            return 0
        else:
            return 2
    elif type(thing1)==list and type(thing2)==list:
        copy1=thing1.copy()
        copy2=thing2.copy()
        while copy1!=[] and copy2!=[]:
            ele1=copy1.pop(0)
            ele2=copy2.pop(0)
            check=funcelf(ele1,ele2)
            if check!=2:
                return check
        if copy1==[] and copy2!=[]:
            return 1
        elif copy1!=[] and copy2==[]:
            return 0
        else:
            return 2
    elif type(thing1)==list:
        return funcelf(thing1,[thing2])
    else:
        return funcelf([thing1],thing2)

def ino():
    kelf=0
    while kelf<len(unpd)-1:
        if funcelf(unpd[kelf],unpd[kelf+1])==0:
            return False
        kelf=kelf+1
    return True

pd=parse(data)
final=0
unpd=[]

for i in pd:
    first=i[0]
    second=i[1]
    #print(first)
    #print(second)
    unpd.append(first)
    unpd.append(second)

unpd.append([[2]])
unpd.append([[6]])

while ino()==False:
    countelf=0
    while countelf<len(unpd)-1:
        onelf=unpd[countelf]
        twelf=unpd[countelf+1]
        if funcelf(onelf,twelf)==0:
            unpd[countelf]=twelf
            unpd[countelf+1]=onelf
        countelf=countelf+1

index1=unpd.index([[2]])+1
index2=unpd.index([[6]])+1

print(index1*index2)

#print(pd[0])
#print(pd[1])
