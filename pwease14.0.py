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
from ast import literal_eval
import csv
import sys
import os

graph=zeros((1000,1000))

def rock(onex,oney,twox,twoy):
    #print(onex)
    if onex==twox:
        if oney<twoy:
            while oney<=twoy:
                graph[oney,onex]=1
                oney=oney+1
            return
        if oney>twoy:
            while oney>=twoy:
                graph[oney,onex]=1
                oney=oney-1
            return
    if oney==twoy:
        if onex<twox:
            while onex<=twox:
                graph[oney,onex]=1
                onex=onex+1
            return
        if onex>twox:
            while onex>=twox:
                graph[oney,onex]=1
                onex=onex-1
            return

def move(mx,my):
    if graph[my+1,mx]==0:
        return 1
    elif graph[my+1,mx-1]==0:
        return 2
    elif graph[my+1,mx+1]==0:
        return 3
    else:
        return 0

def sand():
    sy=0
    sx=500
    check=1
    while check!=0:
        if sy==999:
            return True
        check=move(sx,sy)
        if check==1:
            sy=sy+1
        if check==2:
            sy=sy+1
            sx=sx-1
        if check==3:
            sy=sy+1
            sx=sx+1
    graph[sy,sx]=2
    return False
  
with open('input14modified.txt') as read_obj:
    data=read_obj.read()
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

#data=loadtxt('input14.txt',dtype=str)


def parse(puzzle_input):
    return [[literal_eval(line) for line in pair.splitlines()] for pair in puzzle_input.split('\n')]

pd=parse(data)
#print(pd)

pd.pop()

for i in pd:
    #print(i)
    a=i[0]
    count=0
    while count<len(a)-3:
        x1=a[count]
        y1=a[count+1]
        x2=a[count+2]
        y2=a[count+3]
        rock(x1,y1,x2,y2)
        count=count+2
    
check1=False
fallen=0

while check1==False:
    check1=sand()
    fallen=fallen+1

print(fallen-1)
