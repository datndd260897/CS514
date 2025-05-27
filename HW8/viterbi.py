from collections import defaultdict

def order(n, edges):
    from collections import deque
    adj = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []

    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(topo_order) == n:
        return topo_order
    else:
        return None  # cycle detected, but problem guarantees DAG


def longest(n, edges):
    topo = order(n, edges)
    if topo is None:
        return None  # just a safety check

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    dist = [-float('inf')] * n
    parent = [None] * n

    # Sources have longest path 0 length
    for u in topo:
        if all(u != v for _, v in edges):  # no incoming edges check is O(e)
            dist[u] = 0
    # A better way to find sources:
    indegree = [0] * n
    for u, v in edges:
        indegree[v] += 1
    for u in range(n):
        if indegree[u] == 0:
            dist[u] = 0

    for u in topo:
        if dist[u] == -float('inf'):
            continue
        for v in adj[u]:
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
                parent[v] = u

    # Find max dist and corresponding node
    max_len = max(dist)
    if max_len == -float('inf'):
        # No paths at all, e.g., empty graph
        # Return (0, [some node]) or (0, [])
        return (0, [])

    end = dist.index(max_len)

    # Reconstruct path
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse()

    return (max_len, path)


print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))