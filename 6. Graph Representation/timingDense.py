"""
    Timing comparison using dense graphs.

    Author: George Heineman
"""

from directedGraphAL import DirectedGraphAL
from directedGraphAM import DirectedGraphAM
from dijkstra import singleSourceShortest

import timeit

construct = '''
# Have every node v connect to every other node
for idx in range(n):
    for target in range(n):
        if target != idx:
            d.addEdge(idx, target, random.randint(1,100))
'''

for n in [2**k for k in range(8,14)]:
    setup='''
from directedGraphAL import DirectedGraphAL
import random
n = ''' + str(n) + '''
d = DirectedGraphAL(n)
''' + construct
    
    stmt = '''
from dijkstra import singleSourceShortest
dist=singleSourceShortest(d,0)
'''

    ms = timeit.timeit(setup=setup, stmt=stmt,number=100)
    
    print ("  AL", n, ms)

    setup='''
from directedGraphAM import DirectedGraphAM
import random
n = ''' + str(n) + '''
d = DirectedGraphAM(n)
''' + construct
    
    stmt = '''
from dijkstra import singleSourceShortest
dist=singleSourceShortest(d,0)
'''
    ms = timeit.timeit(setup=setup, stmt=stmt,number=100)
    
    print ("  AM", n, ms)

# Following will only work if you have installed
# pygraph [https://github.com/pmatiello/python-graph.git]

    try:
        setup='''
from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import shortest_path
from directedGraphAM import DirectedGraphAM
n = ''' + str(n) + '''
d = digraph()
d.add_nodes(list(range(n)))
    
# thereafter, all lines of form u,v,weight
for idx in range(1, numEdges+1):
    uS,vS,wS = content[idx].split(',')
    d.add_edge((int(uS), int(vS)), wt=int(wS))
'''
        stmt = 'dist = shortest_path(d, 0)'

        ms = timeit.timeit(setup=setup, stmt=stmt,number=100)
    
        print (" 3rd", f, ms)
    except:
        pass

"""
Sample Output:


"""
