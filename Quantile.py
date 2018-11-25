import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def simple_quantile(X, quantile):
    """This function just provides a working minimum example for calculating a quantile with numpy & pandas from the "standard normal" distribution
    See also https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
    X - the np.array with our realisation
    quantile - The quantiles to be calculated (as array)"""

    X.sort()              # sorts ascending
    dX = pd.DataFrame(X)  # creates a Panda DataFrame

    # Get key indicators about the realisation
    mean = np.mean(X)
    stdev = np.std(X)
 
    print("Mean: " + str(mean) +"\nStDev: " + str(stdev) +"\n=============")
  
    
    return dX.quantile(quantile)

number = 10000
sigma = 1.
mu = 0.

X =  sigma * np.random.randn(number) + mu
plt.hist(X, bins=50)
plt.show()
print(simple_quantile(X, [.1, .5, .75]))
