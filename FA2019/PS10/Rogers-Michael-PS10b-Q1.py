import numpy as np

# The alignStrings function is outputting the optimal cost of aligning two strings x and y.
# The first thing I did was create a numpy array of zeros which is out empty matrix that we
# will populate with the DP algorithm. I then put x in the first column and y in the first row.
# Then I iterated through all of the empty elements fo the table to gain an optimal cost matrix.
# The method of the DP algorithm was to choose the operation with the least cost. So a no-op was
# the cheapest, and then it depended on user input. Once the algorithm is going it chooses based
# on prior elements in the matrix to make it's decision. Unfortunatley, the algorithm seems to not
# be working completely correctly, and I couldn't figure out how to fix it before the deadline.

def alignStrings(x, y, cInsert, cDelete, cSub):
    S = np.zeros([len(y) + 1, len(x) + 1], dtype = int) # len(x) x len(y) Matrix of zeros

    S[0] = [x for x in range(len(x) + 1)] # Put x in first column
    for i in range(len(y) + 1): # Put Y in first row
        S[i][0] = i

    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            if y[i - 1] == x[j - 1]: # If chars are equal, ignore
                S[i][j] = min(S[i][j-1] + cInsert, S[i][j-1] + cDelete, S[i][j] + cInsert, S[i][j] + cDelete, S[i-1][j-1])
            else:
                S[i][j] = min(S[i][j-1] + cInsert, S[i][j-1] + cDelete, S[i-1][j] + cInsert, S[i-1][j] + cDelete, S[i-1][j-1] + cSub)
    return S


# Not working / Incomplete
# def extractAlignment(S, x, y, cInsert, cDelete, cSub):
#     a = []
#     if

# Incomplete
# def commonSubstrings(x, L, a):


print(alignStrings('EXPONENTIAL', 'POLYNOMIAL', 2, 1, 2))
