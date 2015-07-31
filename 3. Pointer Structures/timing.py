"""
    Timing comparison of PrefixTreeDict and PrefixTreeLinkedList
    on random strings of given length
    
    Author: George Heineman
"""

import timeit
import random

letters = 'abcdefghijklmnopqrstuvwxyz'
defaultLen = 6

# stores the different trees constructed 
treesUsed = []

def addRandomStrings(tree, n, k):
    """Add n random strings of k lower-case letters each."""
    for _ in range(n):
        word = ''
        for _ in range(k):
            word += letters[random.randint(0,k-1)]
        tree.add(word)

    treesUsed.append(tree)

print ('N\tDict    \tLinkedList')
trials = [2**k for k in range(10,15)]
for t in trials:
    treesUsed.clear()
    
    stmt='''
import random
from __main__ import addRandomStrings
random.seed(' + str(t) + ')
addRandomStrings(tree,''' + str(t) + ',' + str(defaultLen) + ')'

    setupLL='''
from prefixTreeLinkedList import PrefixTreeLinkedList
tree = PrefixTreeLinkedList()
'''

    setupD='''
from prefixTreeDict import PrefixTree
tree = PrefixTree()
'''

    repeat = 5
    
    mcLL = timeit.timeit(stmt=stmt, setup=setupLL, number=repeat)
    mcD = timeit.timeit(stmt=stmt, setup=setupD, number=repeat)

    # compare strings stored by both trees
    list1 = list(iter(treesUsed[0]))
    list2 = list(iter(treesUsed[repeat]))
    list1.sort()
    list2.sort()
    assert(list1 == list2)
    
    print ('{0:d}\t{1:f}\t{2:f}'.format(t, mcLL, mcD))

"""
Sample Output:

N	Dict    	LinkedList
1024	0.126706	0.116916
2048	0.258611	0.241099
4096	0.511031	0.473042
8192	1.001074	0.937343
16384	1.988120	1.862958
"""
