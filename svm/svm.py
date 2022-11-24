import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# call create data to create a uni dimensional data.
# returns a matrix for x 
# first column as "1", second column will be  x,
# third - x^2, fourth - x^3

# global reg
# reg=0.01

# return the gradient 
# in this case it will be nparray of xorder+1
# should be same as 'w' as we will
# adjust w based on this.

def mysvmdata(n):
    X, y = datasets.make_classification(n_samples=n, n_features=2, 
                                        n_informative=2, n_redundant=0, n_classes=2, 
                                        n_clusters_per_class=1, class_sep=5.0, hypercube=False, scale=1)
    X = np.insert(X, 0, np.ones((1, n)), axis=1)
    y = np.where(y == 0, -1, 1)
    return X, y

def mygradient(x,y,n,w):
    yp = np.matmul(x, w)
    z = y * yp
    gradient = 0
    for i in range(n):
        if z[i] < 1:
            gradient = gradient + (-y[i] * x[i, :])
    gradient = gradient / n
    return gradient

# calculate the cost. 
# single value
def hinge(z):
    if z >= 1:
        return 0
    else:
        return 1 - z

def mycost(x,y,n,w):
    yp = np.matmul(x, w)
    z = y * yp
    # loss = np.vectorize(hinge)

    # hinge_loss = np.vectorize(hinge)
    # cost = np.mean(hinge_loss(z))
    # cost = np.mean(loss(z))
    for i in range(n):
        if z[i] >= 1:
            z[i] = 0
        else:
            z[i] = 1 - z[i]
    # hinge_loss = np.vectorize(hinge)
    # cost = np.mean(hinge_loss(z))
    cost = np.sum(z) / n
    return cost

# x,y - training set
# niter- iterations to run in gradient desceint.
# winit - initial w values
# lr - learning rate
# reg - regularizer constant
# returns:
# cl - list cost for every iteration.
# it - iteration no. in a list. simply 0.. niter
# w - final value of w
# c - Final cost

def run_gradient(x, y, n, niter, winit, lr, reg):
    cl = []
    it = []
    c = 0
    w = winit
    for i in range(niter):
        w = w - (lr * (mygradient(x, y, n, w) + ((reg * (w)))) )
        c = mycost(x, y, n, w) + (reg / (2)) * (np.sum(np.power(w, 2))) 

        cl.append(c)
        it.append(i)
    return cl, it, w, c

def main():
    pd.options.display.max_columns = None
    pd.options.display.width=None
    pd.options.display.max_rows=None
    pd.options.display.max_colwidth=None

    if len(sys.argv) < 5:
        print(f'usage: {sys.argv[0]} <n> <niter> <lr> <reg>')
        sys.exit()
    n = int(sys.argv[1])
    niter = int(sys.argv[2])
    lr = float(sys.argv[3])
    reg = float(sys.argv[4])

    # x, y = mysvmdata(n)

    df = pd.read_csv(r'case1.csv')
    y = df['Y'].to_numpy()
    x = df.drop(columns=['Y']).to_numpy()
    n = len(y)
    print(x)
    print(y)

    print(x.shape)
    order = x.shape[1]
    print(f'n:{n},order:{order}')
    w=np.ones(order)
    print(w)

    print(f'cost:{mycost(x,y,n,w)}')
    print(mygradient(x,y,n,w))
    plt.scatter(x[:, 1][ y == -1 ], x[:, 2][ y == -1 ], color='red', label="class 1")
    plt.scatter(x[:, 1][ y == 1 ], x[:, 2][ y == 1 ], color='cyan', label="class 2")
    plt.legend()
    plt.show()

    clist, iter, w, c = run_gradient(x, y, n, niter, w, lr, reg)
    
    plt.plot(iter,clist,'-o', label='cost')
    plt.legend()
    plt.show()
    print(f'AFTER ITERATIONS:cost:{c}')
    print(x[:,1])

    w1=np.flip(w)
    x_n = np.arange(-4, 4, 1)
    y_n = (-w[1] / w[2]) * x_n - w[0] / w[2]
    y_n2 = (-w[1] / w[2]) * x_n - (w[0]-1) / w[2]
    y_n1 = (-w[1] / w[2]) * x_n - (w[0]+1) / w[2]

    plt.scatter(x[:, 1][ y == -1 ], x[:, 2][ y == -1 ], color='red', label="class 1")
    plt.scatter(x[:, 1][ y == 1 ], x[:, 2][ y == 1 ], color='cyan', label="class 2")
    plt.plot(x_n, y_n, '-b',label="SVM")
    plt.plot(x_n, y_n1, '-g',label="Support 1")
    plt.plot(x_n, y_n2, '-g',label="Support 2")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.legend()
    plt.show()
    print(f'w_i:{w} w_f: {w1}')
    print(f'equation: {w[0]}+{w[1]}x+{w[2]}y')
    
if __name__ == "__main__":
    main()
 