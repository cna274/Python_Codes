from numpy import shape
from numpy import sum
def peri_sum(M):
    [r,c] = M.shape
    b = M[1:r-1,1:c-1]
    return M.sum()-b.sum()
