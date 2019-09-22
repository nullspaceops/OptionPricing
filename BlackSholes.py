import numpy as np
import scipy.stats as si
import matplotlib.pyplot as plt

def euro_vanilla(B, S, T, r, sigma, type="call"):

    #B: spot price
    #S: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    #t = 0

    d1 = (np.log(B / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(B / S) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if type == "call":
        result = (B * si.norm.cdf(d1, 0.0, 1.0) - S * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if type == "put":
        result = (S * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - B * si.norm.cdf(-d1, 0.0, 1.0))

    return result

def first_order_greeks(B, S, T, r, sigma, type="call"):

    # Still WIP

    d1 = (np.log(B / S) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(B / S) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if type == "call":
        delta = si.norm.cdf(d1, 0.0, 1.0)
    if type == "put":
        delta = si.norm.cdf(d1, 0.0, 1.0) - 1

    return delta

print(euro_vanilla(50, 100, 1, 0.05, 0.25, "put"))
print(euro_vanilla(50, 100, 1, 0.05, 0.25, "call"))
