from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import array2string
from numpy import all
from os import getcwd
import csv
import sys


#with open('input7.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input8.txt',dtype=str)

up=0
down=0
left=0
right=0
#felf=False

x=1
y=1

elf=''
yelf=''
count=0
final=[]

while y<len(data)-1:
    elf=data[y]
    while x<len(elf)-1:
        up=0
        down=0
        left=0
        right=0
        count=x-1
        while count>=0:
            left=left+1
            if int(elf[count])>=int(elf[x]):
                break
            count=count-1
        count=x+1
        while count<len(elf):
            right=right+1
            if int(elf[count])>=int(elf[x]):
                break
            count=count+1
        count=y-1
        while count>=0:
            down=down+1
            yelf=data[count]
            if int(yelf[x])>=int(elf[x]):
                break
            count=count-1
        count=y+1
        while count<len(data):
            up=up+1
            yelf=data[count]
            if int(yelf[x])>=int(elf[x]):
                break
            count=count+1
        final.append((left*right*up*down))
        x=x+1
    x=1
    y=y+1
    
print(max(final))
