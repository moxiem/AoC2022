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
from os import getcwd
import csv
import sys


def funkykong(value,op,num,div):
    if op=='*':
        value=value*num
    else:
        value=value+num
    #value=floor(value/3)
    if value%div==0:
        return (value,True)
    else:
        return (value,False)

#with open('input10.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

#data=loadtxt('input10.txt',dtype=str)

inspect0=0
item0=[79, 98]
inspect1=0
item1=[54, 65, 75, 74]
inspect2=0
item2=[79, 60, 97]
inspect3=0
item3=[74]

roun=0
nostyle=None
nograce=0

while roun<10000:
    while item0!=[]:
        nograce=item0.pop(0)
        if nograce>96577 and nograce%96577!=0:
            nograce=nograce%96577
        nostyle=funkykong(nograce,'*',19,23)
        if nostyle[1]==True:
            item2.append(nostyle[0])
        else:
            item3.append(nostyle[0])
        inspect0=inspect0+1
    while item1!=[]:
        nograce=item1.pop(0)
        nostyle=funkykong(nograce,'+',6,19)
        if nostyle[1]==True:
            item2.append(nostyle[0])
        else:
            item0.append(nostyle[0])
        inspect1=inspect1+1
    while item2!=[]:
        nograce=item2.pop(0)
        nostyle=funkykong(nograce,'*',nograce,13)
        if nostyle[1]==True:
            item1.append(nostyle[0])
        else:
            item3.append(nostyle[0])
        inspect2=inspect2+1
    while item3!=[]:
        nograce=item3.pop(0)
        nostyle=funkykong(nograce,'+',3,17)
        if nostyle[1]==True:
            item0.append(nostyle[0])
        else:
            item1.append(nostyle[0])
        inspect3=inspect3+1
    roun=roun+1

monkeys=[inspect0,inspect1,inspect2,inspect3]
count=max(monkeys)

monkeys.remove(count)
final=count*max(monkeys)

print(final)

