CS 514, Algorithms, Spring 2025
HW3 - Priority Queue and Heaps

Due Monday 4/21, 9:59pm.
No late submission will be accepted.

Need to submit: report.txt, kmergesort.py, nbest.py, datastream.py.
nbest.py will be graded for correctness (1%).

To submit:
flip $ /nfs/guille/huang/cs514/submit 514 hw3 report.txt {kmergesort,nbest,datastream}.py
(You can submit each file separately, or submit them together.)

To see your best results so far:
flip $ /nfs/guille/huang/cs514/query 514 hw3


Textbooks for References:
[0] H 1.6, 1.7
[1] CLRS Ch. 6
[2] KT slides for binary heaps (only read the first 20 pages!): 
    https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/BinomialHeaps.pdf
[3] Python's built-in heapq module 

0. Summarize the time complexities of the basic operations (push, pop-min, peek, build) for these implementations of priority queue:

   (a) unsorted array
   (b) sorted array (highest priority first; i.e., "most urgent patient first")
   (c) reversely sorted array (lowest priority first)
   (d) sorted linked list (highest priority first)
   (e) binary heap

   Note: "build" just means to build a PQ from an unsorted list (e.g., heapify).

1. There are two methods for building a heap from an unsorted array:
   (1) insert each element into the heap  --- O(nlogn) -- n x heapq.heappush()
   (2) heapify                            --- O(n)     -- heapq.heapify()

   Derive these time complexities.

2. k-way mergesort (the classical mergesort is a special case where k=2).

   >>> kmergesort([4,1,5,2,6,3,7,0], 3)  # k=3
   [0,1,2,3,4,5,6,7]

   Q: What is the complexity? Write down the detailed analysis in report.txt.
      The resulting complexity is very interesting.

   Filename: kmergesort.py


3. [WILL BE GRADED -- but we only grade nbestc()]

   Given two lists A and B, each with n integers, return
   a sorted list C that contains the smallest n elements from AxB:

     AxB = { (x, y) | x in A, y in B }

   i.e., AxB is the Cartesian Product of A and B.

   ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')

   You need to implement three algorithms and compare:

   (a) enumerate all n^2 pairs, sort, and take top n.
   (b) enumerate all n^2 pairs, but use quickselect instead.
   (c) best-first, only enumerate O(n) (at most 2n) pairs.
       Note: this is known as "baby Dijkstra", due to static priorities.
       	    HW8 does real Dijkstra (priorities can change -- like in ER).

   >>> a, b = [4, 1, 5, 3], [2, 6, 3, 4]
   >>> nbesta(a, b)                 # algorithm (a), slowest
   [(1, 2), (1, 3), (3, 2), (1, 4)]
   >>> nbestb(a, b)                 # algorithm (b), still slow
   [(1, 2), (1, 3), (3, 2), (1, 4)]
   >>> nbestc(a, b)                 # algorithm (c), fast
   [(1, 2), (1, 3), (3, 2), (1, 4)]

   Q1: What are the time complexities of these algorithms? 
   Q2: If you use nbesta for nbestc, how many test cases can you pass?
       What about nbestb? 
       Note: just add a line after defining nbesta/nbestb/nbestc:

       nbestc = nbesta

       This line means you will use nbesta for nbestc.

   Filename: nbest.py -- only nbestc() will be tested


4. Find the k smallest numbers in a data stream of length n (k<<n),
   using only O(k) space (the stream itself is too big to fit in memory).

   >>> ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
   [2, 3, 5, 7]
   >>> ksmallest(3, range(1000000, 0, -1))
   [1, 2, 3]

   Your code should work for both lists and lazy lists:
      
   >>> ksmallest(5, (x**2 for x in range(10,0,-1)))
   [1, 4, 9, 16, 25]
   >>> import random; random.seed(1); ksmallest(5, (random.randint(0,100) for _ in range(10)))
   [8, 15, 17, 32, 57]   

   Note: 
   a) the output list should be sorted
   b) for both types of lists, you can always iterate:

      for x in a:
      	  ...

      but you can't do a[0] or a[-1] or len(a) on a lazy list.

      A lazy list is most often a "generator", which can be created in two simple methods:
      
      Lazy list examples:

      	  a = [x**2 for x in range(10)]   # a (non-lazy) list
      	  b = (x**2 for x in range(10))   # a generator (lazy list)

      	  the only difference is [...] vs (...)

      for more details, see:
      https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
      
   Q: What is your complexity? Write down the detailed analysis in report.txt.
   
   Filename: datastream.py

   Note: The built-in function heapq.nsmallest() is _not_ allowed.
       	 The whole point is to implement it yourself. :)


Debriefing (required!): --------------------------

0. What's your name?
1. Approximately how many hours did you spend on this assignment?
2. Would you rate it as easy, moderate, or difficult?
3. Did you work on it mostly alone, or mostly with other people?
   Note you are encouraged to discuss with your classmates, 
   but each students should submit his/her own code.
4. How deeply do you feel you understand the material it covers (0%-100%)? 
5. Take a moment to reflect on your quiz 1 performance. 
   For the problems you got wrong, do you know the correct answers now?
   What would you do to score better in quiz 2 and midterm?
6. Any comments on the Course Notes so far?

This section is intended to help us calibrate the homework assignments. 
Your answers to this section will *not* affect your grade; however, skipping it
will certainly do.
