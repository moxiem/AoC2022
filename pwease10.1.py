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


def line(cy):
    if cy<40:
        return (0,cy)
    elif cy<80:
        return (1,cy-40)
    elif cy<120:
        return (2,cy-80)
    elif cy<160:
        return (3,cy-120)
    elif cy<200:
        return (4,cy-160)
    else:
        return (5,cy-200)

with open('input10.txt') as read_obj:
    csv_reader=csv.reader(read_obj)
    data=list(csv_reader)

#data=loadtxt('input10.txt',dtype=str)

crt=zeros((6,40))
cycle=0
strelf=''
reg=1
sprite=[]
elf=None

for i in data:
    strelf=i[0]
    if strelf=='noop':
        sprite=[reg-1,reg,reg+1]
        elf=line(cycle)
        if elf[1] in sprite:
            crt[elf[0],elf[1]]=1
        cycle=cycle+1
    else:
        if strelf[5]=='-':
            sprite=[reg-1,reg,reg+1]
            elf=line(cycle)
            if elf[1] in sprite:
                crt[elf[0],elf[1]]=1
            cycle=cycle+1
            sprite=[reg-1,reg,reg+1]
            elf=line(cycle)
            if elf[1] in sprite:
                crt[elf[0],elf[1]]=1
            cycle=cycle+1
            reg=reg-int(strelf[6:])
        else:
            sprite=[reg-1,reg,reg+1]
            elf=line(cycle)
            if elf[1] in sprite:
                crt[elf[0],elf[1]]=1
            cycle=cycle+1
            sprite=[reg-1,reg,reg+1]
            elf=line(cycle)
            if elf[1] in sprite:
                crt[elf[0],elf[1]]=1
            cycle=cycle+1
            reg=reg+int(strelf[5:])

print(crt)

