"""
   Given two lists A and B, each with n integers, return
   a sorted list C that contains the smallest n elements from AxB:

     AxB = { (x, y) | x in A, y in B }

   i.e., AxB is the Cartesian Product of A and B.

   ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')

   You need to implement three algorithms and compare:

   (a) enumerate all n^2 pairs, sort, and take top n.
   (b) enumerate all n^2 pairs, but use quickselect instead.
   (c) best-first, only enumerate O(n) (at most 2n) pairs.
       Note: this is known as "baby Dijkstra", due to static priorities.
       	    HW8 does real Dijkstra (priorities can change -- like in ER).

"""

import heapq
import random


# Algorithm (a) - Brute-force with sorting
def nbesta(a, b):
    pairs = [(x, y) for x in a for y in b]
    pairs.sort(key=lambda p: (p[0] + p[1], p[1]))  # Sort by (x + y) and then y

    return pairs[:len(a)]


# Algorithm (b) - Quickselect-based
def quickselect(arr, k, comp):
    """
    Quickselect to find the k-th smallest element in an array based on a comparison function `comp`.
    Returns the first k elements after selecting them.
    """

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if comp(arr[j], pivot) < 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def select(arr, low, high, k):
        if low < high:
            pi = partition(arr, low, high)
            if pi == k:
                return
            elif pi < k:
                select(arr, pi + 1, high, k)
            else:
                select(arr, low, pi - 1, k)

    select(arr, 0, len(arr) - 1, k)
    return arr[:k]


def nbestb(a, b):
    # Step 1: Enumerate all n^2 pairs
    pairs = [(x, y) for x in a for y in b]

    # Step 2: Use quickselect to find the top n pairs
    return quickselect(pairs, len(a), comp=lambda p, q: (p[0] + p[1]) - (q[0] + q[1]) or (p[1] - q[1]))


# Algorithm (c) - Best-first with priority queue
def nbestc(a, b):
    # Step 1: Initialize a min-heap
    heap = []
    visited = set()  # To track visited pairs
    heapq.heappush(heap, (a[0] + b[0], a[0], b[0]))  # Push the first pair (smallest possible sum)

    result = []

    while len(result) < len(a):
        # Pop the smallest pair from the heap
        _, x, y = heapq.heappop(heap)
        if (x, y) not in visited:
            visited.add((x, y))
            result.append((x, y))

        # Push the next possible pairs into the heap
        for next_y in b:
            if (x, next_y) not in visited:
                heapq.heappush(heap, (x + next_y, x, next_y))

        # Break if we have found 'n' pairs
        if len(result) == len(a):
            break

    return result


# Example usage
a, b = [4, 1, 5, 3], [2, 6, 3, 4]

print("nbesta:", nbesta(a, b))
print("nbestb:", nbestb(a, b))
print("nbestc:", nbestc(a, b))


