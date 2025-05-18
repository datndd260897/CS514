from collections import defaultdict


def best_knapsack_bottom_up(W, items):
    back = {}
    best = defaultdict(int)
    for w in range(1, W+1):
        for i, (weight, value) in enumerate(items):
            if w >= weight:
                ans = best[w - weight] + value
                if ans > best[w]:
                    best[w] = ans
                    back[w] = i
    return best[W], solution(W, back, items)

def best_knapsack_topdown(W, items):
    back = {}
    best = defaultdict(int)
    def _dp(w):
        if w in best:
            return best[w]
        for i, (weight, value) in enumerate(items):
            if w >= weight:
                ans = _dp(w - weight) + value
                if ans > best[w]:
                    best[w] = ans
                    back[w] = i
        return best[w]
    return _dp(W), solution2(W, back, items)


def solution(w, back, items):
    if w not in back:
        return [0] * len(items)
    i = back[w]
    wi = items[i][0]
    result = solution(w - wi, back, items)
    result[i] += 1
    return result

def solution2(w, back, items):
    result = [0] * len(items)
    while w > 0:
        if w not in back: # base case (bag may be non-empty)
            break
        i = back[w]
        weight = items[i][0]
        result[i] += 1
        w -= weight
    return result



print(best_knapsack_bottom_up(29, [(5, 9), (9, 18), (6, 12)]))
print(best_knapsack_topdown(29, [(5, 9), (9, 18), (6, 12)]))