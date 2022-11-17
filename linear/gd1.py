import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ml1 import *

# call create data to create a uni dimensional data.
# returns a matrix for x 
# first column as "", second column will be 
def mydata(n, order, xrange):
    xt, y, y1 = create_data(n, xrange)
    # x is a matrix as described above.
    # y is the function value returned by create data.
    # y1 is the simulated data with noise returned by create data.
    x = pd.DataFrame()
    for i in range(0, order+1):
        head = 'x' + str(i)
        x[head] = np.power(xt, i)
    x = x.to_numpy()
    return x, y, y1

global reg
reg=0.01

# return the gradient 
# in this case it will be nparray of xorder+1
# should be same as 'w' as we will
# adjust w based on this.

def mygradient(x,y,n,w):
    yp = np.matmul(x, w)
    gradient = np.matmul(yp - y, x) / n
    return gradient

# calculate the cost. 
# single value
def mycost(x,y,n,w):
    yp = np.matmul(x, w)
    cost = np.sum(np.power((yp - y), 2)) / (2 * n)
    return cost

def main():
    global reg
    pd.options.display.max_columns = None
    pd.options.display.width=None
    pd.options.display.max_rows=None
    pd.options.display.max_colwidth=None
    if len(sys.argv) < 8:
        print(f'usage: {sys.argv[0]} <n> <order> <xrange> <prange> <niter> <lr> <reg>')
        sys.exit(1)
    niter=1000000
    lr=0.005
    n=int(sys.argv[1])
    order=int(sys.argv[2])
    xrange=int(sys.argv[3])
    prange=int(sys.argv[4])
    niter=int(sys.argv[5])
    lr=float(sys.argv[6])
    reg=float(sys.argv[7])
    x,f,y=mydata(n, order,xrange)
    print(x)
    print(y)
    n=len(x)
    print(x.shape)
    order=x.shape[1]
    print(f'n:{n},order:{order}')
    w=np.ones(order)
    #w=np.zeros(order)
#    w=[ 23.84414518, -36.7656487,   13.38952765,  -0.40729235]
    #w=[ -0.40729235,13.38952765, -36.7656487,  23.84414518 ]
    #w=[ 100.0,100.0,100.0,100.0 ]
    print(w)
    #print(hw(x,y,n,w))
    print(f'cost:{mycost(x,y,n,w)}')
    print(mygradient(x,y,n,w))
    plt.plot(x[:,1], f, "-o",label='func')
    plt.plot(x[:,1], y, "-o",label='noise')
    plt.legend()
    plt.show()

    #sys.exit(1)
    clist=[]
    iter=[]
    c=0
    for i in range(niter):
        w1=w
        w=w-lr*mygradient(x,y,n,w)
        c=mycost(x,y,n,w)
#        if i > 0 and c > clist[i-1]:
#            print(f'BREAKING DUE to cost INCREASE oldcost: {clist[i-1]} new: {c}')
#            w=w1
#            break
        clist.append(c)
        iter.append(i)
    #    print(f'iter:{i} cost:{c}')

    plt.plot(iter,clist,'-o', label='cost')
    plt.legend()
    plt.show()
    print(f'AFTER ITERATIONS:cost:{c}')
    print(x[:,1])
    w1=np.flip(w)
    yp=mypredict(w1, x[:,1])
    plt.plot(x[:,1], f, "-o",label='func')
    plt.plot(x[:,1], y, "-o",label='noise')
    s=f'm={order-1}'
    plt.plot(x[:,1], yp, "-o", label=s)
#    plt.plot(xv, yvp, "-o", label='m=validation')
    plt.legend()
    plt.show()
    print(f'w:{w} w1: {w1}')
    

if __name__ == "__main__":
    main()
