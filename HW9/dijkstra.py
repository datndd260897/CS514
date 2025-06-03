from heapdict import heapdict


def shortest(n, edges):
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    prev = [None] * n
    dist[0] = 0

    pq = heapdict()
    pq[0] = 0

    while pq:
        u, d = pq.popitem()
        if u == n - 1:
            # reconstruct path
            path = []
            while u is not None:
                path.append(u)
                u = prev[u]
            path.reverse()
            return (d, path)

        for v, w in graph[u]:
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                pq[v] = alt  # decrease key or insert

    return None


print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
# Expected: (4, [0,1,2,3])

print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
# Expected: None

print(shortest(4, [(0,1,1), (2,3,1)]))
# Expected: None
