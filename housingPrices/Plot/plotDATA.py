import csv
import numpy as np
import matplotlib.pyplot as plt


data=[]
with open('DATA/nearBay.csv','r') as f:
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


#plt.plot(medianHouseValue,longitude,'r.',label='longitude')
#plt.plot(medianHouseValue,latitude,'g.',label='latitude')
#plt.plot(medianHouseValue,housing_median_age,'g.',label='housing Median age')
#plt.plot(medianHouseValue,total_rooms,'c.',label='total rooms')
#plt.plot(medianHouseValue,total_bedrooms,'m.',label='total bedrooms')
#plt.plot(medianHouseValue,population,'y.',label='population')
#plt.plot(medianHouseValue,households,'k.',label='households')
#plt.plot(medianHouseValue,medianIncome,'r.',label='median income')
plt.plot(total_rooms,total_bedrooms,'r.')
plt.xlabel('total rooms')
plt.ylabel('total bedrooms')
plt.legend()
plt.show()
        



