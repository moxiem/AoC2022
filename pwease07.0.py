from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import array2string
from numpy import all
from os import getcwd
import csv
import sys


with open('input7.txt') as read_obj:
    csv_reader=csv.reader(read_obj)
    data=list(csv_reader)

#data=loadtxt('input7.txt',dtype=str)


class nelf:
    def __init__(self,name,placement=None):
        self.name=name
        self.placement=placement
        self.files=[]
        self.delf={}
        self.size=0
    def changesize(self,digit):
        self.size=self.size+digit
    def getsize(self):
        return self.size
    def getdir(self):
        return self.delf
    def getfiles(self):
        return self.files
    def getplace(self):
        return self.placement
    def adddir(self,name):
        self.delf[name]=nelf(name,placement=self)
    def addfile(self,big):
        self.files.append(big)
    def addsize(self):
        for i in self.getfiles():
            #print(i)
            self.changesize(i)
        for a in self.getdir().keys():
            self.getdir()[a].addsize()
            self.changesize(self.getdir()[a].getsize())
    def listsize(self):
        lelf=[self.getsize()]
        for a in self.getdir().keys():
            lelf=lelf+self.getdir()[a].listsize()
        return lelf

strelf=''
key='/'
num=''
current=nelf('/')

for i in data:
    strelf=i[0]
    if strelf[0]!='$':
        if strelf[0]=='d':
            num=strelf[4:]
            current.adddir(num)
            num=''
        else:
            for i in strelf:
                if i==' ':
                    break
                else:
                    num=num+i
            current.addfile(int(num))
            num=''
    else:
        if 'cd /' in strelf:
            while current.getplace()!=None:
                current=current.getplace()
        elif 'cd ..' in strelf:
            current=current.getplace()
        elif 'cd' in strelf:
            num=strelf[5:]
            current=current.getdir()[num]
            num=''
            
while current.getplace()!=None:
    current=current.getplace()
    
current.addsize()

holdlist=current.listsize()
final=0

for a in holdlist:
    if a<=100000:
        final=final+a
#current=current.getdir()['hdwsmn']
#current=current.getdir()['mrrqnc']

print(final)
