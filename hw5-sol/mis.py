# max_wis and max_wis2 are O(n) time & space (required)
# max_wis3 is O(n) time and O(1) space (not required)
# max_wis4 is O(n^2) time & space (BAD!)

def max_wis(a): # top-down; required
    best = {-1:0, -2:0} # 0-based index
    back = {}
    n = len(a)
    def top_down(i):
        if i not in best:
            best[i] = max(top_down(i-1), top_down(i-2)+a[i])
            back[i] = best[i] == best[i-1] # True if NOT take a[i]
        return best[i]

    return top_down(n-1), solution(n-1, a, back)

def max_wis2(a): # bottom-up; required
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        back[i] = best[i] == best[i-1] # True if not take i
    return best[n-1], solution(n-1, a, back)

def solution0(i, a, back): # recursive backtracing; BAD: O(n^2) time
    if i < 0:
        return []
    # BAD: this ... + [a[i]] below is O(n) time!
    return solution0(i-1, a, back) if back[i] else (solution0(i-2, a, back) + [a[i]])

def solution1(i, a, back): # recursive backtracing; good: O(n) time
    if i < 0:
        return []
    # use __iadd__ (+=) to ensure O(1) time
    return solution1(i-1, a, back) if back[i] else solution1(i-2, a, back).__iadd__([a[i]])

def solution2(_, a, back): # non-recursive; loop+reverse; O(n) time
    sol = []
    i = len(a)-1
    print(back)
    while i >= 0: # backward from n-1
        if not back[i]: # take
            sol.append(a[i])
            i -= 2
        else:
            i -= 1
    print(back)
    return sol[::-1] # reverse the order

solution = solution1

def max_wis4(a): # BAD: storing subsolutions slows it down to O(n^2)
    best = {-1: 0, -2: 0}
    path = {-1: [], -2: []}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        path[i] = path[i-1] if best[i] == best[i-1] else path[i-2] + [a[i]]
    return best[n-1], path[n-1]

def max_wis5(a): # O(n) but wrong! (try [9,10,9,2,1,3])
    best = {-1: 0, -2: 0}
    path = {-2: [], -1: []}
    print(path)
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        path[i] = path[i-1] if best[i] == best[i-1] else path[i-2].__iadd__([a[i]])
        print(i, path)
    print(path)
    return best[n-1], path[n-1]

if __name__ == "__main__":

    # print(max_wis5([9,10,9,2,1,3]))
    print(max_wis([9,10,9,2,1,3]))
    print(max_wis2([9,10,9,2,1,3]))
    print(max_wis4([9, 10, 9, 2, 1, 3]))
    exit()

    # import sys, random
    # sys.setrecursionlimit(1000000)
    #
    # example = [9, 10, 8, 5, 2, 4]
    # print(max_wis2(example))
    #
    # #lst = [random.randint(-1e5,1e5) for _ in range(20000)]
    #
    # from time import time
    # for n in [2500, 5000, 10000, 20000]: #, 10000000, 100000000]:
    #     a = [random.randint(-1e5,1e5) for _ in range(n)]
    #     t = time()
    #     solution = solution0
    #     sol1 = max_wis2(a)
    #     time1 = time() - t
    #
    #     solution = solution1
    #     t = time()
    #     sol2 = max_wis2(a)
    #     time2 = time() - t
    #
    #     solution = solution2
    #     t = time()
    #     sol3 = max_wis2(a)
    #     time3 = time() - t
    #
    #     t = time()
    #     sol4 = max_wis4(a) # O(n^2)
    #     time4 = time() - t
    #
    #     t = time()
    #     solution = solution2
    #     sol5 = max_wis(a) # top-down
    #     time5 = time() - t
    #     print("%6d %.3f %.3f %.3f %.3f %.3f" % (n, time1, time2, time3, time4, time5),
    #           sol1 == sol2 == sol3 == sol4 == sol5)
        
    # t = time()
    # a = max_wis(lst)
    # print("max_wis : top-down\t", time() -t) 
    # t = time()
    # b = max_wis2(lst)
    # print("max_wis2: bottom-up\t", time() -t) 
    # t = time()
    # c = max_wis3(lst)
    # print("max_wis3: bit oper.\t", time() -t) 
    # t = time()
    # d = max_wis4(lst)
    # print("max_wis4: slow (subsol)\t", time() - t)
    # print(a == b == c == d) # verify result
    # #print(a==b)

