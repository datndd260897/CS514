def max_wis(a):
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    def _dp(i):
        if i not in best:
            best[i] = max(_dp(i - 1), _dp(i - 2) + a[i])
            back[i] = best[i] == best[i-1]
        return best[i]
    return _dp(n-1), solution2(n-1, a, back)

def solution(i, a, back):
    if i < 0:
        return []
    return solution(i -1, a, back) if back[i] else solution(i - 2, a, back).__iadd__([a[i]])

def solution2(i, a, back):
    resut = []
    while i >= 0:
        if not back[i]:
            resut.append(a[i])
            i -= 2
        else:
            i -= 1
    return resut[::-1]

print(max_wis([9,10,9,2,1,3]))
