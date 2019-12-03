import matplotlib.pyplot as plt
import numpy as np
import random

def hash_index(last_name, bucket):
    hash = 0
    for char in last_name:
        hash += ord(char) - ord('A') + 1
        hash = hash % bucket
    return hash

last_name_hash = {}

bucket_size = 5987

for i in range(0, bucket_size):
    last_name_hash[i] = 0

name_list = []
with open("dist.all.last.txt") as file:
    for line in file:
        last_name = line.split()[0]
        names_list.append(last_name)

rand_indicies = random.sample(range(len(names_list)), len(names_list) // 2)
last_name_list = [names_list[i] for i in indicies]

for name in last_name_list:
    hash_value = hash_index(name,bucket_size)
    last_name_hash[hash_value] += 1

print(last_name_hash)

hash_lst = []

for key in sorted(last_name_hash.keys()):
    hash_lst.append(last_name_hash[key])

print(hash_lst)

b = range(0,bucket_size)
plt.bar(b, hash_lst)
#plt.hist(hash_as_list, bins=b)
plt.title("Histogram showing distribution of hash of last names")
plt.xlabel("Bucket number")
plt.ylabel("Size of bucket")
plt.show()
