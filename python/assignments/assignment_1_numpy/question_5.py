# 5. Create a 10x10 array with random values and find the minimum and maximum values

import numpy as np

def min_max():
    array = np.random.rand(10, 10)

    minimum_value = np.min(array)
    maximum_value = np.max(array)
    
    print("Maximum value : ",maximum_value)
    print("Minimum_value : ",minimum_value)

if __name__ == "__main__":
    min_max()