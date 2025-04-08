def _search(tree, x):
    """

    :param tree: tree
    :param x: value
    :return: (list)
    """
    if not tree:
        return []
    left, root, right = tree
    if x < root:
        return _search(left, x)
    elif x > root:
        return _search(right, x)
    else:
        return tree


def sorted(t):
    """

    :param t: tree
    :return: sorted array
    """
    if not t:
        return []
    left, root, right = t[0], t[1], t[2]
    return sorted(left) + [root] + sorted(right)

def search(t, x):
    """

    :param t: tree
    :param x: number
    :return: (boolean)
    """
    return _search(t, x) != []

def insert(t, x):
    """Inserts x into the tree (in-place) if it is missing, otherwise does nothing"""
    def _insert(t, x):
        if not t:
            return [[], x, []]
        left, root, right = t
        if x < root:
            t[0] = _insert(left, x)
        elif x > root:
            t[2] = _insert(right, x)
        return t

    if not _search(t, x):
        _insert(t, x)


def sort(a):
    """
    Quicksort
    :param a: array
    :return: sorted array
    """
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

if __name__ == "__main__":
    tree = sort([4,2,6,3,5,7,1,9])
    a = sorted(tree)
    print(a)
    print(search(tree, 6))
    print(search(tree, 6.5))
    insert(tree, 6.5)
    insert(tree, 3)
    print(tree)
