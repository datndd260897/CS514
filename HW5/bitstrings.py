# Number of bit strings of length n with no two consecutive 0s
def num_no(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Number of bit strings of length n with two consecutive 0s
def num_yes(n):
    return 2**n - num_no(n)

# Test cases
print(num_no(3))  # Output: 5
print(num_yes(3))  # Output: 3
