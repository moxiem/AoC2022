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
from os import getcwd
import csv
import sys


#with open('input10.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input12.txt',dtype=str)

end=None
alph='abcdefghijklmnopqrstuvwxyz'

class nelf:
    def __init__(self,letter,x,y):
        self.horizontal=x
        self.vertical=y
        self.neighbors=[]
        if letter=='S':
            self.value=0
            self.distance=0
        elif letter=='E':
            self.value=26
            print(str(x)+','+str(y))
            self.distance=float('inf')
        else:
            self.value=alph.index(letter)+1
            self.distance=float('inf')
    def get_neighbors(self):
        return self.neighbors
    def add_neighbors(self,node):
        if node not in self.get_neighbors():
            self.neighbors.append(node)
    def get_value(self):
        return self.value
    def get_position(self):
        return (self.horizontal,self.vertical)
    def get_distance(self):
        return self.distance
    def set_distance(self,new):
        self.distance=new

def search_by_position(pelf):
    for i in allnelf:
        if i.get_position()==pelf:
            return i
    return None

def search_by_position1(pelf):
    for i in look:
        if i.get_position()==pelf:
            return i
    return None

def search_by_value(velf):
    values=[]
    for i in allnelf:
        if i.get_value()==velf:
            values.append(i)
    return values

def find_smallest():
    a=allnelf[0]
    for b in allnelf:
        if b.get_distance()<a.get_distance():
            a=b
    return a

allnelf=[]
yelf=0
xelf=0
strelf=''

while yelf<len(data):
    strelf=data[yelf]
    while xelf<len(strelf):
        allnelf.append(nelf(strelf[xelf],xelf,yelf))
        xelf=xelf+1
    xelf=0
    yelf=yelf+1

nodelf=None

for n in allnelf:
    position=n.get_position()
    nodelf=search_by_position((position[0]+1,position[1]))
    if nodelf!=None:
        n.add_neighbors(nodelf)
    nodelf=search_by_position((position[0]-1,position[1]))
    if nodelf!=None:
        n.add_neighbors(nodelf)
    nodelf=search_by_position((position[0],position[1]+1))
    if nodelf!=None:
        n.add_neighbors(nodelf)
    nodelf=search_by_position((position[0],position[1]-1))
    if nodelf!=None:
        n.add_neighbors(nodelf)
    
look=[]

while allnelf!=[]:
    nodelf=find_smallest()
    allnelf.remove(nodelf)
    look.append(nodelf)
    for neighbor in nodelf.get_neighbors():
        if (neighbor.get_value()<=nodelf.get_value()+1) and (nodelf.get_distance()+1<neighbor.get_distance()):
            neighbor.set_distance(nodelf.get_distance()+1)

endnode=search_by_position1((43,20))

print(endnode.get_distance())

