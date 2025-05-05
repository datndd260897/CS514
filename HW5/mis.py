# Maximum Weighted Independent Set (WIS)
def max_wis(nums):
    n = len(nums)
    if n == 0:
        return (0, [])

    # Dynamic Programming approach (bottom-up)
    dp = [0] * (n + 1)
    chosen = [False] * n  # To track which elements are chosen

    dp[0] = 0
    dp[1] = max(0, nums[0])

    for i in range(2, n + 1):
        if dp[i - 1] > dp[i - 2] + nums[i - 1]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 2] + nums[i - 1]
            chosen[i - 1] = True

    # Backtrack to find the chosen elements
    selected = []
    i = n - 1
    while i >= 0:
        if chosen[i]:
            selected.append(nums[i])
            i -= 2  # Skip the adjacent element
        else:
            i -= 1

    return (dp[n], selected[::-1])


# Test cases
print(max_wis([7, 8, 5]))  # Output: (12, [7, 5])
print(max_wis([-1, 8, 10]))  # Output: (10, [10])
print(max_wis([]))  # Output: (0, [])
print(max_wis([-5, -1, -4]))  # Output: (0, [])
