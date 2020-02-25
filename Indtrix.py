# This function creates an array out of a tuple of numbers (from 1 to 9)
# The outputted array should have regular indexed values, good for checking things.
# For an example array X of some undefined shape, X[2,4,1,2,3]rd entry should be 24123 etc.

import numpy as np

def Indtrix(shape):
    matr = np.zeros((shape)) # Generate a basic shape for indexing
    x = np.ndim(matr) # work out its dimensions
    b = np.ones(x)*10 # Create a matrix of ones of array's size
    b = np.cumprod(b) #multiply the arrays
    b = np.floor_divide(b,10) #divide arrays by 10 but keep them equal
    b = b[: :-1] # reversing the arrays
    # For some matrix:
    xarray = np.indices(matr.shape)
    rng = np.arange(x)
    for i in rng:
        xarray[i] = xarray[i]*b[i]
    return xarray.sum(axis=0) # Better than "Print" I discovered
    #print(xarray.sum(axis=0)) Here just in case
