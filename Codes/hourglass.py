import numpy as np
arr = []
val = list()
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
   mask = [0,1,2,7,11,12,13]
for i in range(4):
  for j in range(4):   
    val = val.append(sum([arr[i] for i in mask]))
    mask = np.add(mask,1)
  mask = np.add(mask,4)
print max(val)   
   
