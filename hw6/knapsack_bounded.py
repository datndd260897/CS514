def best(W, items):
    from functools import lru_cache

    n = len(items)

    @lru_cache(maxsize=None)
    def dp(i, w):
        if i == n:
            return 0, [0] * n
        wi, vi, ci = items[i]
        max_val = 0
        best_combo = [0] * n
        for k in range(0, min(ci, w // wi) + 1):
            val, combo = dp(i + 1, w - k * wi)
            val += k * vi
            new_combo = combo[:]
            new_combo[i] = k
            if val > max_val or (val == max_val and new_combo > best_combo):
                max_val = val
                best_combo = new_combo
        return max_val, best_combo

    return dp(0, W)



print(best(3, [(2, 4, 2), (3, 5, 3)]))  # Output: (5, [0, 1])
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))  # Output: (130, [6, 4, 1])
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))


