import numpy as np

def sumSubset(S, t, k):
    determination_matrix = np.array([[False for x in range(t + 1)] for x in range(len(S))])

    for i in range(len(S)):
        determination_matrix[i][0] = True
    print(determination_matrix)

    # for i in range

sumSubset([2,1,5,7],4, 2)
