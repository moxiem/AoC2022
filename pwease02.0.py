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
me='a'
foe='b'
elf=0

for i in data:
    foe=i[0]
    me=i[1]
    if(me=='X' and foe=='C') or (me=='Y' and foe=='A') or (me=='Z' and foe=='B'):
        if(me=='X'):
            elf=1
        elif(me=='Y'):
            elf=2
        else:
            elf=3
        score=score+elf+6
    if(me=='Y' and foe=='C') or (me=='Z' and foe=='A') or (me=='X' and foe=='B'):
        if(me=='X'):
            elf=1
        elif(me=='Y'):
            elf=2
        else:
            elf=3
        score=score+elf+0
    if(me=='Y' and foe=='B') or (me=='Z' and foe=='C') or (me=='X' and foe=='A'):
        if(me=='X'):
            elf=1
        elif(me=='Y'):
            elf=2
        else:
            elf=3
        score=score+elf+3

print(score)
