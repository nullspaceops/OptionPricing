import numpy as np
import matplotlib.pyplot as plt

# Number of Paths and Timesteps
paths = 1000
n = 100
T = 1
delta = T/n
t = np.arange(1,step=delta)

# Initial values and structures
# res for final values
S = np.zeros(n)
res = np.zeros(paths)
S0 = 0
S[0] = S0

# Z Variable, N(0,1) for Martingale
# Mean mu and standard deviation sigma
mu = 0.0
sigma = 1.0

# Creates an array for iteration. 
# It will look like [1.,2.,3......n-1,n]
x = range(1, len(S))

# This function simulates one path, see Rüdiger Seydel
def wiener():

    for iter in x:

        dW = np.random.normal(mu, sigma)
        dt = np.sqrt(delta)
        dS = dW*dt
        S[iter] = S[iter-1] + dS

    plt.plot(t,S)
    return S[iter]

for i in range(1,paths+1):

    # Saves the final value of each path
    res[i-1] = wiener()

print("Mean is: " + str(np.sum(res)/len(res)))

plt.xlim(0)
plt.show()