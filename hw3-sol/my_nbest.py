import heapq


def nbest(a, b):
    a.sort()
    n = len(a)
    heap = [(a[0] + b[index], b[index], index, 0) for index in range(n)]
    heapq.heapify(heap)
    result = []
    for i in range(n):
        _, _, b_index, a_index = heap[0]
        result.append((a[a_index], b[b_index]))
        if a_index + 1 < n:
            heapq.heapreplace(heap, (a[a_index + 1] + b[b_index], b[b_index], b_index, a_index + 1))

    return result

def nbest2(a, b):
    a.sort()
    b.sort()
    n = len(a)
    heap = [(a[0], b[0], 0, 0)]
    result = []
    def _put(i, j):
        if i < n and j <n:
            heapq.heappush(heap, (a[i] + b[j], b[j], j, i))
    for i in range(n):
        _, _, b_index, a_index = heapq.heappop(heap)
        result.append((a[a_index], b[b_index]))
        _put(a_index + 1, b_index)
        _put(a_index, b_index + 1)
    return result



# sum((h - 1)^ 2 + 2*(h-1) * (h-2))

if __name__ == "__main__":
    a, b = [4,1,5,3], [4, 2,6,3]
    print(nbest2(a,b))


