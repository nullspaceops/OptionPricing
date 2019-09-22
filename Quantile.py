import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats
import seaborn as sns

def simple_quantile(X, quantile):
    """This function just provides a working minimum example for calculating a quantile with numpy & pandas from the "standard normal" distribution
    See also https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
    X - the np.array with our realisation
    quantile - The quantiles to be calculated (as array)"""

    dX = pd.DataFrame(X)  # creates a Panda DataFrame

    # Get key indicators about the realisation
    mean = np.mean(X)
    stdev = np.std(X)
 
    print("Mean: " + str(mean) +"\nStDev: " + str(stdev) +"\n=============")
  
    
    return dX.quantile(quantile)

number = 2000000
sigma = 1.
mu = 0.

X =  sigma * np.random.randn(number) + mu
plt.hist(X, bins=50, density=True)
sns.distplot(X);
plt.show()
print(simple_quantile(X, [.01, .1, .5, .75, .99]))
