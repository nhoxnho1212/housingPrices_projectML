import csv
import numpy as np
import matplotlib.pyplot as plt

DataTrainFile='./DATA/freshTrain.csv'
ResultTrainFile='ResultTrain.txt'
DataTestFile='./DATA/freshTest.csv'

data=[]
with open(DataTrainFile,'r') as f:
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

data=[]
with open(DataTrainFile,'r') as f:
    reader=f.read()
    tmp=reader.split('\n')
    for x in tmp:
        data.append((x.split('\t')[:]))
    data.pop()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])

for i in data: 
    total_rooms.append(i[0])
    medianHouseValue.append(i[1])
#norm
len_TotalRoom=len(total_rooms)
arg_TotalRoom=sum(total_rooms)/len_TotalRoom
max_TotalRoom=max(total_rooms)
min_TotalRoom=min(total_rooms)
for i in range(len_TotalRoom):
    total_rooms[i]=(total_rooms[i]-arg_TotalRoom)/(max_TotalRoom-min_TotalRoom)

len_MedianHouseValue=len(medianHouseValue)
max_MedianHouseValue=max(medianHouseValue)
min_MedianHouseValue=min(medianHouseValue)
arg_MedianHouseValue=sum(medianHouseValue)/len_MedianHouseValue
for i in range(len_MedianHouseValue):
    medianHouseValue[i]=(medianHouseValue[i]-arg_MedianHouseValue)/(max_MedianHouseValue-min_MedianHouseValue)

#--------------------------------------------------------------
theta=[]
with open('./ResultTrain.txt','r') as f:
    reader=f.read()
    
    readstring=reader.split('\n')
    x=readstring[1].split(' ')
    theta.append(float(x[0]))
    theta.append(float(x[1]))

#plot data
lin=np.array([min(total_rooms),max(total_rooms)])

def J(x,theta):
    return theta[0]+theta[1]*x
costf=J(lin,theta)

#plt.plot(medianHouseValue,longitude,'r.',label='longitude')
#plt.plot(medianHouseValue,latitude,'g.',label='latitude')
#plt.plot(medianHouseValue,housing_median_age,'g.',label='housing Median age')
plt.plot(total_rooms,medianHouseValue,'c.',label='total rooms')
plt.plot(lin,costf,'r')
#plt.plot(medianHouseValue,total_bedrooms,'m.',label='total bedrooms')
#plt.plot(medianHouseValue,population,'y.',label='population')
#plt.plot(medianHouseValue,households,'k.',label='households')
#plt.plot(medianHouseValue,medianIncome,'r.',label='median income')
#plt.plot(total_rooms,total_bedrooms,'r.')
plt.ylabel('median House value')
plt.xlabel('total rooms')
plt.axis([min(total_rooms), max(total_rooms), min(medianHouseValue), max(medianHouseValue)])
plt.legend()
plt.show()


