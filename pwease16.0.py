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
from sympy import Point
from sympy import Segment
from sympy import Line
import csv
import sys
import os


allv={}

class valves:
    def __init__(self,name,rate):
        self.rate=rate
        self.neighbors=[]
        allv[name]=self
    def add_n(self,neighbor):
        self.neighbors.append(neighbor)
    def get_n(self):
        return self.neighbors
    def get_rate(self):
        return self.rate
        
        
    
    


with open('input16.txt') as read_obj:
    #data=read_obj.read()
    csv_reader=csv.reader(read_obj)
    data=list(csv_reader)

#data=loadtxt('input16.txt',dtype=str)


for i in data:
    innerlist=0
    while innerlist<len(i):
        strelf=i[innerlist]
        if innerlist==0:
            nelf=strelf[6:8]
            if len(strelf)==53:
                flow=int(strelf[23:25])
                n1=strelf[51:]
                valve1=valves(nelf,flow)
                valve1.add_n(n1)
            else:
                flow=int(strelf[23])
                n1=strelf[50:]
                valve1=valves(nelf,flow)
                valve1.add_n(n1)
        else:
            valve1.add_n(strelf[1:])
        innerlist=innerlist+1

cave=zeros((60,60))
nodename=list(allv.keys())
x=0
y=0

while y<60:
    valv=nodename[y]
    while x<60:
        valv1=nodename[x]
        if valv==valv1:
            cave[y,x]=0
        elif valv1 in allv[valv].get_n():
            cave[y,x]=1
            print('!')
        else:
            cave[y,x]=float('inf')
        x=x+1
    x=0
    y=y+1

x=0
y=0
internode=0

while internode<60:
    #realnode=nodename[internode]
    while y<60:
        while x<60:
            if cave[y,internode]+cave[internode,x]<cave[y,x]:
                cave[y,x]=cave[y,internode]+cave[internode,x]
                cave[x,y]=cave[y,x]
            x=x+1
        x=0
        y=y+1
    y=0
    internode=internode+1

print(cave)





