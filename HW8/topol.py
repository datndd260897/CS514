# topol.py

from collections import deque, defaultdict

def order(n, edges):
    # Bottom-up (Kahn's Algorithm)
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
        return None  # cycle detected


def order2(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    for u in adj:
        adj[u].sort()  # sort neighbors for deterministic traversal order

    visited = [0] * n
    topo_order = []

    def dfs(u):
        if visited[u] == 1:
            return False
        if visited[u] == 2:
            return True
        visited[u] = 1
        for v in adj[u]:
            if not dfs(v):
                return False
        visited[u] = 2
        topo_order.append(u)
        return True

    for node in range(n):
        if visited[node] == 0:
            if not dfs(node):
                return None

    topo_order.reverse()
    return topo_order


print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order2(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
# Output: None


