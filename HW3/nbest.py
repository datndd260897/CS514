import heapq


# Algorithm (a) - Naive Enumeration & Sorting
def nbesta(A, B):
    pairs = [(x, y) for x in A for y in B]
    pairs.sort(key=lambda pair: (pair[0] + pair[1], pair[1]))
    return pairs[:len(A)]


# Algorithm (b) - Quickselect
def quickselect(arr, k, compare_fn):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if compare_fn(arr[j], pivot):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(left, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, right, k)

    select(0, len(arr) - 1, k)
    return arr[:k]


def nbestb(A, B):
    def _compare_function(x, y):
        return (x[0] + x[1] < y[0] + y[1]) or (x[0] + x[1] == y[0] + y[1] and x[1] > y[1])
    pairs = [(x, y) for x in A for y in B]
    pairs.sort(key=lambda pair: (pair[0] + pair[1], pair[1]))
    return quickselect(pairs, len(A), _compare_function)




def nbestc(A, B):
    if not A or not B:
        return []
    # Sort both lists to ensure we always work with the smallest available values
    A.sort()
    B.sort()

    # Initialize the priority queue with the smallest pair (A[0], B[0])
    pq = []
    heapq.heappush(pq, (A[0] + B[0], B[0], 0, 0))  # (sum, index in A, index in B)

    # Keep track of the pairs we've already considered to avoid duplicates
    visited = set((0, 0))

    result = []

    while len(result) < len(A):  # We need exactly n pairs
        sum_val, y_val, i, j = heapq.heappop(pq)
        result.append((A[i], B[j]))

        # Expand by adding the next pair in the row (i+1, j) and column (i, j+1)
        if i + 1 < len(A) and (i + 1, j) not in visited:
            heapq.heappush(pq, (A[i + 1] + B[j], B[j], i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < len(B) and (i, j + 1) not in visited:
            heapq.heappush(pq, (A[i] + B[j + 1], B[j + 1], i, j + 1))
            visited.add((i, j + 1))

    return result


# Test the functions
a = [4, 1, 5, 3]
b = [2, 6, 3, 4]

print("Algorithm (a) Result:", nbesta(a, b))
print("Algorithm (b) Result:", nbestb(a, b))
print("Algorithm (c) Result:", nbestc(a, b))
