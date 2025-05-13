import random

def qselect(k, a):
    i = random.randrange(len(a))
    a[0], a[i] = a[i], a[0] # the new a[0] is the pivot
    pivot = a[0] # randomized
    left = [x for x in a if x < pivot]
    remaining = k - len(left) - 1 # 1 is for pivot
    if remaining <= 0: # cases 1-2: no need to do right!
        return pivot if remaining == 0 else qselect(k, left)
    right = [x for x in a[1:] if x >= pivot]
    return qselect(remaining, right) # case 3

if __name__ == "__main__":
    print(qselect(2, [3, 10, 4, 7, 19]))


