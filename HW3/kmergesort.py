import heapq


def k_way_merge(arrays):
    heap = []
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(heap, (array[0], i, 0))  # (value, list index, element index)

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(arrays[list_idx]):
            next_val = arrays[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


def kmergesort(arr, k):
    if k >= len(arr):
        return sorted(arr)
    subarray_size = len(arr) // k
    subarrays = []
    start = 0
    for i in range(k - 1):
        subarrays.append(arr[start*subarray_size:subarray_size * (i+1)])
        start += 1
    subarrays.append(arr[start*subarray_size:])
    sorted_subarrays = [kmergesort(subarray, k) for subarray in subarrays]
    return k_way_merge(sorted_subarrays)


# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3  # You can change k to any value

sorted_arr = kmergesort(arr, k)
print(sorted_arr)
