def best(W, items):
    from functools import lru_cache

    n = len(items)

    # @lru_cache(maxsize=None)
    def dp(w):
        if w == 0:
            return 0, [0]*n
        max_val = 0
        best_combo = [0]*n
        for i, (wi, vi) in enumerate(items):
            if w >= wi:
                val, combo = dp(w - wi)
                val += vi
                new_combo = combo[:]
                new_combo[i] += 1
                if val > max_val or (val == max_val and new_combo > best_combo):
                    max_val = val
                    best_combo = new_combo
        return max_val, best_combo

    return dp(W)


print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(3, [(2, 4), (3, 5)]))
print(best(3, [(1, 2), (2, 5)]))