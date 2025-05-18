def no_bitstring(n):
    back = {0: 1, 1: 2}
    def dp(n):
        if n < 2:
            return back[n]
        if n not in back:
            back[n] = dp(n - 1) + dp(n - 2)
        return back[n]
    dp(n)
    return back[n]

yes_bitstring = lambda n: 2**n - no_bitstring(n)


print(no_bitstring(3))
print(yes_bitstring(3))
print(no_bitstring(5))
print(yes_bitstring(5))


def num_no(n): # similar to O(1)-space Fibonacci
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return b

num_yes = lambda n: 2**n - num_no(n)


print(num_yes(3))
print(num_no(3))
print(num_no(5))
print(num_yes(5))


