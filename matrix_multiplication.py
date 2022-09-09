import numpy as np


if __name__=='__main__':
    arr1 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ])

    arr2 = np.array([
        [0, 3, 1],
        [0, 1, 4],
        [4, 5, 2],
        [0, 1, 2],
    ])

    print(np.matmul(arr2, arr1))
