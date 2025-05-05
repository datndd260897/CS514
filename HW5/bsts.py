# Number of Binary Search Trees (BSTs) for n nodes
def bsts(n):
    # DP table to store results for subproblems
    dp = [0] * (n + 1)
    dp[0] = 1  # There's 1 BST for an empty tree

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]


# Test cases
print(bsts(2))  # Output: 2
print(bsts(3))  # Output: 5
print(bsts(5))  # Output: 42
