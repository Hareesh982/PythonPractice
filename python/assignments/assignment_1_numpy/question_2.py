# 2. Create a vector with values ranging from 10 to 49.

import numpy as np

def vector_range():
    vector = np.arange(10, 50)
    return vector

if __name__ == "__main__":
    res = vector_range()
    print(res)