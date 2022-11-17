import sys
import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use("Agg")

def main():
    args = sys.argv
    n = int(args[1])
    order = int(args[2])
    xrange = int(args[3])
    prange = int(args[4])
    x, y, y1 = create_data(n, xrange)
    model = myfit(x, y1, order)
    mypred(x, y, y1, model, prange)

def create_data(n, xrange):
    x = np.linspace(0, xrange, n)
    y = np.sin(2*np.pi*x)
    y1 = y + np.random.normal(0, 0.1, len(x))
    return x, y, y1

def myfit(x, y, order):
    model = np.polyfit(x, y, order)
    return model

def mypred(x, y, y1, model, pvalue):
    func = np.poly1d(model)
    pred_x = np.sort(np.random.uniform(0, pvalue, size=pvalue))
    yp = func(x)
    yv = func(pred_x)
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.plot(x, yp, color='cyan')
    plt.plot(pred_x, yv, color='red')
    plt.title("Model: " + str(len(model) - 1))
    #plt.ylim([-1, 1])
    plt.legend(["y", "y1", "yp", "yv"])
    plt_name = "graph.model." + str(len(model) - 1) + ".png"
    plt.savefig(plt_name)
    plt.show()
if __name__ == "__main__":
    main()
