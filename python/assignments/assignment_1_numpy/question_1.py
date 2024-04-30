# 1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np

def create_null_vector(size):
    null_vector = np.zeros(10)
    null_vector[4] = 1
    return null_vector

if __name__ == "__main__":
    size = 10
    res = create_null_vector(size)
    print(res)