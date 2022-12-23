from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import array2string
from numpy import all
import csv


#with open('input4.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input6.txt',dtype=str)

trelf=False
trf=True
felf=1
strelf=''
temp=array2string(data)

#print(temp)

while trelf==False:
    if felf>=14:
        strelf=temp[felf-13:felf+1]
        trf=False
        for i in strelf:
            if strelf.count(i)>1:
                trf=True
    if trf==False:
        trelf=True
    felf=felf+1

print(felf-1)
    
