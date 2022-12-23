from numpy import loadtxt
from numpy import size
from numpy import delete
from numpy import array
from numpy import arange
from numpy import shape
from numpy import all
import csv


#with open('input3.txt') as read_obj:
    #csv_reader=csv.reader(read_obj)
    #data=list(csv_reader)

data=loadtxt('input3.txt',dtype=str)

length=0
ruck='a'
sack='b'
common=[]
priority=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
prisum=0

for i in data:
    length=int(len(i)/2)
    ruck=i[:length]
    sack=i[length:]
    #if len(ruck)==len(sack):
        #print('ttt')
    common=list(set(ruck)&set(sack))
    #print(priority.index(common[0]))
    prisum=prisum+priority.index(common[0])+1

print(prisum)
