import numpy as np
def simple_stats(mat):
    row = mat.shape
    stat = np.zeros((row[0],4),dtype = float)
    for i in range(0,row[0]):
        stat[i] = [mat[i].mean(), np.median(mat[i],axis=1),mat[i].max(),mat[i].min()]
    return np.vstack(stat[0:row[0]])