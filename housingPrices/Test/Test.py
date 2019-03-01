import csv
import numpy as np

DataTestFile='./DATA/freshTest.csv'
ResultTrainFile='ResultTrain.txt'
ResultTestFile='ResultTest.txt'

data=[]
theta=[]
LF_Test=0.0
LF_Train=0.0
DiffLF=0.0

with open(DataTestFile,'r') as f:
    reader=f.read()
    tmp=reader.split('\n')
    for x in tmp:
        data.append((x.split('\t')[:]))
    data.pop()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])


#totalRooms: Total number of rooms within a block
total_rooms=[]

#medianHouseValue: Median house value for households within a block (measured in US Dollars)
medianHouseValue=[]

for i in data: 
    total_rooms.append(i[0])
    medianHouseValue.append(i[1])

with open(ResultTrainFile,'r') as FRead:
    reader=FRead.read()
    tmp=reader.split('\n')
    theta.append(float(tmp[1].split(' ')[0]))
    theta.append(float(tmp[1].split(' ')[1]))
    LF_Train=float(tmp[0].split(' ')[2])

#lost func
len_TotalRoom=len(total_rooms)
for i in range(len_TotalRoom):
    LF_Test+=(medianHouseValue[i]-(theta[0]+theta[1]*total_rooms[i]))**2

LF_Test*=(1/(2*len_TotalRoom))

DiffLF=abs(LF_Test-LF_Train)

with open(ResultTestFile,'w') as fw:
    fw.write(str(DiffLF))
    