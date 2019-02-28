import csv
import numpy as np


data=[]
with open('./DATA/fresh.csv','r') as f:
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

len_TotalRoom=len(total_rooms)

total_rooms=np.array([total_rooms]).T
one = np.ones((total_rooms.shape[0], 1))
X = np.concatenate((one,total_rooms), axis = 1)
y=np.array([medianHouseValue]).T

#cal
b=np.dot(X.T,y)
A=np.dot(X.T,X)
transposeOfA=np.linalg.pinv(A)
theta=np.dot(transposeOfA,b)

#lostfunc
y=y.T
total_rooms=total_rooms.T
l=0.0
for i in range(len_TotalRoom):
    l+=(y[0][i]-(theta[0][0]+theta[1][0]*total_rooms[0][i]))**2

l*=(1/(2*len_TotalRoom))
#
with open('result.txt','w') as f:
    f.write('lost function: %s\n%s %s' %(str(l),str(theta[0][0]),str(theta[1][0])))

