from numpy import shape
def top_right(M,n):
    [r, c] = M.shape
    b = M[c-n:c,0:r-1]
    return b
    
