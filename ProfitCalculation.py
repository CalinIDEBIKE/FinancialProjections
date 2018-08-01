#libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#global variables
cpm = 0.05 # 1 cent per minute normal trip

#clean list of negative numbers
def clean_list( list ) :
    clean = []
    for x in list:
        if x > 0 :
            clean.append(x)
    return clean
    
# Random Gaussian for normal trip times
mu, sigma = 18, 10 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
s.sort()
s=clean_list(s.tolist())

#Random Gaussian for number of trips per day

mu, sigma = 3, 0.5 # mean and standard deviation
t = np.random.normal(mu, sigma, 1000)
t.sort()
t=clean_list(t.tolist())



###Calculation for trips

#Cost of a trip
def profit_per_trip( time, rate):
    return time*rate/100

def profit_per_day(rate):
    trips = math.ceil(random.choice(t))
    sumtrip = []
    for x in range(0, trips):
       sumtrip.append(profit_per_trip(random.choice(s), rate))
    return sum(sumtrip)

def profit_per_fleet_day(sizef, rate):
    fleet = []
    for x in range(0, sizef):
       fleet.append(profit_per_day(rate))
    return sum(fleet)

#Fix Values
cpm = input('Select Cents per minute \n')
cpm=float(cpm)
fleet_size = input('Select fleet size \n')
fleet_size=int(fleet_size)

print("The random trip costs : %.3f \n" % profit_per_trip(random.choice(s), cpm))
daily_income = profit_per_day(cpm)
print("The vehicle yields per day %.3f \n" % daily_income)
fleet_income_daily= profit_per_fleet_day(fleet_size, cpm)
print("The fleet of %s yields per day %.3f \n" % (fleet_size, fleet_income_daily)) 













##if(abs(mu - np.mean(s)) < 0.01)
##    print(True)
##    
##if(abs(sigma - np.std(s, ddof=1)) < 0.01)
##    print(True)


### Print Fine gaussian based on the formula
count, bins, ignored = plt.hist(t, 100, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

