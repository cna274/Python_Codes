import numpy as np
def int_quad(n,m):
    zero = np.zeros((n,m), dtype = int)
    one = np.ones((n,m), dtype = int)
    two = 2*np.ones((n,m),dtype = int)
    three = 3*np.ones((n,m),dtype = int)
    rowOne = np.hstack((zero,one))
    rowTwo = np.hstack((two,three))
    return (np.vstack((rowOne,rowTwo)))