from collections import defaultdict


def can_pair(x, y):
    return (x, y) in [('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')]

def best(rna):
    n = len(rna)

    # Use defaultdict for dp to automatically initialize with 0
    dp = defaultdict(lambda: 0)
    # Use dict for traceback
    traceback = defaultdict(lambda: tuple)

    # Fill DP table
    for span in range(2, n + 1):  # span goes from 2 to n
        for i in range(n - span + 1):  # i goes from 0 to n - span
            j = i + span - 1  # calculate j based on span
            # Case 1: j is unpaired
            dp[i, j] = dp[i, j - 1]
            traceback[i, j] = -1  # inherit the value without pairing j

            # Case 2: j pairs with some k (i <= k < j)
            for k in range(i, j):
                if can_pair(rna[k], rna[j]):
                    val = dp[i, k - 1] + dp[k + 1, j - 1] + 1
                    if val > dp[(i, j)]:
                        dp[i, j] = val
                        traceback[i, j] = k

    def tracebacking(i, j):
        if i > j:
            return ''
        if i == j:
            return '.'
        k = traceback[i, j]
        if k == -1:
            return tracebacking(i, j - 1) + '.'
        else:
            left = tracebacking(i, k - 1) if k - 1 >= i else ''
            middle = '(' + tracebacking(k + 1, j - 1) + ')'
            return left + middle

    return dp[0, n - 1], tracebacking(0, n - 1)


# Test the function
print(best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU"))
print(best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC"))
print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))

def total(rna):
    n = len(rna)
    # Use defaultdict for dp to automatically initialize with 0
    dp = defaultdict(lambda: 1)

    # Fill DP table
    for span in range(2, n + 1):  # span goes from 2 to n
        for i in range(n - span + 1):  # i goes from 0 to n - span
            j = i + span - 1  # calculate j based on span
            # Case 1: j is unpaired
            dp[i, j] = dp[i, j - 1]
            # Case 2: j pairs with some k (i <= k < j)
            for k in range(i, j):
                if can_pair(rna[k], rna[j]):
                    dp[i, j] += dp[i, k - 1] * dp[k + 1, j - 1]
    return dp[0, n - 1]

print(total("ACAGU"))
