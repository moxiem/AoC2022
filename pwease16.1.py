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
from copy import copy
import csv
import sys
import os
import re


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
        
class path:
    def __init__(self,time,initial):
        self.time=time
        self.visited=[initial]
        self.pressure=0
    def copy(self,newinitial):
        newpath=path(self.time,newinitial)
        newpath.pressure=self.pressure
        newpath.visited=newpath.visited+self.visited.copy()
        return newpath
    def getvisited(self):
        return self.visited
    def gettime(self):
        return self.time
    def subtracttime(self,subtract):
        self.time=self.time-subtract
    def addpressure(self,add):
        self.pressure=self.pressure+add
    def getpressure(self):
        return self.pressure
   
def getnextvalve(currentpath):
    nodenelf=[]
    for k in nodename:
        if k not in currentpath.getvisited():
            nodenelf.append(k)
    return nodenelf

def complete(total,stop=False):
    firstcave='AA'
    firstpath=path(total,firstcave)
    stack=[firstpath]
    completepaths=[]
    while stack!=[]:
        cpath=stack.pop(0)
        if stop:
            completepaths.append(cpath)
        newpaths=[]
        for nex in getnextvalve(cpath):
            nextnum=bridge[nex]
            curnum=bridge[cpath.getvisited()[0]]
            if cpath.gettime()-(cave[curnum,nextnum]+1)<=0:
                continue
            nextpath=cpath.copy(nex)
            nextpath.subtracttime(cave[curnum,nextnum]+1)
            flow=allv[nextpath.getvisited()[0]].get_rate()
            nextpath.addpressure((cpath.gettime()-(cave[curnum,nextnum]+1))*flow)
            newpaths.append(nextpath)
        if newpaths!=[]:
            stack=stack+newpaths
        else:
            if not stop:
                completepaths.append(cpath)
    return completepaths


with open('input16.txt','r') as read_obj:
    #data=read_obj.read()
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)
    lines=map(str.strip,read_obj.readlines())

for l in lines:
    labels=re.findall('[A-Z]{2}',l)
    search=re.findall('[0-9]+',l)[0]
    flo=int(search)
    newvalve=valves(labels[0],flo)
    t=1
    while t<len(labels):
        newvalve.add_n(labels[t])
        t=t+1

#data=loadtxt('input16.txt',dtype=str)


cave=zeros((60,60))
nodenam=list(allv.keys())
x=0
y=0
bridge={}

while y<60:
    valv=nodenam[y]
    bridge[valv]=y
    while x<60:
        valv1=nodenam[x]
        if valv==valv1:
            cave[y,x]=0
        elif valv1 in allv[valv].get_n():
            cave[y,x]=1
        else:
            cave[y,x]=float('inf')
        x=x+1
    x=0
    y=y+1

x=0
y=0
internode=0

while internode<60:
    while y<60:
        while x<60:
            if cave[y,internode]+cave[internode,x]<cave[y,x]:
                cave[y,x]=cave[y,internode]+cave[internode,x]
                cave[x,y]=cave[y,internode]+cave[internode,x]
            x=x+1
        x=0
        y=y+1
    y=0
    internode=internode+1

nodename=[]

for i in nodenam:
    if allv[i].get_rate()!=0:
        nodename.append(i)

c=complete(26,True)
p={}
vi={}
please=[]
countelf=0

#print(len(c))

for i in c:
    v=i.getvisited()
    if 'AA' in v:
        v.remove('AA')
    p=i.getpressure()
    for t in c:
        vt=t.getvisited()
        if 'AA' in vt:
            vt.remove('AA')
        pt=t.getpressure()
        if set(v).isdisjoint(set(vt)) and p+pt>2000:
            please.append(p+pt)
    
print(max(please))
