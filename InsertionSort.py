# Pseudocode:

# 1- x = [], key = 0
# 2- read x
# 3- for i = 1 forward len(x)
# 3.1-  key = x[i]
# 3.2-  for j = i - 1 backward j >= 0
# 3.2.1-    if key < x[j] then x[j + 1] = x[j]
# 3.2.2-    else break this loop
# 3.3-  x[j + 1] = key
# 4- print x

# ----------------------------------------------------

# Code Implementaion:
def InsertionSort(array):
    n = len(array) # 1
    for i in range(1, n): # n
        key = array[i] # n
        j = i - 1 # n
        while j >= 0: # n * n
            if key < array[j]: # n * n
                array[j + 1] = array[j] # n * n
            else:
                break # n * n
            j -= 1 # n * n
        array[j + 1] = key # n

# f(n) = 5n^2 + 4n + 1
# Time complexity O(n^2)
