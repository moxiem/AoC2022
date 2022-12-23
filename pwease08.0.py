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

up=True
down=True
left=True
right=True
#felf=False

x=1
y=1

elf=''
yelf=''
count=0
final=0

while y<len(data)-1:
    elf=data[y]
    while x<len(elf)-1:
        up=True
        down=True
        left=True
        right=True
        count=0
        while count<x:
            if int(elf[count])>=int(elf[x]):
                left=False
            count=count+1
        count=x+1
        while count<len(elf):
            if int(elf[count])>=int(elf[x]):
                right=False
            count=count+1
        count=0
        while count<y:
            yelf=data[count]
            if int(yelf[x])>=int(elf[x]):
                down=False
            count=count+1
        count=y+1
        while count<len(data):
            yelf=data[count]
            if int(yelf[x])>=int(elf[x]):
                up=False
            count=count+1
        if left==True or right==True or down==True or up==True:
            final=final+1
            #felf=True
            #print(elf[x])
        x=x+1
        felf=False
    x=1
    y=y+1
    
#print(final)
final=final+((len(data)-1)*2)+((len(elf)-1)*2)
print(final)
