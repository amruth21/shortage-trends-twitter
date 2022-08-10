import pandas as pd    
import matplotlib.pyplot as plt
import numpy as np
from pytrends.request import TrendReq
pytrends = TrendReq()

def pieChart(arr):
    #print(arr)
    #print(arr.values)
    sum = 0
    y = np.array([])
    labels = arr['query'].to_numpy()
    labels = labels[0:10]

    #print(labels)
    for i in range(0,10):
        y = np.append(y, arr.iloc[i].value)
        #sum += arr.iloc[i].value

    plt.pie(y, labels = labels)
    plt.show()

    print(y)
    #print(sum)


#Pulling shortage data
pytrends.build_payload(kw_list=["shortage"],timeframe="now 1-d",geo="US")
arr = pytrends.related_queries()["shortage"]["top"]

#Cleaning dataframe
arr = arr[arr['query'].str.contains("what") == False]
arr = arr[arr['query'].str.contains("is") == False]
arr = arr[arr['query'].str.contains("how") == False]
arr['query'] = arr['query'].str.replace('2022', '')
arr = arr[arr['query'].str.contains("shortage") == True]

#Creating pieChart
pieChart(arr)


#print(arr.values)
#print(pytrends.suggestions("shortage"))


