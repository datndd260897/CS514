from random import randint
import heapq

def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)

def nbesta(a, b):
    c = [((x+y, y), (x,y)) for x in a for y in b] # decorate
    return [xy for _, xy in sorted(c)[:len(a)]] # sort and undecorate

def nbestb(a, b):
    c = [((x+y, y), (x,y)) for x in a for y in b]
    threshold = qselect(len(a), c) 
    result = [stuff for stuff in c if stuff <= threshold]
    return [xy for _, xy in sorted(result)[:len(a)]]

def nbestc(a, b): # default (symmetric) solution from (0, 0)
    def put(i, j):
        if i < n and j < n and (i, j) not in used:
            used.add((i, j))
            heapq.heappush(h, (a[i]+b[j], b[j], i, j)) # compare sum first, then 2nd dimension

    a.sort()
    b.sort()
    n = len(a)
    h, used = [], set()
    result = []

    put(0, 0)
    for _ in range(n):
        _, _, i, j = heapq.heappop(h)
        result.append((a[i], b[j]))
        put(i+1, j)
        put(i, j+1)
    return result

def nbestc2(a, b): # alternative (asymmetric) solution from (0, j) for all j
    # advantages: 1) single sort, 2) single successor (heapreplace), 
    # 3) no need to keep track of used (i, j) pairs
    # N.B.: very similar to team selection problem
    
    a.sort() # b remains unsorted
    n = len(a)
    h = [(a[0]+b[j], b[j], 0, j) for j in range(n)] # first column
    heapq.heapify(h) # initial heap
    result = []
    for _ in range(n):
        _, _, i, j = h[0]
        result.append((a[i], b[j]))
        if i + 1 < n: # pop and push one successor
            heapq.heapreplace(h, (a[i+1]+b[j], b[j], i+1, j))
        # N.B.: if no more successors, still no need to pop because 
        # in that case the result is all from that row (j)
        # and this is the end of the for loop
    return result

if __name__ == "__main__":
    a, b = [4,1,5,3], [4, 2,6,3]
    # print(nbesta(a,b))
    # print(nbestb(a,b))
    print(nbestc(a,b))
    # print(nbestc2(a,b))

    # print()
    # a, b = [4,1,5,3], [4,0,5,7]
    # print(nbesta(a,b))
    # print(nbestb(a,b))
    # print(nbestc(a,b))
    # print(nbestc2(a,b))
