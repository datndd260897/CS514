import heapq

def ksmallest(k, data):
    max_heap = []
    for x in data:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return sorted(-x for x in max_heap)


print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))  # Output: [2, 3, 5, 7]
print(ksmallest(3, range(1000000, 0, -1)))  # Output: [1, 2, 3]
print(ksmallest(5, (x ** 2 for x in range(10, 0, -1))))  # Output: [1, 4, 9, 16, 25]
import random;

random.seed(1);
print(ksmallest(5, (random.randint(0, 100) for _ in range(10))))  # Output: [8, 15, 17, 32, 57]
