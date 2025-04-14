def mergesorted(left, right):
    """
    Merge two sorted lists.
    :param left: left list
    :param right: right list
    :return: combined sorted list
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    elif j < len(right):
        result.extend(right[j:])
    return result

def mergesort(a):
    """
    Divide a list into two parts and combine them.
    :param a: array to be divided
    :return: sorted array
    """
    if (n:=len(a)) <= 1:
        return a
    return mergesorted(mergesort(a[:n//2]), mergesort(a[n//2:]))

if __name__ == '__main__':
    print(mergesort([4, 2, 5, 1, 6, 3]))


