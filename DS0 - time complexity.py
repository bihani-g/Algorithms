import time
import numpy as np


# # Linear search
#
# def linear_search(a, array):
#     a = int(a)
#     for i in range(len(array)):
#         if a == array[i]:
#             print("Index of the item we are looking is", i)
#
#
# linear_search(4, [0,5,6,4])  #O(N) time complexity
#
#  Binary search
#  iterative
# def bin_search_i(a, sort):
#     a = int(a)
#
#     low = 0
#     high = len(sort) - 1
#     mid = 0
#
#     while low <= high:
#         mid = math.floor((high + low) / 2)
#
#         if a < sort[mid]:
#             high = mid - 1
#         elif a > sort[mid]:
#             low = mid + 1
#         elif a == sort[mid]:
#             print("Index of the item we are looking is", mid)
#             break
#
#
# bin_search_i(10, [-1, 0, 1, 2, 3, 4, 10])


#  recursive
# def bin_search_r(a, sort, low, high):
#     a = int(a)
#
#     if low <= high:
#         mid = math.floor((high + low) / 2)
#
#         if a == sort[mid]:
#             return print("Index of the item we are looking is", mid)
#
#         elif a < sort[mid]:
#             return bin_search_r(a, sort, low, mid - 1)
#         elif a > sort[mid]:
#             return bin_search_r(a, sort, mid + 1, high)
#
#     else:
#         return print("Number doesn't exist in array")
#
#
# array = [-1, 0, 1, 2, 3, 4, 10]
# element = 10
#
# bin_search_r(element, array, 0, len(array) - 1)


#  Bubble sort

def bubble_sort(a):
    high = len(a) - 1
    new = []

    while high >= 0:  ## 2 loops, first loops n times, second loops n-1 times; (n-1)*n = n2 -n --> O(n2)
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp

        new.insert(0, a[high])
        a = a[0:high]
        high = high - 1

    # return print(new)


#  checking sorting time

array = np.random.rand(1000)
start_time = time.time()
bubble_sort(array)
print("--- %s seconds ---" % round((time.time() - start_time), 10))
