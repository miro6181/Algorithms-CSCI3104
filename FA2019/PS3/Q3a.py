def optimal_win_vals(n):
    win_vals = [1,2,4,8,16]
    remaining = n
    count = 0
    # while remaining != 0:
    #     if win_vals[-1] <= remaining:
    #         remaining -= win_vals[-1]
    #         count += 1
    #     else:
    if win_vals[-1] <= remaining:
        remaining = remaining - win_vals[-1]
        count += 1
    for i in range(0, len(win_vals)):
        if win_vals[i] == remaining:
            remaining = remaining - win_vals[i]
        elif win_vals[i] > remaining:
            print(i)
            remaining = remaining - win_vals[i-1]
            count += 1
    return count

print(optimal_win_vals(15))
