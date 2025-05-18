import math
def bsts(n):
    back = {0: 1}
    def dp(i):
        if i not in back:
            back[i] = sum(dp(j) * dp(i - j- 1) for j in range(i))
        return back[i]
    return dp(n)

def bsts2(n): # top-down; almost identical
    num = {0:1}
    def _bst(i):
        if i not in num:
            num[i] = sum(_bst(j) * _bst(i-j-1) for j in range(i))
        return num[i]
    return _bst(n)

def bsts_balance(h):
    back = {0: 1, 1: 1 }
    def dp(i):
        if i not in back:
            back[i] = dp(i - 1)**2 + 2*(dp(i - 2) * dp(i - 1))
        return back[i]
    return dp(h)


print(bsts2(5))
print(bsts_balance(4))