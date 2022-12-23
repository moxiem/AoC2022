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
item0=[52, 78, 79, 63, 51, 94]
inspect1=0
item1=[77, 94, 70, 83, 53]
inspect2=0
item2=[98, 50, 76]
inspect3=0
item3=[92, 91, 61, 75, 99, 63, 84, 69]
inspect4=0
item4=[51, 53, 83, 52]
inspect5=0
item5=[76, 76]
inspect6=0
item6=[75, 59, 93, 69, 76, 96, 65]
inspect7=0
item7=[89]

roun=0
nostyle=None
nograce=0

while roun<10000:
    while item0!=[]:
        nograce=item0.pop(0)
        if nograce>9699690 and nograce%9699690!=0:
            nograce=nograce%9699690
        nostyle=funkykong(nograce,'*',13,5)
        if nostyle[1]==True:
            item1.append(nostyle[0])
        else:
            item6.append(nostyle[0])
        inspect0=inspect0+1
    while item1!=[]:
        nograce=item1.pop(0)
        nostyle=funkykong(nograce,'+',3,7)
        if nostyle[1]==True:
            item5.append(nostyle[0])
        else:
            item3.append(nostyle[0])
        inspect1=inspect1+1
    while item2!=[]:
        nograce=item2.pop(0)
        nostyle=funkykong(nograce,'*',nograce,13)
        if nostyle[1]==True:
            item0.append(nostyle[0])
        else:
            item6.append(nostyle[0])
        inspect2=inspect2+1
    while item3!=[]:
        nograce=item3.pop(0)
        nostyle=funkykong(nograce,'+',5,11)
        if nostyle[1]==True:
            item5.append(nostyle[0])
        else:
            item7.append(nostyle[0])
        inspect3=inspect3+1
    while item4!=[]:
        nograce=item4.pop(0)
        nostyle=funkykong(nograce,'+',7,3)
        if nostyle[1]==True:
            item2.append(nostyle[0])
        else:
            item0.append(nostyle[0])
        inspect4=inspect4+1
    while item5!=[]:
        nograce=item5.pop(0)
        nostyle=funkykong(nograce,'+',4,2)
        if nostyle[1]==True:
            item4.append(nostyle[0])
        else:
            item7.append(nostyle[0])
        inspect5=inspect5+1
    while item6!=[]:
        nograce=item6.pop(0)
        nostyle=funkykong(nograce,'*',19,17)
        if nostyle[1]==True:
            item1.append(nostyle[0])
        else:
            item3.append(nostyle[0])
        inspect6=inspect6+1
    while item7!=[]:
        nograce=item7.pop(0)
        nostyle=funkykong(nograce,'+',2,19)
        if nostyle[1]==True:
            item2.append(nostyle[0])
        else:
            item4.append(nostyle[0])
        inspect7=inspect7+1
    roun=roun+1

monkeys=[inspect0,inspect1,inspect2,inspect3,inspect4,inspect5,inspect6,inspect7]
count=max(monkeys)

monkeys.remove(count)
final=count*max(monkeys)

print(final)

