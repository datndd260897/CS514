def fibonacci_bottom_up(n):
    F = [0] * (n)
    F[0] = 0
    F[1] = 1
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F, F[n - 1]

print(fibonacci_bottom_up(200)[1])

def fibonacci_top_down(i, memo = {}):
    if i in memo:
        return memo[i]
    if i <= 1:
        return i
    memo[i] = fibonacci_top_down(i - 1, memo) + fibonacci_top_down(i - 2, memo)
    return memo[i]

print(fibonacci_top_down(200))