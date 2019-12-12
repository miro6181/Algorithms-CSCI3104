import numpy as np

def sumSubset(S, t, k):
    #Creates matrix to store decisions
    determination_matrix = np.array([[False for x in range(t + 1)] for x in range(len(S) + 1)])

    #Fill in the first column with true because 0 can be made with the empty set.
    for i in range(len(S) + 1):
        determination_matrix[i][0] = True

    #Iterate through table of false values
    for i in range(1, len(S) + 1):
        for j in range(1, t + 1):
            # If sum is net positive, take the true above it, or backtrack to the last used element of S
            if j - S[i - 1] >= 0:
                determination_matrix[i][j] = determination_matrix[i - 1][j] or determination_matrix[i - 1][j - S[i - 1]]
            # Else copy entry from previous row
            else:
                determination_matrix[i][j] = determination_matrix[i - 1][j]
    print(determination_matrix)

    subset = []
    #Backtrack through the matrix and collect numbers in subset sum
    if determination_matrix[len(S)][t] == True:
        for i in range(len(S), 0, -1):
            if determination_matrix[i-1][t-1] == False:
                subset.append(S[i-1])
        if len(subset) == k:
            return subset
        return False
    else:
        return False

print(sumSubset([2,1,5,7],4, 2))
print(sumSubset([2,1,5,7], 6, 2))
print(sumSubset([3,3,5,1], 6, 3))
