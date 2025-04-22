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



# Algorithm (c) - Best-First (Baby Dijkstra)
def nbestc(A, B):
    # Initialize the heap with the first element
    heap = []
    heapq.heappush(heap, (A[0] + B[0], 0, 0))  # (sum, index in A, index in B)

    result = []
    seen = set()  # To track visited index pairs
    seen.add((0, 0))  # We start from (0, 0)

    while len(result) < len(A):
        _, i, j = heapq.heappop(heap)  # Pop the smallest element from the heap
        result.append((A[i], B[j]))  # Add the pair to the result

        # Move to the next element in the current row if possible
        if i + 1 < len(A) and (i + 1, j) not in seen:
            heapq.heappush(heap, (A[i + 1] + B[j], i + 1, j))
            seen.add((i + 1, j))

        # Move to the next element in the current column if possible
        if j + 1 < len(B) and (i, j + 1) not in seen:
            heapq.heappush(heap, (A[i] + B[j + 1], i, j + 1))
            seen.add((i, j + 1))

    return result


# Test the functions
a = [4, 1, 5, 3]
b = [2, 6, 3, 4]

print("Algorithm (a) Result:", nbesta(a, b))
print("Algorithm (b) Result:", nbestb(a, b))
print("Algorithm (c) Result:", nbestc(a, b))
