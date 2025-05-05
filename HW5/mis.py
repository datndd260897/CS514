def max_wis(nums):
    n = len(nums)
    if n == 0:
        return (0, [])

    # Dynamic Programming approach (bottom-up)
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = max(0, nums[0])

    # Fill dp array with optimal solutions
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

    # Backtrack to find the chosen elements
    selected = []
    i = n - 1
    while i >= 0:
        if dp[i + 1] == dp[i]:  # Element at index i is not included
            i -= 1
        else:  # Element at index i is included
            selected.append(nums[i])
            i -= 2  # Skip adjacent element

    return (dp[n], selected[::-1])  # Reverse the selected list to maintain order


# Test cases
print(max_wis([7, 8, 5]))  # Expected Output: (12, [7, 5])
print(max_wis([-1, 8, 10]))  # Expected Output: (10, [10])
print(max_wis([]))  # Expected Output: (0, [])
print(max_wis([-5, -1, -4]))  # Expected Output: (0, [])
