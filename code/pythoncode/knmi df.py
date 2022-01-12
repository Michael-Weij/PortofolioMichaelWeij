import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

data = pd.read_csv("result.txt",header=0)
degrees = data.iloc[:,7]/10


def gap1(data,p,gap_length):
    
    index_numbers = []
    indexes = sorted(random.sample(range(len(data)),len(data)//p),reverse=True)
    for i in indexes:
        x = np.arange(1,random.randrange(gap_length[0],gap_length[1]),1)
        for a in x:
            index_numbers.append(a+i)
            data[i+a] = np.nan
    print('Total deleted data: ' + str(len(data)-np.count_nonzero(~np.isnan(data))))
    return data , index_numbers


gap_degrees, index = gap1(degrees,10,[5,10][30,100])
gap_degrees = gap_degrees.tolist()
timehour = np.arange(0,len(gap_degrees) ,1)


plt.scatter(timehour,gap_degrees)
plt.show()

