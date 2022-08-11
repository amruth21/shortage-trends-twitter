import pandas as pd    
import io
from PIL import Image as Image
import matplotlib.pyplot as plt
import matplotlib.image as Images
import numpy as np
from pytrends.request import TrendReq
pytrends = TrendReq()

#Turn PLT file into PIL Image
def createImage(plt):
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    image = Image.open(img_buf)
    return image


    '''
    im = IMG.open(img_buf)
    im.show(title="My Image")
    return im
    '''
    

    #im = Image.open(img_buf)
    #im.show(title="My Image")
    #img_buf.close()


def pieChart(arr):
    print(arr)
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

    return(createImage(plt))
    #plt.show()

    #print(y)
    #print(sum)

def pullData():
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
    return(pieChart(arr))

    #print(arr.values)
    #print(pytrends.suggestions("shortage"))


