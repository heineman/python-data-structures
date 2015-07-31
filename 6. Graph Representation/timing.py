"""
    Timing comparison using larger graphs stored on disk. These
    are neither sparse nor dense, but try to be "in between."

    Graph data files are drawn from "Algorithms in a Nutshell (1ed)".

    Author: George Heineman
"""

from directedGraphAL import DirectedGraphAL
from directedGraphAM import DirectedGraphAM
from dijkstra import singleSourceShortest

import timeit

files = ['benchmark-1.dat', 'benchmark-2.dat',
         'benchmark-3.dat', 'benchmark-4.dat']

for f in files:
    setup='''
from directedGraphAL import DirectedGraphAL
file = open ("''' + f + '''")
content = file.readlines()
file.close()
    
# numV numE is first line
vS,eS = content[0].split()
numVertices = int(vS)
numEdges = int(eS)
print ("vertices:", numVertices, "edges:", numEdges)
d = DirectedGraphAL(numVertices)
    
# thereafter, all lines of form u,v,weight
for idx in range(1, numEdges+1):
    uS,vS,wS = content[idx].split(',')
    d.addEdge(int(uS), int(vS), int(wS))
'''
    stmt = '''
from dijkstra import singleSourceShortest
dist=singleSourceShortest(d,0)
'''

    ms = timeit.timeit(setup=setup, stmt=stmt,number=100)
    
    print ("  AL", f, ms)

    setup='''
from directedGraphAM import DirectedGraphAM
file = open ("''' + f + '''")
content = file.readlines()
file.close()
    
# numV numE is first line
vS,eS = content[0].split()
numVertices = int(vS)
numEdges = int(eS)
d = DirectedGraphAM(numVertices)
    
# thereafter, all lines of form u,v,weight
for idx in range(1, numEdges+1):
    uS,vS,wS = content[idx].split(',')
    d.addEdge(int(uS), int(vS), int(wS))
'''
    ms = timeit.timeit(setup=setup, stmt=stmt,number=100)
    
    print ("  AM", f, ms)

# Following will only work if you have installed
# pygraph [https://github.com/pmatiello/python-graph.git]

    try:
        setup='''
from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import shortest_path
from directedGraphAM import DirectedGraphAM
file = open ("''' + f + '''")
content = file.readlines()
file.close()
    
# numV numE is first line
vS,eS = content[0].split()
numVertices = int(vS)
numEdges = int(eS)
d = digraph()
d.add_nodes(list(range(numVertices)))
    
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

vertices: 6 edges: 8
  AL benchmark-1.dat 0.00658211315649212
  AM benchmark-1.dat 0.006640907021352322
vertices: 18 edges: 56
  AL benchmark-2.dat 0.02384511176258757
  AM benchmark-2.dat 0.025866150867157017
vertices: 66 edges: 464
  AL benchmark-3.dat 0.126597189583267
  AM benchmark-3.dat 0.13712654084546277
vertices: 1026 edges: 31808
  AL benchmark-4.dat 4.10031983162557
  AM benchmark-4.dat 4.833211254405602

"""

