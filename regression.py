import numpy as np 
import matplotlib.pyplot as plt
data_x = [1,2,2,3]
data_y = [1,2,3,6]



mean_x = np.mean(data_x)
mean_y = np.mean(data_y)

std_x = np.std(data_x,ddof=1)
var_x = std_x**2
std_y = np.std(data_y,ddof = 1)
var_y = std_y**2

n = len(data_x)
zscore_x = []
zscore_y = []
prit = lambda x,y : x+y



zscore = list(map(lambda x,y : ((x - mean_x)/std_x)*((y - mean_y)/std_y ),data_x,data_y))
zscore = list(map(lambda x,y : (x-mean_x) * (y-mean_y) ,data_x,data_y))
zscores = list(map(lambda x : x/(std_x * std_y),zscore))


# r = (1/(n-1)) * sum(zscores)
r = (1/(n-1)) * sum(zscores)
#print(r)



# slope of the line equals to r * (std_y/std_x)

m = (std_y/std_x) * r


# calculating the y intercept 
#Using y = mx + c 
# c = y - mx    y = mean(y) & x = mean(x)


c = mean_y - m * mean_x

x = np.linspace(0,6,100)
y = m*x + c

plt.scatter(data_x,data_y)
plt.plot(x, y, '-r', label='y=2x+1')

plt.show()