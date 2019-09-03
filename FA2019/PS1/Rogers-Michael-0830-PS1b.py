import random

def count_flip(n):
    print("Create random array of size " + str(n))
    rand_arr = [x for x in range(1,n + 1)] # Create list of numbers between 1 and n
    random.shuffle(rand_arr) # Shuffle list of numbers
    count = 0 # Initialize the counter at 0
    for i in range(n):
        for j in range(i + 1, n): # Compare i with all numbers with a larger index in the list
            if rand_arr[i] > rand_arr[j]:
                count += 1
    return count

print(count_flip(2**10))
