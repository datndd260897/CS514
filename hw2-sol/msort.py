#!/usr/bin/env python3

__author__ = "Liang Huang" 

'''I wrote two versions of mergesorted().'''

def mergesort(lst): # common among three versions
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

def mergesorted0(a, b): # v0: BAD; O(n^2) merging => O(n^2) overall
    if a == [] or b == []:
        return a+b
    elif a[0] <= b[0]:
        return [a[0]] + mergesorted0(a[1:], b) # O(n)
    else:
        return [b[0]] + mergesorted0(a, b[1:]) # O(n)

def mergesorted1(a, b): # v1: good; O(n) merging => O(nlogn) overall
    if a == [] or b == []:
        return a+b
    c = []
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    return c

mergesorteds = [mergesorted0, mergesorted1] # function pointers

if __name__ == "__main__":
    import sys, time
    import random
    random.seed(1)
    sys.setrecursionlimit(100000)
    for j in range(5):
        n = 1000 * 2**j # exponential scale    
        print("n=%6d" % n, end=" ")
        a = random.sample(list(range(n)), n)        
        results = []
        for i in range(2):
            t = time.time()
            mergesorted = mergesorteds[i] # function pointer
            results.append(mergesort(a))
            print("mergesorted%d" % i, "%.3f secs" % (time.time() - t), end="\t")
        print("Equal" if results[0] == results[1] else "NOT EQUAL!")        