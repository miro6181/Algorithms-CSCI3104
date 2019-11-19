import numpy as np

def alignStrings(x, y, cInsert, cDelete, cSub):
    S = np.zeros([len(y) + 1, len(x) + 1], dtype = int) # len(x) x len(y) Matrix of zeros

    S[0] = [x for x in range(len(x) + 1)] # Put X in first row
    for i in range(len(y) + 1): # Put Y in first column
        S[i][0] = i

    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            if y[i - 1] == x[j - 1]: # If chars are equal, ignore
                S[i][j] = min(S[i][j-1] + cInsert, S[i][j-1] + cDelete, S[i][j] + cInsert, S[i][j] + cDelete, S[i-1][j-1])
            else:
                S[i][j] = min(S[i][j-1] + cInsert, S[i][j-1] + cDelete, S[i-1][j] + cInsert, S[i-1][j] + cDelete, S[i-1][j-1] + cSub)
    return S


#
# def extractAlignment(S, x, y, cInsert, cDelete, cSub):
#     a = []
#     if

# def commonSubstrings(x, L, a):


print(alignStrings('EXPONENTIAL', 'POLYNOMIAL', 2, 1, 2))
