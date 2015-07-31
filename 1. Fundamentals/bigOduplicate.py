"""
    Demonstrate O(n) behavior with O(n) storage for determining whether
    list contains duplicate values

    Shows alternate implementation with O(n^2) behavior with O(1) storage
    to solve same problem

    Author: George Heineman
"""
import random
import timeit

def uniqueCheckFast(aList):
    """
    Return True if aList contains any duplicates. Its contents are not
    altered and completes in O(n) time with O(n) space required. The
    individual elements must be hashable.
    """
    check = set()
    for v in aList:
        if v in check:
            return True
        check.add(v)
    return False

def uniqueCheckSlow(aList):
    """
    Return True if aList contains any duplicates. Its contents are not
    altered and completes in O(n^2) time with no space required. 
    """
    for i in range(len(aList)-1):
        for j in range(i+1, len(aList)):
            if aList[i] == aList[j]:
                return True
    return False

print ('N\tSlow     \tFast')
for trial in [2**_ for _ in range(1,10)]:
    numbers = [random.random() for _ in range(trial)]
    mSlow = timeit.timeit(stmt='uniqueCheckSlow(numbers)',
                  setup='import random\nfrom __main__ import uniqueCheckSlow\nnumbers = ' + str(numbers),
                  number=1000)
    mFast = timeit.timeit(stmt='uniqueCheckFast(numbers)',
                  setup='import random\nfrom __main__ import uniqueCheckFast\nnumbers = ' + str(numbers),
                  number=1000)

    print ('{0:d}\t{1:f}\t{2:f}'.format(trial, mSlow, mFast))


"""
Sample Output:

N	Slow     	Fast
2	0.001619	0.001241
4	0.003531	0.001805
8	0.009362	0.003077
16	0.030581	0.006073
32	0.098761	0.011974
64	0.338519	0.020638
128	1.276854	0.043545
256	4.887293	0.080524
512	22.114716	0.173997
"""
