from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import all
import csv


#with open('input4.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input4.txt',dtype=str)

lonelf=0
honelf=0
twelfl=0
twelfh=0
elf=0
temp=''
pairs=0

for i in data:
    while i[elf]!='-':
        temp=temp+i[elf]
        elf=elf+1
    lonelf=int(temp)
    temp=''
    elf=elf+1
    while i[elf]!=',':
        temp=temp+i[elf]
        elf=elf+1
    honelf=int(temp)
    temp=''
    elf=elf+1
    while i[elf]!='-':
        temp=temp+i[elf]
        elf=elf+1
    twelfl=int(temp)
    temp=''
    elf=elf+1
    while elf<len(i):
        temp=temp+i[elf]
        elf=elf+1
    twelfh=int(temp)
    temp=''
    elf=0
    if (honelf<=twelfh and lonelf>=twelfl) or (twelfh<=honelf and lonelf<=twelfl):
        pairs=pairs+1

print(pairs)
