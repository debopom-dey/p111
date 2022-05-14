import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["id"].to_list()
datamean = statistics.mean(data)
std_deviation_data = statistics.stdev(data)

print("Mean of the data is {}".format(datamean))
print("Standard Deviation of the data is {}".format(std_deviation_data))

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,1000):
    SetOfMean = randomSetOfMean(100)
    meanlist.append(SetOfMean)

std_deviation = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)

df = pd.read_csv("Book1.csv")
data = df["reading_time"].to_list()
meanOfSample = statistics.mean(data)
print("Mean of Sampling Distribution", meanOfSample)

fig = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name="Standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name="Standard deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name="Standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name="Standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name="Standard deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name="Standard deviation 3 end"))
fig.show()

zScore = (meanOfSample - mean)/std_deviation
print("Z Score is = ", zScore)