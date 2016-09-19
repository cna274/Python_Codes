import numpy as np
def cancel_middle(a,b):
    #matrix = np.zeros(b)
    row = (np.shape(a)[0]-b)/2
    col = (np.shape(a)[1]-b)/2
    a[row:np.shape(a)[0]-row,col:np.shape(a)[1]-col] = 0
    return a
    
    