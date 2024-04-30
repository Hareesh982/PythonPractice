# 6. Create a random vector of size 30 and find the mean value

import numpy as np

def mean():
    vector = np.random.rand(30)
    mean = np.mean(vector)
    return mean

if __name__ == "__main__":
    res = mean()
    print("Mean value:", res)
