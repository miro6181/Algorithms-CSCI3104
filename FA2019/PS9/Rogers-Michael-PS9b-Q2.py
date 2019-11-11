def optimalShake(arr):

    dp = list(range(len(arr)-1))

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    dp = [max(dp[i-1], dp[i-2] + arr[i]) for i in range(2, len(arr) -1)]

    return dp[-1]

print(optimalShake([2,7,9,3,1]))
