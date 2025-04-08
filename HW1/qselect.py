import random

def qselect(k, a):
    """
    Quick selection algorithm.
    :param k: kth-smallest number in the array.
    :param a: arbitrary array
    :return:
    """
    i = random.randrange(len(a))
    a[0], a[i] = a[i], a[0]
    pivot = a[0]
    left = [x for x in a if x < pivot]
    remaining = k - len(left) - 1 # 1 is for pivot
    if remaining <= 0: # cases 1-2: no need to do right!
        return pivot if remaining == 0 else qselect(left, k)
    right = [x for x in a[1:] if x >= pivot]
    return qselect(right, remaining) # case 3

