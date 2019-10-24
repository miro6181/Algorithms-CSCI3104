import random

class SortArr:

    def __init__(self, n):
        self.n = n
        self.rand_arr = [x for x in range(1, n + 1)]
        random.shuffle(self.rand_arr)

    def slow_sort(self): #Runs in O(n^2)
        count = 0 # Initialize the counter at 0
        for i in range(self.n):
            for j in range(i + 1, self.n): # Compare i with all numbers with a larger index in the list
                if self.rand_arr[i] > self.rand_arr[j]:
                    count += 1
        return count

    def fast_sort(self, in_arr):
        count = 0
        if len(in_arr) > 1:
            midpoint = len(in_arr) // 2 # Sets midpoint in array
            left = in_arr[:midpoint]
            right = in_arr[midpoint:]
            self.fast_sort(left) # Traversal of Left Sub-Tree
            self.fast_sort(right) # Traversal of Right Sub-Tree

            i = 0
            j = 0
            k = 0

            # Copy sub-arrays into temp arrays left and right
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    in_arr[k] = left[i]
                    i += 1
                    count += 1
                else:
                    in_arr[k] = right[j]
                    j += 1
                    count += 1
                k += 1

            while i < len(left):
                in_arr[k] = left[i]
                i += 1
                k += 1
                count += 1

            while j < len(right):
                in_arr[k] = right[j]
                j += 1
                k += 1
                count += 1
        return count

#Test Cases
arr1 = SortArr(2**2)
print("Array 1 Slow: " + str(arr1.slow_sort()))
print("Array 1 Fast: " + str(arr1.fast_sort(arr1.rand_arr)) + "\n")

arr2 = SortArr(2**3)
print("Array 2 Slow: " + str(arr2.slow_sort()))
print("Array 2 Fast: " + str(arr2.fast_sort(arr2.rand_arr)) + "\n")

arr3 = SortArr(2**4)
print("Array 3 Slow: " + str(arr3.slow_sort()))
print("Array 3 Fast: " + str(arr3.fast_sort(arr3.rand_arr)) + "\n")

arr4 = SortArr(2**5)
print("Array 4 Slow: " + str(arr4.slow_sort()))
print("Array 4 Fast: " + str(arr4.fast_sort(arr4.rand_arr)) + "\n")

arr5 = SortArr(2**6)
print("Array 5 Slow: " + str(arr5.slow_sort()))
print("Array 5 Fast: " + str(arr5.fast_sort(arr5.rand_arr)) + "\n")

arr6 = SortArr(2**7)
print("Array 6 Slow: " + str(arr6.slow_sort()))
print("Array 6 Fast: " + str(arr6.fast_sort(arr6.rand_arr)) + "\n")

arr7 = SortArr(2**8)
print("Array 7 Slow: " + str(arr7.slow_sort()))
print("Array 7 Fast: " + str(arr7.fast_sort(arr7.rand_arr)) + "\n")

arr8 = SortArr(2**9)
print("Array 8 Slow: " + str(arr8.slow_sort()))
print("Array 8 Fast: " + str(arr8.fast_sort(arr8.rand_arr)) + "\n")

arr9 = SortArr(2**10)
print("Array 9 Slow: " + str(arr9.slow_sort()))
print("Array 9 Fast: " + str(arr9.fast_sort(arr9.rand_arr)) + "\n")

arr10 = SortArr(2**11)
print("Array 10 Slow: " + str(arr10.slow_sort()))
print("Array 10 Fast: " + str(arr10.fast_sort(arr10.rand_arr)) + "\n")

arr11 = SortArr(2**12)
print("Array 11 Slow: " + str(arr11.slow_sort()))
print("Array 11 Fast: " + str(arr11.fast_sort(arr11.rand_arr)) + "\n")
