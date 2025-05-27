from collections import defaultdict

def edges2adjlist(edges):
    adjlist = defaultdict(list)
    for u, v in edges:
        adjlist[u].append(v)
    return adjlist

def bfs(n, edges): # full BFS procedure for the whole graph
    def _BFS(v): # do one BFS from v
        queue = [v] # start node
        for u in queue: # pop u logically but not physically from queue
            order.append(u) # BFS visit order
            for w in adjlist[u]: # u->w
                if color[w] == 0: # only if gray->white (tree edge)
                    queue.append(w)
                    color[w] = 1 # gray
            color[u] = 2 # black: i'm done

    adjlist = edges2adjlist(edges) # convert edges to adjaency list
    color = defaultdict(int) # default 0: white
    order = [] # output
    for v in range(n):
        if color[v] == 0: # only do BFS on white nodes
            _BFS(v) # another BFS tree in BFS forest
    return order

def dfs(n, edges): # DFS for the whole graph
    def _DFS(v): # recursive
        color[v] = 1 # gray
        order.append(v)
        for u in adjlist[v]: # v->u
            if color[u] == 0: # tree edge (gray->white)
                _DFS(u)
        color[v] = 2 # black

    adjlist = edges2adjlist(edges) # convert edges to adjacency list
    color = defaultdict(int) # default 0: white
    order = [] # output
    for v in range(n): # no need for this loop if there is "God" node
        if color[v] == 0:
            _DFS(v) # another DFS tree

    return order

print(bfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)]))
print(dfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)]))