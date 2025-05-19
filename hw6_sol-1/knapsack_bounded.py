#!/usr/bin/env python3

from collections import defaultdict

def solution(i, w, back, a): # recursive backtracking
    if (w, i) not in back: # can't put any more items 
        #print(w, i)
        return [0] * (i+1) # N.B.: 0 copies for items 0..i 
    j = back[w, i] # number of copies taken for item i
    w_i = a[i][0]
    return solution(i - 1, w - j*w_i, back, a).__iadd__([j]) # O(1) __iadd__

def solution2(i, w, back, a): # non-recursive backtracking

    res = [0] * (i+1) # output (i == n-1)
    for i in range(i, -1, -1): # n-1 down to 0
        if (w, i) not in back: # can't put any more items in bag
            break  
        j = back[w, i] # number of copies taken for item i
        res[i] = j
        w_i = a[i][0]
        w -= j*w_i     # shrink bag
    return res

def print_table(dp, a, W):
        print("  |" + "".join("%3d" % w for w in range(W+1))) # header row
        print("--+" + "---" * (W+1))
        #print("0 |" + "".join("  0" for _ in range(W+1)))
        i = -1 # base case row (empty store)
        print(i+1, "|" + "".join(("%3d" % dp[w, i]) if (w, i) in dp else "   "\
                                  for w in range(W+1)))

        for i, _ in enumerate(a):
            print(i+1, "|" + "".join(("%3d" % dp[w, i]) if (w, i) in dp else "   "\
                                    for w in range(W+1)))

def best1(W, a, debug=False): # bottom-up

    dp = defaultdict(lambda : 0) # dp[w, i] is easier than dp[w][i]
    back = {}

    for i, (w_i, v_i, c_i) in enumerate(a): # 0-based in dp/back
        for w in range(1, W+1):
            for j in range(min(c_i, w//w_i)+1): # 0..c_i
                v = dp[w - j*w_i, i-1] + j*v_i
                if v > dp[w, i]:
                    dp[w, i] = v
                    back[w, i] = j
    if debug:
        print_table(dp, a, W)

    return dp[W, len(a)-1], solution(len(a)-1, W, back, a)

def best2(W, a, debug=False): # top-down

    dp = {}
    back = {}

    def _best2(w, i):
        if (w, i) not in dp: # this () is needed
            dp[w, i] = 0

            if w <= 0 or i < 0:
                return 0 # base case

            w_i, v_i, c_i = a[i]
            for j in range(min(c_i, w//w_i)+1):
                v = _best2(w - j*w_i, i-1) + j*v_i
                if v > dp[w, i]:
                    dp[w, i] = v
                    back[w, i] = j
        elif debug:
            print(f"{(w,i+1)} revisited!")

        return dp[w, i]
    
    ans = _best2(W, len(a)-1) # for debugging
    if debug:
        print_table(dp, a, W)

    return ans, solution(len(a)-1, W, back, a)

#solution = solution2 # choose non-recursive backtracking
best = best1 # choose bottom-up

if __name__ == "__main__":

    cases = [((20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]), (130, [6, 4, 1])),
             ((92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]), (236, [6, 7, 3, 7, 2]))
            ]
    for inp, out in cases:
        print("passed" if best(*inp) == out else "failed")

    # 0-1 version of KT slides example
    KT = [(1, 1, 1), (2, 6, 1), (5, 18, 1), (6, 22, 1), (7, 28, 1)]
    # print("bottom-up:")
    # print(best1(11, KT, True)) # bottom-up: dense table
    print("top-down:")
    print(best2(11, KT, True)) # top-down: sparse table
    print(KT)
    print()

