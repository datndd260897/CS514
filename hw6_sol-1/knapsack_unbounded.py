#!/usr/bin/env python3

from collections import defaultdict

# O(nW) time; O(W) space
def best(W, items): # top-down
    back = {}
    
    def _best(w, opt=defaultdict(int)):
        if w in opt:
            return opt[w]
        for i, (w_i, v_i) in enumerate(items):
            if w >= w_i:
                ans = _best(w - w_i) + v_i
                if ans > opt[w]:
                    opt[w] = ans
                    back[w] = i
        return opt[w]

    return _best(W), solution(W, back, items)

def solution(w, back, items): # recursive backtracking
    if w not in back: # base case
        return [0] * len(items)
    i = back[w]
    w_i = items[i][0]
    res = solution(w - w_i, back, items)
    res[i] += 1 # take one more copy of item i
    return res

def solution2(w, back, items): # non-recursive backtracking
    res = [0] * len(items)
    print(back)
    while w > 0:
        if w not in back: # base case (bag may be non-empty)
            break
        i = back[w]
        w_i = items[i][0]
        res[i] += 1
        w -= w_i
    return res

def best2(W, items): # bottom-up
    back = {}
    opt = defaultdict(int)

    for w in range(1, W+1):
        for i, (w_i, v_i) in enumerate(items):
            if w >= w_i:
                ans = opt[w - w_i] + v_i
                if ans > opt[w]:
                    opt[w] = ans
                    back[w] = i
                    
    return opt[W], solution(W, back, items)

solution = solution2 # choose non-recursive backtracking

if __name__ == "__main__":

    # print(best(3, [(2, 4), (3, 5)]))
    print(best2(29, [(5, 9), (9, 18), (6, 12)]))
    # print(best(3, [(1, 5), (1, 5)]))
    # print(best(3, [(1, 2), (1, 5)]))
    # print(best(3, [(1, 2), (2, 5)]))
    #
    # print(best2(3, [(2, 4), (3, 5)]))
    # print(best2(3, [(1, 5), (1, 5)]))
    # print(best2(3, [(1, 2), (1, 5)]))
    # print(best2(3, [(1, 2), (2, 5)]))