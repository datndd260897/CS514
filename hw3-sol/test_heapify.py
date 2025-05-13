#!/usr/bin/env python3

import random
import time
import heapq

for i in range(5):
    n = 1000000 * 2**i
    a = list(range(n, 0, -1))  # worst-case input
    h = a.copy()
    t = time.time()
    heapq.heapify(h)
    t1 = time.time()
    h = []
    for x in a:
        heapq.heappush(h, x)
    t2 = time.time()
    print("n=%9d heapify: %.3f  n heappushes: %.3f ratio: %.1f" % (n, t1-t, t2-t1, (t2-t1)/(t1-t)))
    
