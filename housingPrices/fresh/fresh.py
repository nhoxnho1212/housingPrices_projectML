import csv
import numpy as np
import matplotlib.pyplot as plt

FileDataNearBay='DATA/nearBay.csv'
FileOutlier='outlier.txt'
FileDataFreshTrain='DATA/freshTrain.csv'
FileDataFreshTest='DATA/freshTest.csv'
data=[]

with open(FileDataNearBay,'r') as f:
    reader=f.read()
    tmp=reader.split('\n')
    for x in tmp:
        data.append((x.split('\t'))[:-1])
    data=data[1:]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])

# longitude:A measure of how far west a house is; a higher value is farther west
longitude=[]
#latitude: A measure of how far north a house is; a higher value is farther north
latitude=[]
#housingMedianAge: Median age of a house within a block; a lower number is a newer building
housing_median_age=[]
#totalRooms: Total number of rooms within a block
total_rooms=[]
# totalBedrooms: Total number of bedrooms within a block
total_bedrooms=[]
#population: Total number of people residing within a block
population=[]
# households: Total number of households, a group of people residing within a home unit, for a block
households=[]
#medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars)
medianIncome=[]
#medianHouseValue: Median house value for households within a block (measured in US Dollars)
medianHouseValue=[]
for i in data: 
    longitude.append(i[0])
    latitude.append(i[1])
    housing_median_age.append(i[2])
    total_rooms.append(i[3])
    total_bedrooms.append(i[4])
    population.append(i[5])
    households.append(i[6])
    medianIncome.append(i[7])
    medianHouseValue.append(i[8])

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
#outlier-------------------------------------------------------
max_MedianHouseValue=max(medianHouseValue)
max_TotalRoom=max(total_rooms)
outlier_x=list()
outlier_y=list()
tmp_totalrooms=total_rooms
tmp_totalrooms.sort()
median=tmp_totalrooms[int(len(tmp_totalrooms)/2)]
arg=sum(tmp_totalrooms)/len_TotalRoom


with open(FileOutlier,'w') as fw:        
    while (abs(median-arg)>0.0071):
        #delete max value
        index_MHV=total_rooms.index(tmp_totalrooms[-1])
        textWrite=str(medianHouseValue[index_MHV])
        medianHouseValue.remove(medianHouseValue[index_MHV])
        textWrite=str((tmp_totalrooms[-1]))+" "+textWrite
        total_rooms.remove(tmp_totalrooms[-1])
        #delete min value
        index_MHV=total_rooms.index(tmp_totalrooms[0])
        medianHouseValue.remove(medianHouseValue[index_MHV])
        total_rooms.remove(tmp_totalrooms[0])

        median=tmp_totalrooms[int(len(tmp_totalrooms)/2)]
        arg=sum(tmp_totalrooms)/len(tmp_totalrooms)

        #write file
        fw.write((textWrite+"\n"))



#--------------------------------------------------------------
#write
with open(FileDataFreshTest,'w') as fTest:
    with open(FileDataFreshTrain,'w') as fTrain:
        lenx=len(total_rooms)
        check=True
        for i in range(lenx):
            if check:
                fTrain.write('%s\t%s\n'%(str(total_rooms[i]),str(medianHouseValue[i])))
            else:
                fTest.write('%s\t%s\n'%(str(total_rooms[i]),str(medianHouseValue[i])))
            check=not(check)