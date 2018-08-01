import numpy as np
import

def clean_list( list ) :
    clean = []
    for x in list:
        if x > 0 :
            clean.append(x)
    return clean

def generate_list(mu, sigma):
mu, sigma = 18, 10 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
s.sort()
s=clean_list(s.tolist())