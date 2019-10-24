def h_index_calculator(arr):

    #Using Binary Search
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        midpoint = (lo + hi) // 2
        if arr[midpoint] == len(arr) - midpoint:
            return arr[midpoint]
        elif arr[midpoint] < len(arr) - midpoint:
            lo = midpoint + 1
        else:
            hi = midpoint - 1
    return len(arr) - hi - 1

    # Linear Search
    # h_index = 0
    # for i in arr:
    #     if i > h_index:
    #         h_index += 1
    #     else:
    #         return h_index

print(h_index_calculator([6,5,3,1,0]))
