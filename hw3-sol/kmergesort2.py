from heapq import heappush, heappop, heapify, heapreplace


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    return merge_sorted(mergesort(arr[:len(arr) // 2]), mergesort(arr[len(arr) // 2:]))


def merge_sorted(a, b):
    if a == [] or b == []:
        return a + b
    elif a[0] <= b[0]:
        return [a[0]] + merge_sorted(a[1:], b)
    else:
        return [b[0]] + merge_sorted(a, b[1:])

# print(mergesort([4, 2, 5, 1, 6, 3]))
#
# def mymerge3(k_lists):
#     heap = [(next(a), i, a.__next__) for i, a in enumerate(map(iter, k_lists))] # passing the next function instead of iterator
#     heapify(heap)
#     while heap != []:
#         x, i, next_f = heap[0]
#         yield x
#         try:
#             heapreplace(heap, (next_f(), i, next_f))
#         except StopIteration: # no more elements in this sublist
#             heappop(heap)

def select(list_states):
    """
    list_state = [(), ()]
    """
    num_states, num_players = len(list_states), len(list_states[0])
    heap = [(list_states[state_index][0], state_index, 0)  for state_index in range(num_states)]
    heapify(heap)
    for _ in range(num_players):
        x, i, j = heap[0]
        yield x
        if j <= num_players -1:
            heapreplace(heap, (list_states[i][j+1], i, j+1))

# Test case
list_states = [
    (1, 4, 7, 10),   # State 0
    (2, 5, 8, 11),   # State 1
    (3, 6, 9, 12),   # State 2
]
result = list(select(list_states))
print(result)
