def h_index_calculator(arr):

    #Using Binary Search
    # low = 0
    # high = len(arr) - 1
    #
    # while low <= high:
    #     midpoint = (low + high) // 2
    #     if arr[midpoint] == len(arr) - midpoint:
    #         return arr[midpoint]
    #     elif arr[midpoint] < len(arr) - midpoint:
    #         low = midpoint + 1
    #     else:
    #         high = midpoint - 1
    # return len(arr) - high - 1


    # Linear Search
    h_index = 0
    for i in arr:
        if i > h_index:
            h_index += 1
        else:
            return h_index

print(h_index_calculator([6,5,3,1,0]))
print(h_index_calculator([100,34,23,15,11,4,2,1]))
