"""
    Timing comparison using sparse graphs.

    Author: George Heineman
"""

from directedGraphAL import DirectedGraphAL
from directedGraphAM import DirectedGraphAM
from dijkstra import singleSourceShortest

import timeit

construct = '''
# Have every node v connect to v+1 % n and K random vertices
K = 5
for idx in range(n):
    d.addEdge(idx, (idx+1)%n, random.randint(1,100))
    for _ in range(K):
        target = random.randint(0,n-1)
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

  AL 256 0.5072258709803632
  AM 256 0.5567786001530739
  AL 512 1.12097502625601
  AM 512 1.1878565471693032
  AL 1024 2.3947315097669555
  AM 1024 2.5516383365395816
  AL 2048 5.141922790356826
  AM 2048 5.42714092784418
  AL 4096 10.940127547690398
  AM 4096 11.62373291347048
  AL 8192 23.258136563449604
  AM 8192 24.662680699269032
"""
