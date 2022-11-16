import os
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pylab as plt


# curse of dimensionality problem:
# see the relationship between volume fractions
# and the dimension and the epsilon value as 
# described below.
# think intuitively looking at the graph
# you plot in the function main (below)
# and visualize the impact of dimensions.

# 
# 
# mathematically:
# volume of unit sphere of d dimensions = K*1^d
# where K is a constant.
# volume of sphere of radius (1-epsilon) of d dimensons = K*(1-epsilon)^d

# thus the fraction between 1-epsilon and 1 radius is :
# vf = (k*1^d - k*(1-epsilon)^d)/(k*1^d)
# vf = 1-(1-epsilon)^d

# calculate the volume fractions
# given the epsilons.
# epsilon - list of values
# d - no. of dimensions
# return vf  - list volume fraction corresonding to the epsilon.

# from the main function plot epsilon vs vf, understand
# how the dimensions impact the relationship between
# epsilon and volume fraction.
#
# Volume fraction is the fraction of the volume
# occupied between 1 and (1-epsilon) in the unit 
# sphere of "d" dimensions. 

def volume_fraction(epsilon, d):
    vf = [1 - (1 - eps) ** d for eps in epsilon]
    return vf
    raise NotImplementedError


# Similar intuition as above with a cube. 
# Suppose you have a one dimensional cube
# with "d" dimensions
# Take a fraction of the cube say 10% or 20% 
# of volume of the unit cube and verify
# how much distance you have to travel
# from the origin on each of the dimensions
# to get a cube of that fracton !
# mathematically:
# let us say the fraction value is f.
# a cube of "d" dimensions volume is = x^d
# where x is the distance  on all d dimensions
# from the origin. 
# x^d = f
# implies x=(f)^(1/d).

# from the main function plot x vs f, understand
# how the dimensions impact the relationship between
# distance x and volume fraction in a cube.

# below you calculate the x values for each of the fraction
# for a given dimension d.
# input: 
# f - list of fraction value of the cube 
# d - dimension of the cube
# return:  list of x values.


def cube_distance(f, d):
    x = [fs ** (1 / d) for fs in f]
    return x
    raise NotImplementedError

             
def main():

    # Attach the graphs below as part of codepost.
    # Code for drawing graph of volume fractions.

    epsilon=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    for d in range(1,21):
        vf=volume_fraction(epsilon,d)
        s=f'D={d}'
        plt.plot(epsilon, vf, "-o",label=s)
    plt.xlabel('epsilon')
    plt.ylabel('volume fraction')
    plt.legend()
    plt.show()

    # Code for drawing graph of the cube distances.

    f=[0.01,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ]
    for d in range(1,21):
        x=cube_distance(f,d)
        s=f'D={d}'
        plt.plot(x, f, "-o",label=s)
    plt.xlabel('distance in dimension')
    plt.ylabel('volume fraction')
    plt.legend()
    plt.show()

	
if __name__ == "__main__":
    main()
