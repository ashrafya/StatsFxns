import numpy as np
import statistics
from scipy import stats
import pandas as pd
import matplotlib as plt
from collections import Counter

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
   
def range(data):
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
    
    

y = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
x = [2, -2, 3, 6, 9, 4, 5, -1, 0]