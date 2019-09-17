def optimal_win_vals(n):
    win_vals = [1,2,4,8,16]
    remaining = n
    count = 0
    while remaining > 0:
        for i in win_vals[::-1]:
            print(i)
            if i <= remaining :
                remaining -= i
                count += 1
    return count

print(optimal_win_vals(100))
