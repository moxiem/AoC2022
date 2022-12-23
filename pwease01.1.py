from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import all
import csv


with open('input.txt') as read_obj:
    csv_reader=csv.reader(read_obj)
    data=list(csv_reader)

elf=0
calories=[0]

for i in data:
    if i==[]:
        calories.append(0)
        elf=elf+1
    else:
        calories[elf]=calories[elf]+int(i[0])

onelf=max(calories)

calories.remove(onelf)

twelf=max(calories)

calories.remove(twelf)

threlf=max(calories)

calories.remove(threlf)

print(onelf+twelf+threlf)
