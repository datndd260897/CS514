# Top-Down Approach (Recursive with Memoization)
def max_wis2(arr):
    n = len(arr)
    if n == 0:
        return (0, [])

    # Memoization for dp values and path reconstruction
    dp = [-1] * (n + 1)  # dp[i] will store the max sum up to index i
    path = [None] * (n + 1)  # path[i] will store the list of chosen elements up to index i

    def helper(i):
        if i < 0:
            return (0, [])
        if dp[i] != -1:
            return (dp[i], path[i])

        # Case 1: Skip the current element (index i)
        skip_val, skip_path = helper(i - 1)

        # Case 2: Include the current element (index i)
        include_val, include_path = helper(i - 2)
        include_val += arr[i]
        include_path = include_path + [arr[i]]

        # Choose the best between including or excluding
        if include_val > skip_val:
            dp[i] = include_val
            path[i] = include_path
        else:
            dp[i] = skip_val
            path[i] = skip_path

        return dp[i], path[i]

    # Start the helper function from the last index
    return helper(n - 1)


# Bottom-Up Approach (Iterative)
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
print(max_wis([-1, 8, 10]))  # Output: (10, [10])
print(max_wis([]))  # Output: (0, [])
print(max_wis([-5, -1, -4]))  # Output: (0, [])

print(max_wis2([7, 8, 5]))  # Expected Output: (12, [7, 5])
print(max_wis2([-1, 8, 10]))  # Output: (10, [10])
print(max_wis2([]))  # Output: (0, [])
print(max_wis2([-5, -1, -4]))  # Output: (0, [])
