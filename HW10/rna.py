from collections import defaultdict
import heapq


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


def kbest(rna_sequence, num_best=3):
    """
    Given an RNA sequence, return the top-k (score, structure) pairs from the dynamic programming table.
    Each pair consists of (score, structure) where structure contains the (k, j) pairings that form the secondary structure.
    """
    length = len(rna_sequence)
    valid_pairs = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')}
    dp_table = defaultdict(list)  # Stores top-k results for subsequences

    def reconstruct_structure(i, j, level):
        """ Recursively reconstruct the RNA structure from the DP table. """
        structure = ['.'] * len(rna_sequence)  # Initialize the structure with dots

        def _reconstruct(i, j, level):
            """ Helper function for the recursive backtracking. """
            if i >= j:
                return
            score, pair, k, LeftLevel, RightLevel = dp_table[(i, j)][
                level]  # Retrieve the pair and its details from the DP table

            if not pair:  # If no pair is formed, explore the next subproblem
                _reconstruct(i, j - 1, LeftLevel)
            else:  # If pairing is formed, place parentheses and continue backtracking
                structure[k] = '('
                structure[j] = ')'
                _reconstruct(i, k - 1, LeftLevel)  # Explore the left side
                _reconstruct(k + 1, j - 1, RightLevel)  # Explore the right side

        _reconstruct(i, j, level)
        return ''.join(structure)  # Return the reconstructed structure as a string

    def get_top_k_structures(priority_queue):
        """ Select the top-k best structures using a max heap. """
        result = []
        visited = set()  # To avoid duplicates

        def try_to_add(k, pair, LeftIndex, RightIndex, left_structures, right_structures):
            """ Attempt to push new configurations onto the heap. """
            if not pair and LeftIndex < len(left_structures):
                score = left_structures[LeftIndex][0]
                heapq.heappush(priority_queue,
                               (-score, pair, k, LeftIndex, RightIndex, left_structures, right_structures))

            if pair and LeftIndex < len(left_structures) and RightIndex < len(right_structures) and (
                    (LeftIndex, RightIndex, id(left_structures), id(right_structures)) not in visited):
                score = left_structures[LeftIndex][0] + right_structures[RightIndex][0] + 1
                heapq.heappush(priority_queue,
                               (-score, pair, k, LeftIndex, RightIndex, left_structures, right_structures))
                visited.add((LeftIndex, RightIndex, id(left_structures), id(right_structures)))

                # Continue popping from the heap to find the top-k results

        while len(result) < num_best and priority_queue:
            score, pair, k, LeftIndex, RightIndex, left_structures, right_structures = heapq.heappop(priority_queue)
            result.append((-score, pair, k, LeftIndex, RightIndex))

            if not pair:  # No pair, move to the next possibility
                try_to_add(k, False, LeftIndex + 1, -1, left_structures, right_structures)
            elif pair:  # A pair is formed, explore both the left and right sides
                try_to_add(k, True, LeftIndex + 1, RightIndex, left_structures, right_structures)
                try_to_add(k, True, LeftIndex, RightIndex + 1, left_structures, right_structures)
        return result

    def compute_dp(i, j):
        """ Dynamic programming function to compute the top-k solutions for subsequence (i, j). """
        if i >= j:
            return [(0, False, -1, -1, -1)]  # Base case: no valid pair
        if (i, j) in dp_table:
            return dp_table[(i, j)]  # Return the cached result if already computed

        candidates = []

        # 1. Case: No pairing for j (consider the subproblem without j paired)
        left_structures = compute_dp(i, j - 1)
        candidates.append((-left_structures[0][0], False, -1, 0, -1, left_structures, []))

        # 2. Case: Try pairing (k, j) for all i <= k < j (consider all valid pairings)
        for k in range(i, j):
            if (rna_sequence[k], rna_sequence[
                j]) in valid_pairs:  # Check if the bases rna_sequence[k] and rna_sequence[j] can form a valid pair
                left_structures = compute_dp(i, k - 1)
                right_structures = compute_dp(k + 1, j - 1)
                score = left_structures[0][0] + right_structures[0][
                    0] + 1  # Calculate the score for the current pairing
                candidates.append((-score, True, k, 0, 0, left_structures, right_structures))

        heapq.heapify(candidates)  # Turn the list into a heap for easy extraction of top-k results
        top_k_candidates = get_top_k_structures(candidates)  # Get the top-k candidates from the heap
        dp_table[(i, j)] = top_k_candidates  # Cache the top-k solutions for subsequence (i, j)
        return dp_table[(i, j)]

    best_structures = compute_dp(0, len(rna_sequence) - 1)  # Get the list of top-k solutions for the entire sequence

    # Return the top-k structures and their scores by backtracking
    return [(_best[0], reconstruct_structure(0, len(rna_sequence) - 1, level)) for level, _best in
            enumerate(best_structures)]

print(kbest("ACAGU", 3))