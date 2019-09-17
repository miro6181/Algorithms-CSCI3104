def chargingRoute(k, pods_lst):
    selected_pods = [0] # Initialize selected pods with 0 to help with indexing in the for loop.
    for i in range(0,len(pods_lst)): # Iterate through each element in the list
        if pods_lst[i] - selected_pods[-1] > k: # If there is more than k meters between i and the last selected pod:
            selected_pods.append(pods_lst[i-1]) # Add the element before i to the selected pods list.

    selected_pods.pop(0) # Remove the starting location for formatting.
    return selected_pods


# Test Cases From assignment
print(chargingRoute(40, [0, 20, 37, 54, 70, 90]))  # = [37, 70]
print(chargingRoute(20, [0, 18, 21, 24, 37, 56, 66]))  # = [18, 37, 56]
print(chargingRoute(20, [0, 10, 15, 18]))  # = []
# Personal Test Cases
print(chargingRoute(60, [0, 14, 58, 100])) # = [58]
print(chargingRoute(15, [0, 14, 17, 30, 35])) # = [14, 17, 30]
print(chargingRoute(35, [0, 10, 15, 30])) # = []
