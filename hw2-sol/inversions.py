#!/usr/bin/env python3

def _mergesorted_inv(left, right): # python3 doesn't support ((a, numa), (b, numb)) as arguments
    (a, numa), (b, numb) = left, right
    if a == [] or b == []:
        return a+b, numa+numb
    c, numc = [], numa+numb
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            c.append(b[j])
            j += 1
            numc += la-i
        else:
            c.append(a[i])
            i += 1
    return c, numc

def _mergesort_inv(a):
    l = len(a)
    if l <= 1:
        return a, 0
    return _mergesorted_inv(_mergesort_inv(a[:l//2]), _mergesort_inv(a[l//2:]))

def num_inversions(a):
    return _mergesort_inv(a)[1]

if __name__ == "__main__":
    tests = ["num_inversions([4, 1, 3, 2]) == 4",
             "num_inversions([2, 4, 1, 3]) == 3",
             "num_inversions(list(range(10))) == 0",
             "num_inversions(list(range(10))[::-1]) == 45",]

    results = True
    for test in tests:
        print("testing", test, t := eval(test))
        results &= t
    print("all passed" if results else "not passed")
        
