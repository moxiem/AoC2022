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


lelf=[]

class sensor:
    def __init__(self,sx,sy,bx,by):
        self.hori=sx
        self.vert=sy
        self.dis=abs(sx-bx)+abs(sy-by)
        p1=Point(self.hori,self.vert+self.dis)
        p2=Point(self.hori+self.dis,self.vert)
        p3=Point(self.hori,self.vert-self.dis)
        p4=Point(self.hori-self.dis,self.vert)
        s1=Segment(p1,p2)
        s2=Segment(p2,p3)
        s3=Segment(p3,p4)
        s4=Segment(p4,p1)
        self.perimeter=[s1,s2,s3,s4]
    def get_edges(self):
        return self.perimeter
    def in_boundary(self,newx,newy):
        newdis=abs(self.hori-newx)+abs(self.vert-newy)
        if newdis<=self.dis:
            return True
        else:
            return False

def checkpos(cx,cy):
    for i in lelf:
        if i.in_boundary(cx,cy)==True:
            return False
    return True


#with open('input14modified.txt') as read_obj:
    #data=read_obj.read()
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input15.txt',dtype=str)


for i in data:
    x1=i[2]
    y1=i[3]
    x2=i[8]
    y2=i[9]
    num1=int(x1[2:len(x1)-1])
    #print(num1)
    num2=int(y1[2:len(y1)-1])
    #print(num2)
    n1=int(x2[2:len(x2)-1])
    #print(n1)
    n2=int(y2[2:len(y2)])
    #print(n2)
    lelf.append(sensor(num1,num2,n1,n2))
    
inter=[]

for l in lelf:
    edge1=l.get_edges()
    for k in lelf:
        if lelf.index(l)!=lelf.index(k):
            edge2=k.get_edges()
            for e1 in edge1:
                for e2 in edge2:
                    point=e1.intersection(e2)
                    if point!=[] and Line.are_concurrent(e1,e2):
                        inter.append(point[0])

inter=[*set(inter)]
posch=[]

for t in inter:
    stx=str(t[0])
    sty=str(t[1])
    if '/' not in stx and '/' not in sty:
        ix=int(stx)
        iy=int(sty)
        posch.append((ix+1,iy))
        posch.append((ix-1,iy))
        posch.append((ix,iy+1))
        posch.append((ix,iy-1))

posch=[*set(posch)]
relf=[]

for pos in posch:
    px=pos[0]
    py=pos[1]
    if 0<=px<=4000000 and 0<=py<=4000000:
        relf.append(pos)

for pos2 in relf:
    px=pos2[0]
    py=pos2[1]
    if checkpos(px,py)==True:
        final=pos2

finx=final[0]
finy=final[1]

print(finx*4000000+finy)
    

