import numpy as np
import statistics
from scipy import stats
import pandas as pd
import matplotlib as plt
from collections import Counter
import plotly.express as px

def mean(data):
    '''
    takes a list and outputs the mean
    '''
    total=0
    for i in range(len(data)):
        total += data[i]
    return total/len(data)

def sample_size(data):
    '''
    returns the sample size
    '''
    return len(data)

def median(data):
    '''
    returns median of data
    deals with odd and even numbers automatically
    '''
    return statistics.median(data)

def trimmed_mean(data, cap):
    '''
    data == data
    cap == teh percentage cap (input in decimal values)
    calculates trimmed mean with percentage cap
    '''
    return stats.trim_mean(data, cap)
   
def range_mine(data):
    '''
    returns range of a data set
    '''
    return max(data) - min(data)
    
def maxMin(data):
    '''
    returns max and min of a dataset
    list --> [max, min]
    '''
    return [max(data), min(data)]

def variance(data):
    '''
    ASSUMING FOR A SAMPLE --> if whole population then use pvariance
    returns variance of a dataset
    '''
    # return statistics.pvariance(data)
    return statistics.variance(data)

def standardDev(data):
    '''
    ASSUMING FOR A SAMPLE --> if whole population then use pvariance
    returns standard deviation of a data set
    '''
    # return statistics.pstdev(data)
    return statistics.stdev(data)    

def plot_histogram(data):
    '''
    takes a list as an input and outputs histogram drawn using matplotlib
    '''
    recounted = Counter(data)
    plt.pyplot.hist(data, bins=len(recounted))  # bins is the length of the dictionary, or how many frequency units there are
    plt.pyplot.ylabel('No of times')
    plt.pyplot.show()
    
    
def relativeFreq(data):
    '''
    returns a relative frequency graph
    '''
    a = np.array(data) # convert to np array
    recounted = Counter(data) # count how many colunns to have by making dict
    res = stats.relfreq(a, numbins=len(recounted))
    res.frequency #freq array
    
    x = res.lowerlimit + np.linspace(0, res.binsize*res.frequency.size, 
                                     res.frequency.size)
    fig = plt.pyplot.figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(x, res.frequency, width=res.binsize)
    ax.set_title('Relative frequency histogram')
    ax.set_xlim([x.min(), x.max()])
    plt.pyplot.show()    
    
    
def dotPlot(data):
    '''
    returns dot plot of data
    '''
    indices =[]
    new = sorted(data)
    print(new)
    recounted = Counter(new)
    for val in recounted:
        for i in range(recounted[val]):
            indices.append(i+1)    
    plt.pyplot.scatter(new, indices)
    plt.pyplot.ylim(0,5)
    plt.pyplot.show()

def get_percentile(data, number):
    return np.percentile(data, number)

f1 = [3,1,4,1,5,9,2,6,5,3,5,8]