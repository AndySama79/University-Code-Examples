# IMPLEMENT run gradient for SVM.
# 
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
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
# from svm import *

def mygradient(x,y,n,w):
    yp = np.matmul(x, w)
    z = y * yp
    gradient = 0
    for i in range(n):
        if z[i] < 1:
            gradient = gradient + (-y[i] * x[i, :])
    gradient = gradient / n
    return gradient

def mycost(x,y,n,w):
    yp = np.matmul(x, w)
    z = y * yp
    for i in range(n):
        if z[i] >= 1:
            z[i] = 0
        else:
            z[i] = 1 - z[i]
    # hinge_loss = np.vectorize(hinge)
    # cost = np.mean(hinge_loss(z))
    cost = np.sum(z) / n
    return cost

def run_gradient(x,y,n,niter, winit, lr, reg):
    cl = []
    it = [0]
    c = 0
    cl.append(mycost(x, y, n, w))
    w = winit
    for i in range(niter-1):
        w = w - (lr * (mygradient(x, y, n, w) + ((reg * (w)))) )
        c = mycost(x, y, n, w) + (reg / (2)) * (np.sum(np.power(w, 2))) 

        cl.append(c)
        it.append(i)
    return cl, it, w, c

def main():
    global reg
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
    c = mycost(x, y, n, w)
    m = mygradient(x, y, n, w)
    # print(hw(x,y,n,w))
#    c,hl=mycost(x,y,n,w)
    print(f'cost:{c}')
#    m=mygradient(x,y,n,w,hl)
    print(f'Gradient: {m}, {m.shape}')
#    sys.exit(1)
    #plt.plot(x[:,1], f, "-o",label='func')
    #plt.plot(x[:,1], y, "-o",label='noise')
    #plt.legend()
    #plt.show()
#    sys.exit(1)
    clist,iter,w,c = run_gradient(x,y,n,niter,w,lr,reg)
    ClassAIndices=np.where(y==-1)
    ClassAIndices=ClassAIndices[0].tolist()
    ClassBIndices=np.where(y==1)
    ClassBIndices=ClassBIndices[0].tolist()

    t1=x[:,1]
    t2=x[:,2]
    XclassA=x[ClassAIndices,:]
    XclassB=x[ClassBIndices,:]
    YclassA=y[ClassAIndices]
    YclassB=y[ClassBIndices]
#    yclassA=t2[ClassAIndices]
#    yclassB=t2[ClassBIndices]
    plt.scatter(XclassA[:,1],XclassA[:,2], color='blue', marker='x', label='Class A')
    plt.scatter(XclassB[:,1],XclassB[:,2], color='red', marker='o', label='Class B') 
    plt.xlabel('X1 feature') 
    plt.ylabel('X2 feature') 
    myx=np.arange(-4.0,4.0,0.1)
    plt.plot(myx, (-(w[1]/w[2])*myx-w[0]/w[2]), '-b', label='pline')
    plt.plot(myx, (-(w[1]/w[2])*myx-(w[0]-1)/w[2]), '-g', label='pline')
    plt.plot(myx, (-(w[1]/w[2])*myx-(w[0]+1)/w[2]), '-g', label='pline')
    plt.xlim([-4,4])
    plt.ylim([-4,4])
    plt.legend()
    plt.savefig('finalFigure.png')
    plt.show()


    plt.plot(iter,clist,'-o', label='cost')
    plt.legend()
    plt.show()
    plt.savefig('finalcostFigure.png')
    print(f'AFTER ITERATIONS:cost:{c}')
    #myprint(x[:,1])
    #w1=np.flip(w)
    #yp=mypredict(w1, x[:,1])
    #plt.plot(x[:,1], f, "-o",label='func')
    #plt.plot(x[:,1], y, "-o",label='noise')

    print(f'FINAL ITERATIONS: {niter} LR: {lr} LAMBDA: {reg}')
    print(f'FINAL COST: {c}')
    print(f'FINAL W: {w}')
    finalc, finalhz = mycost(x,y,n,w)
    print(f'finalc:{finalc} finalhz:{finalhz}')
    print(f'finalx: {x}')
    print(f'finaly: {y}')
    print(f'class a: {XclassA} Y: {YclassA}')
    print(f'class b: {XclassB} Y: {YclassB}')
    myz=[]
    print(f'len: {len(x)}')
    for i in range(len(x)):
        print(x[i])
        m=w[0]+x[i][1]*w[1]+x[i][2]*w[2]
        m=m*y[i]
        myz.append(m)

    print(f'myZ: {myz}')
    print(f'myfinalhl: {finalhz}')
    print(f'classa indices: {ClassAIndices} classb: {ClassBIndices}')
#    print(f'{XclassA[:,1],XclassA[:,2]}')
    t1=XclassA[:,1]
    t2=XclassA[:,2]
    for i in range(len(t1)):
        print(f'{t1[i],t2[i]},',  end="")    
    print("")
    t1=XclassB[:,1]
    t2=XclassB[:,2]
    for i in range(len(t1)):
        print(f'{t1[i],t2[i]},',  end="")    
    print("")
    print(f'equation: {w[0]}+{w[1]}x+{w[2]}y')
#    print(f'{XclassB[:,1],XclassB[:,2]}')

    print(f'FINAL W: {w}')


if __name__ == '__main__':
    main()