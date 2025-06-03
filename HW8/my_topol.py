from collections import defaultdict

def edges2adjlist(edges):
    adjlist = defaultdict(list)
    color = defaultdict(int)
    for u, v in edges:
        adjlist[u].append(v)
        color[v] += 1
    return adjlist, color

def order(n, edges):
    adjlist, color = edges2adjlist(edges)
    queue = [v for v in range(n) if color[v] == 0]
    order = []
    for u in queue:
        order.append(u)
        for v in adjlist[u]:
            color[v] -= 1
            if color[v] == 0: queue.append(v)

    return order

class CycleException(Exception): pass # define my own exception

def order2(n, edges):  # top-down, recursive, memoization

    def visit(v):  # DFS
        if color[v] == 1:  # gray
            raise CycleException("cycle detected")
        elif color[v] == 0:  # white: visit (if black: return -- memoization)
            color[v] = 1  # becomes gray
            for u in prereqs[v]:
                visit(u)
            color[v] = 2  # now black; done
            out.append(v)  # take this course now

    prereqs = defaultdict(list)  # incoming edges
    for u, v in edges:  # u->v
        prereqs[v].append(u)

    color = defaultdict(int)  # default: white (0)
    out = []  # topological order (output)
    try:
        for u in range(n):  # DFS on each non-visited node
            visit(u)  # try to visit u if it's white
    except CycleException:  # important: only catch my own exception
        return out  # cycle detected; out is not the whole set
    return out



print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order2(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))