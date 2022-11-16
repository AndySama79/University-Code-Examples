import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

# x is the training input set "x" values
# y is the array of function of x values in the 
# training data set.
# y includes the noise already.
# order is the order of polynomial for which you have to
# fit the data using polyfit.
# returns Model, as returned by the polyfit.
# also writes the model to a text file model.<order>
# this function is invoked from main
# for the x training values, and y is the values including
# the noise.
# the x value corresponds to the x data returned from
# the create data function and y value is same as y1(including noise)
# data returned from the create data function.

def myfit(x, y, order):
    model = np.polyfit(x, y, order)
    return model
    raise NotImplementedError

# n is the training data set size.
# xrange is the upper limit of x values from 0 till xrange.
# returns: x, y, y1
# y=sin(2*pi*x)
# y1 is the final noise added value using normal distribution.
# pi you can use np.pi
# sin you can use np.sin function.

def create_data(n, xrange):
    x = np.linspace(0, xrange, n)
    y = np.sin(2*np.pi*x)
    y1 = y + np.random.normal(0, 0.1, len(x))
    return x, y, y1
    raise NotImplementedError

# create validation data inputs for x
# return an nparray of size n, x values between
# 0 and prange. Use uniform distribution
# and then sort it and return.
# use only numpy sort.

def create_validation_data(n, prange):
    pred_x = np.sort(np.random.uniform(0, prange, size=n))
    return pred_x
    raise NotImplementedError

# myprediction uses the model to calcualte
# the predicted value using poly1d and
# returns the predicted value for the given
# input value of x.

def mypredict(model, x):
    func = np.poly1d(model)
    y = func(x)
    return y
    raise NotImplementedError

# Please all draw all graph related functions in the main
# function only.
# Invoke the above functions to get your program working properly.

def main():
    # your code for arg parsing
    if len(sys.argv) < 5:
        print(f'usage: {sys.argv[0]} <n> <order> <xrange> <prange>')
        sys.exit(1)
    n=int(sys.argv[1])
    order=int(sys.argv[2])
    xrange=int(sys.argv[3])
    prange=int(sys.argv[4])

    # Implement your code here. Invoke the
    # above functions properly and please draw all the
    # graph related functions in this function only. Not in the
    # individual functions above.
    
    x, y, y1 = create_data(n, xrange)
    validate_x = create_validation_data(n, prange)
    model = myfit(x, y1, order)
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.plot(x, mypredict(model, x))
    plt.plot(validate_x, mypredict(model, validate_x))
    plt.show()

if __name__ == "__main__":
    main()
