def h_index_calculator(arr):

    #Using Binary Search
    n = len(arr)
    start = 0
    end = n-1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == n-middle:
            return arr[middle]
        elif arr[middle] < n - middle:
            start = middle + 1
        else:
            end = middle - 1
    return n - end - 1


    # Linear Search
    # for i in arr:
    #     if i > h_index:
    #         h_index += 1
    #     else:
    #         return h_index

print(h_index_calculator([6,5,3,1,0]))
