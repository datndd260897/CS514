# def best(W, items):
#     from functools import lru_cache
#
#     n = len(items)
#
#     @lru_cache(maxsize=None)
#     def dp(w):
#         if w == 0:
#             return 0, [0]*n
#         max_val = 0
#         best_combo = [0]*n
#         for i, (wi, vi) in enumerate(items):
#             if w >= wi:
#                 val, combo = dp(w - wi)
#                 val += vi
#                 new_combo = combo[:]
#                 new_combo[i] += 1
#                 if val > max_val or (val == max_val and new_combo > best_combo):
#                     max_val = val
#                     best_combo = new_combo
#         return max_val, best_combo
#
#     return dp(W)

def best(W, items):
    """
    :param W: weight of bag
    :param items: weight and value of each item [(2, 4), (4, 9)]
    :return: best value and list item in bag
    """
    #memo
    best = {}
    n = len(items)

    def dp(w):
        if w in best:
            return best[w]

        # Base case: if weight is 0, no items can be taken
        if w == 0:
            return 0, [0] * n

        max_value = 0
        best_combination = [0] * n

        #Try every item to see if we can take it
        for i, (item_weight, item_value) in enumerate(items):
            if w >= item_weight:
                remaining_value, remainning_combination = dp(w - item_weight)
                total_value = item_value + remaining_value

                #If this option gives a better value, update max_value and item combination
                if total_value > max_value:
                    max_value = total_value
                    best_combination = remainning_combination[:]
                    best_combination[i] += 1
                elif total_value == max_value and remainning_combination[::-1] < best_combination[::-1]:
                    best_combination = remainning_combination[:]
                    best_combination[i] += 1

        best[w] = (max_value, best_combination)
        return best[w]
    return dp(W)

print(best(29, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(3, [(2, 4), (3, 5)]))
print(best(3, [(1, 2), (2, 5)]))