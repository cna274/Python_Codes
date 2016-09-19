import numpy as np
def even_index(M):
    z = np.shape(M)
    b = []
    even_row = range(1,z[0],2)
    even_col = range(1,z[1],2)
    if not even_row or not even_col:
        return b
    else:
        b = M[even_row,even_col]
        return b
