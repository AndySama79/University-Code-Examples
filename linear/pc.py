import math
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

myprint_enabled=0
def myprint(msg):
    if myprint_enabled:
        print(msg)


# x1 - two dimensional np array feature vector each is a list of points each with length equal to dimension.
# y1 - label or classification value -1 or +1. It is nparray of values
# niter - no. of iterations perceptron has to run
# th - theta values in np array
# t0 - offset in the perceptron linear equation
# start_index - the starting index for the iteration instead of starting from index 0.
# offset - is t0 to be calculated or not. If offset is 0, the return value for t0 wont
# be considered as valid.
# return values: total mistakes, theta, theta0

def run_perceptron(x1, y1, niter, th, t0, start_index, offset):
    #   initialization
    total_mistakes = 0
    convergence = 0  #   assumption
    thetas = []
    #   logic for perceptron: updating th, t0, total_mistakes
    while convergence != 1:
  
        for i in range(start_index, len(y1)):
            if y1[i] * (np.sum(np.dot(th, x1[i])) + t0) <= 0:
                th = th + y1[i] * x1[i]
                total_mistakes += 1
                if offset != False or offset != 0:
                    t0 += y1[i]
            thetas.append(list(th))

        for i in range(0, start_index):
            if y1[i] * (np.sum(np.dot(th, x1[i])) + t0) <= 0:
                th = th + y1[i] * x1[i]
                total_mistakes += 1
                if offset != False or offset != 0:
                    t0 += y1[i]
            thetas.append(list(th))
        
        for i in range(len(y1)):
            if y1[i] * (np.sum(np.dot(th, x1[i])) + t0) <= 0:
                convergence = 0
                break
            convergence = 1

        # niter = niter - 1

    # for i in range(len(y1)):
    #     if y1[i] * (np.sum(np.dot(th, x1[i])) + t0) <= 0:
    #         convergence = 0
    #         break

    return convergence, total_mistakes, th, t0, thetas

def main():
    # generate your own points in two dimensions
    # and see how the line should be
    # run perceptron and see what it gives
    # vary the starting point, offset etc.,
    # and see what you get.
    # it will be good to plot the resulting line !
    pd.options.display.max_columns = None
    pd.options.display.width=None
    pd.options.display.max_rows=None
    pd.options.display.max_colwidth=None

    if len(sys.argv) < 4:
        print(f'usage: {sys.argv[0]} <testpoints> <niter> <points-in-test>')
        sys.exit(1)
    testpoints = int(sys.argv[1])
    niter = int(sys.argv[2])
    points_in_test = int(sys.argv[3])

    X, y = datasets.make_classification(n_samples=testpoints, n_features=2, n_informative=1, n_redundant=0, n_classes=2, n_clusters_per_class=1, class_sep=5.0, hypercube=False)
    y = np.where(y == 0, -1, 1)

    X = np.array([[-2, -2], [2, 0], [-2, 2.5]])
    y = np.array([1, -1, 1])

    print(f'Points:{X}')
    print(f'Classification:{y}')
    order = X.shape[1]
    print(f'n:{len(X)}, order:{order}')

    th = np.array([0, 0])
    t0 = 0

    print(f'Parameters:{th}')
    print(f'Offset:{t0}') 
    # print(thetas)

    plt.scatter(X[:, 0][ y == -1 ], X[:, 1][ y == -1 ], color='red')
    plt.scatter(X[:, 0][ y == 1 ], X[:, 1][ y == 1 ], color='cyan')
    plt.title("Classification Data")
    plt.legend(["Class 1", "Class 2"])
    # plt.xlim([-5, 5])
    # plt.ylim([-5, 5])
    plt.show()

    convergence, total_mistakes, th_n, t0_n, thetas = run_perceptron(X, y, niter, th, t0, 1, 0)
    # print(thetas)

    print(f'After {niter} iterations:')
    print(f'Converged:{convergence}')
    print(f'Parameters:{th_n}')
    print(f'Offset:{t0_n}')
    print(f'Mistakes:{total_mistakes}')
    print(thetas)

    x_n = np.arange(-10, 10, 1)
    y_n = (-th_n[0] / th_n[1]) * x_n - t0_n

    # print(thetas)

    plt.scatter(X[:, 0][ y == -1 ], X[:, 1][ y == -1 ], color='red')
    plt.scatter(X[:, 0][ y == 1 ], X[:, 1][ y == 1 ], color='cyan')
    # plt.xlim([-5, 5])
    # plt.ylim([-5, 5])
    plt.plot(x_n, y_n, label='Perception')
    plt.title("Perceptron Line")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
