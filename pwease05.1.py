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

data=loadtxt('input5.txt',dtype=str)

stack=[['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],['S', 'R', 'M', 'D', 'W', 'P', 'F'],['V', 'C', 'R', 'S', 'Z'],['R', 'T', 'J', 'Z', 'P', 'H', 'G'],['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],['G', 'C', 'V', 'B', 'P', 'Q'],['Z', 'B', 'P', 'N'],['W', 'P', 'J']]

box=0
start=0
end=0
belf=[]
final=''
pos=0

for i in data:
    box=int(i[1])
    start=int(i[3])-1
    end=int(i[5])-1
    pos=len(stack[start])-box
    belf=stack[start][pos:]
    #print(belf)
    #print(stack[start])
    del stack[start][-box:]
    #print(stack[start])
    stack[end]=stack[end]+belf
    #print(stack[end])

for i in stack:
    if i!=[]:
        final=final+i.pop()

print(final)
