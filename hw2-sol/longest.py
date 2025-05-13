#!/usr/bin/env python3

import time
import sys

def _longest(tree):
    if tree == []:
        return 0, 0
    dep_left, max_left = _longest(tree[0])
    dep_right, max_right = _longest(tree[2])
    return max(dep_left, dep_right) + 1, max(max_left, max_right, dep_left + dep_right)

longest = lambda tree: _longest(tree)[1]

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[],1,[]], 2, [[],3,[]]]))

