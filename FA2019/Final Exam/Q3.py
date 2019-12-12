import numpy as np
import random as rand

def dpsolution(arr):
    # Creates matrix of zeros with dimentions len(arr) x len(arr)
    dpTable = np.zeros((len(arr), len(arr)), dtype = int)

    # Iterates through matrix
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # Variables to store decisions
            C1 = 0
            C2 = 0
            C3 = 0

            # Predicting 2 ahead of P2 in to account for all possiblilties, i + 2 vs j
            if i + 2 <= j:
                C1 = dpTable[i + 2][j]
            else:
                C1 = 0

            # Predicting j - 1 vs i + 1
            if i + 1 <= j - 1:
                C2 = dpTable[i + 1][j - 1]
            else:
                C2 = 0

            # Predicting i vs j -2
            if i <= j  - 2:
                C3 = dpTable[i][j - 2]
            else:
                C3 = 0

            # Select min from decisions and insert it into the dp table
            dpTable[i][j] = min(arr[i] + min(C1, C2), arr[j] + min(C2, C3))

    winner_sum = dpTable[0][len(arr) - 1]

    # Return the sum of the winner, which will always be P1
    return "Winner Sum: " + str(winner_sum)

def greedysolution(A):
    turn = True
    #Stores hands
    P1_hand = []
    P2_hand = []

    while len(A) != 0:
        if turn == True:
            #Append min of first and last elemtents
            P1_hand.append(min(A[0], A[-1]))
            A.remove(P1_hand[-1])

        if turn == False:
            P2_hand.append(min(A[0], A[-1]))
            A.remove(P2_hand[-1])

        turn = not(turn)

    print("P1 sum: " + str(sum(P1_hand)))
    # print(P1_hand, P2_hand)
    print("P2 sum: " + str(sum(P2_hand)))

    if sum(P1_hand) < sum(P2_hand):
        return "P1 is the winner"
    if sum(P2_hand) < sum(P1_hand):
        return "P2 is the winner"


#Test Cases
print(greedysolution([4,2,6,5])) #P2 is Winner
print(greedysolution([2,3,4,56,8,7,10,68])) #P1 is winner
print(greedysolution([rand.randrange(1,100) for i in range(100)]))

print(dpsolution([4,2,6,5]))
print(dpsolution([2,3,4,56,8,7,10,68]))
print(dpsolution([rand.randrange(1,100) for i in range(100)]))
