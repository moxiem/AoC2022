from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import all
import csv


#with open('input2.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input2.txt',dtype=str)

score=0
foe='b'
outcome='c'
elf=0

for i in data:
    foe=i[0]
    outcome=i[1]
    if outcome=='X':
        if foe=='A':
            elf=3
        if foe=='B':
            elf=1
        if foe=='C':
            elf=2
        score=score+elf
    if outcome=='Y':
        if foe=='A':
            elf=1
        if foe=='B':
            elf=2
        if foe=='C':
            elf=3
        score=score+elf+3
    if outcome=='Z':
        if foe=='A':
            elf=2
        if foe=='B':
            elf=3
        if foe=='C':
            elf=1
        score=score+elf+6

print(score)
        
