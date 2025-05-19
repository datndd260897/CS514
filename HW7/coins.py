from collections import defaultdict

# def smallest(X, v):
#     best = [X+1] * (X+1)
#     best[0] = 0
#     back = {}
#     def _dp(x):
#         if best[x] != X + 1:  # already computed
#             return best[x]
#         for index, value in enumerate(v):
#             if x - value >= 0:
#                 coins = _dp(x - value) + 1
#                 if coins < best[x]:
#                     best[x] = coins
#                     back[x] = index
#         return best[x]
#     return _dp(X), solution2(X, back, v)



# def solution(X, back, v):
#     res = []
#     while X > 0:
#         chosen_index = back[X]
#         chosen_value = v[chosen_index]
#         res.append(chosen_value)
#         X -= chosen_value
#     return res

def solution2(X, back, v):
    if X not in back:
        return []
    chosen_index = back[X]
    chosen_value = v[chosen_index]
    res = solution2(X - chosen_value, back, v)
    res.append(chosen_value)
    return res


def smallest(amount, coins):
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0
    back = {}
    for i in range(1, amount + 1):
        for index, c in enumerate(coins):
            if i - c >= 0:
                ans = 1 + min_coins[i - c]
                if ans < min_coins[i]:
                    min_coins[i] = ans
                    back[i] = index
    return min_coins[-1] if min_coins[-1] != amount + 1 else 0, solution2(amount, back, coins)


print(smallest(6, [1,5]))
print(smallest(1, [2]))
print(smallest(6, [1,3,4]))
print(smallest(87, [1,5,10,25]))
print(smallest(25, [2,4,6]))
