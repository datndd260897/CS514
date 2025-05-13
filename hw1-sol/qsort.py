#!/usr/bin/env python3

import sys

def sort(a): # buggy qsort, returns BST
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree): # worst-case O(n^2): sorted(sort([1,2,3,...]))
    return [] if tree == [] else sorted(tree[0]) + [tree[1]] + sorted(tree[2])

def sorted2(tree): # O(n)
    result = [] # local variable
    def _sorted(tree): # function inside function
        if tree == []:
            return 
        left, root, right = tree
        _sorted(left)
        result.append(root) # O(1)
        _sorted(right)
    _sorted(tree)
    return result

def _search(tree, x):
    if tree == [] or tree[1] == x:
        return tree # return the address
    return _search(tree[0], x) if x < tree[1] else _search(tree[2], x)

def search(tree, x):
    return _search(tree,x) != []

def insert(tree, x):
    r = _search(tree, x)
    if r == []:
        r += [[], x, []] # N.B.: NOT r = [[], x, []] !!!

def pp(tree, dep=0): # reverse in-order traversal
    if tree == []:
        return
    left, root, right = tree
    pp(right, dep+1)
    print(" |" * dep, root)
    pp(left, dep+1)

if __name__ == '__main__':
    tree = sort([4,2,6,3,5,7,1,9])
    print(tree)
    pp(tree)
    t1 = sorted2(tree) # fast
    print("sorted", t1)    
    print("search for 6", search(tree, 6))
    print("search for 6.5", search(tree, 6.5))
    insert(tree, 6.5)
    print("after inserting 6.5")
    pp(tree)
    insert(tree, 3)
    print("after inserting 3")
    pp(tree)
    
    tree = sort([4,2,6,3,5,7,1,9])        # starting from the initial tree
    print(tree)
    pp(tree)
    print("_search for 3", _search(tree, 3))
    print("_search for 0", _search(tree, 0))
    print("_search for 6.5", _search(tree, 6.5))
    print(_search(tree, 0) is _search(tree, 6.5))
    print(_search(tree, 0) == _search(tree, 6.5))
