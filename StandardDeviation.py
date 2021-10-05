import csv
import math

with open('data.csv',newline='')as f:
    reader = csv.reader(f)
    fileData = list(reader)

newData = fileData[0]

def mean(newData):
    n = len(newData)
    Total = 0
    for x in newData:
        Total = Total+int(x) 
        
    mean = Total/n  
    return mean   

SquaredList = [] 
for number in newData:
    a = int(number) - mean(newData)
    a = a**2
    SquaredList.append(a)  

sum = 0 

for i in SquaredList:
    sum = sum + i

result = sum/len(newData)-1
StanDev = math.sqrt(result)

print(StanDev)