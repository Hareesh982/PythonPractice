# 4. Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

def non_zero_indices():
    array = np.array([13, 0, 0, 0, 14, 0])
    indices = np.nonzero(array)
    return indices

if __name__ == "__main__":
    res = non_zero_indices()
    print(res)
