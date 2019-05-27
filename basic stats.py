#Todos:
	#Use flat map in pyspark to identify the unique values.
	#Plot the new dataset.
	


data = "70 36 43 69 82 48 34 62 35 15 59 139 46 37 42 30 55 56 36 82 38 89 54 25 35 24 22 9 56 19"
data = data.split()

import numpy as np
data = list(map(lambda x : int(x),data))

data = np.array(data)
data.sort()

sum_ = np.sum(data)
mean = np.mean(data)

data = data.sort()
#Calculating the baisedness on the data

def calcBais(data,mean):
    bais = []
    bais = list(map(lambda x:(x,x - mean,),data))
    return bais

bais = calcBais(data,mean)


medain = np.median(data)

import matplotlib.pyplot as plt

plt.hist(data,bins=11)

