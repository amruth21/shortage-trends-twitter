import pandas as pd    
import io
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as Images
import seaborn as sns
import numpy as np
from pytrends.request import TrendReq
pytrends = TrendReq()

#Turn PLT file into PIL Image
def createImagefromPLT(plt):
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    plt.clf()
    img_buf.seek(0)
    image = Image.open(img_buf)
    return image

#Generates MatPlotLib pie chart
def pieChart(arr):
    sum = 0
    y = np.array([])
    labels = arr['query'].to_numpy()
    labels = labels[0:10]

    #In edge cases with not enough queries
    max = 10
    if(len(arr) < max):
        max = len(arr)

    for i in range(0,max):
        y = np.append(y, arr.iloc[i].value)
        #sum += arr.iloc[i].value

    plt.pie(y, labels = labels)

    return(createImagefromPLT(plt))

#Generates MatPlotLib bar chart
def barChart(arr):
    sum = 0
    y = np.array([])
    #Grabs top 10 labels(queries)
    labels = arr['query'].to_numpy()
    labels = labels[0:10]

    #In edge cases with not enough queries
    max = 10
    if(len(arr) < max):
        max = len(arr)

    for i in range(0,max):
        y = np.append(y, arr.iloc[i].value)
        #sum += arr.iloc[i].value

    plt.xticks(fontsize=6, rotation=330)
    plt.bar(labels, y)

    return(createImagefromPLT(plt))

#Generate plotly bubble plot
def bubblePlot(arr):
    x = arr['query'].to_numpy()[0:10]
    values = arr['value'].to_numpy()[0:10]

    x = x[::-1]
    values = values[::-1]

    fig = go.Figure(data=[go.Scatter(
        x=x, y=[0,10,20,30,40,50,60,70,80,90],
        mode='markers',
        text=x,
        marker=dict(
            color=values,
            size=values,
            showscale=True
            )
    )])
    fig.update_yaxes(visible=False)

    #Convert to image then PIL image
    fig_bytes = fig.to_image(format="png")
    buf = io.BytesIO(fig_bytes)
    img = Image.open(buf)
    return img

#Uses Google-Trends API to grab raw data
def pullData(geo):
    #Pulling shortage data
    pytrends.build_payload(kw_list=["shortage"],timeframe="now 1-d",geo=geo)
    arr = pytrends.related_queries()["shortage"]["top"]

    #Cleaning dataframe
    arr = arr[arr['query'].str.contains("what") == False]
    arr = arr[arr['query'].str.contains("is") == False]
    arr = arr[arr['query'].str.contains("how") == False]
    arr = arr[arr['query'].str.contains(geo) == False]
    arr['query'] = arr['query'].str.replace('2022', '')
    arr = arr[arr['query'].str.contains("shortage") == True]
    return arr





