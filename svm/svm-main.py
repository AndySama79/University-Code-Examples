def mysvmdata(n):
#    x,y=datasets.make_classification(n_samples=20,n_features=2, n_informative=2, n_redundant=0, n_repeated=0)
    sep=1.5
    x,y=datasets.make_classification(n_samples=n,n_features=2, n_informative=2, n_redundant=0, n_repeated=0,class_sep=sep)
#    print(x)
#    print(y)
    myvf=np.vectorize(myf)
    y1=myvf(y)
#    print(y1)
    df=pd.DataFrame(data=x, columns=['x1', 'x2'])
    myprint(df)
    df.insert(0, 'x0', 1)
    x=df.values
    df['Y'] = y1
    df.to_csv('idata.csv', index=False)
#    print(df)
#    print(f'x:{x}')
    return x,y1

def myfdata(fname):
    df =pd.read_csv(fname)
    myprint(df.describe())
    y=df.values[:,-1]
    df1=df.drop(['Y'],axis=1)
    x=df1.values
    myprint(x)
    myprint(y)
#    sys.exit(1)
    return x,y

def main():
    global reg
    pd.options.display.max_columns = None
    pd.options.display.width=None
    pd.options.display.max_rows=None
    pd.options.display.max_colwidth=None
    if len(sys.argv) < 5:
        print(f'usage: {sys.argv[0]} <n> <niter> <lr> <reg>')
        sys.exit(1)
    niter=1000000
    lr=0.005
    n=int(sys.argv[1])
    niter=int(sys.argv[2])
    lr=float(sys.argv[3])
    reg=float(sys.argv[4])
    readf=''
    if len(sys.argv) == 6:
        myprint('readf?')
        readf=sys.argv[5]
    if readf != '':
        x,y=myfdata(readf)
    else:
        x,y=mysvmdata(n)
        f=y
    myprint(x)
    myprint(y)
    n=len(x)
    myprint(x.shape)
    order=x.shape[1]
    myprint(f'n:{n},order:{order}')
    w=np.ones(order)
    #w=np.zeros(order)
    #w=np.zeros(order)
#    w=[ 23.84414518, -36.7656487,   13.38952765,  -0.40729235]
    #w=[ -0.40729235,13.38952765, -36.7656487,  23.84414518 ]
    #w=[ 100.0,100.0,100.0,100.0 ]
    myprint(w)
    myprint(hw(x,y,n,w))
#    c,hl=mycost(x,y,n,w)
    myprint(f'cost:{c}')
#    m=mygradient(x,y,n,w,hl)
    myprint(f'Gradient: {m}, {m.shape}')
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
    myprint(f'AFTER ITERATIONS:cost:{c}')
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
    #plot_cost_function(x,y,n,w)
    

if __name__ == "__main__":
    main()

