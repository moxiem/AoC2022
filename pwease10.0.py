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


with open('input10.txt') as read_obj:
    csv_reader=csv.reader(read_obj)
    data=list(csv_reader)

#data=loadtxt('input10.txt',dtype=str)

signal=[20,60,100,140,180,220]
cycle=1
strength=[]
strelf=''
reg=1

for i in data:
    strelf=i[0]
    if strelf=='noop':
        if cycle in signal:
            strength.append(cycle*reg)
        cycle=cycle+1
    else:
        if strelf[5]=='-':
            if cycle in signal:
                strength.append(cycle*reg)
            cycle=cycle+1
            if cycle in signal:
                strength.append(cycle*reg)
            cycle=cycle+1
            reg=reg-int(strelf[6:])
        else:
            if cycle in signal:
                strength.append(cycle*reg)
            cycle=cycle+1
            if cycle in signal:
                strength.append(cycle*reg)
            cycle=cycle+1
            reg=reg+int(strelf[5:])

print(sum(strength))
