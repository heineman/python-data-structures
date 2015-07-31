"""
    Example Single Source Shortest Path with different
    graph implementations

    Author: George Heineman
"""
from directedGraphAL import DirectedGraphAL
from directedGraphAM import DirectedGraphAM
from dijkstra import singleSourceShortest

d = DirectedGraphAM(6)
d.addEdge(0,1,6)
d.addEdge(0,3,18)
d.addEdge(0,2,8)
d.addEdge(1,4,11)
d.addEdge(4,5,3)
d.addEdge(2,3,9)
d.addEdge(5,2,7)
d.addEdge(5,3,4)

dist = singleSourceShortest(d, 0)
print (dist)


d = DirectedGraphAL(6)
d.addEdge(0,1,6)
d.addEdge(0,3,18)
d.addEdge(0,2,8)
d.addEdge(1,4,11)
d.addEdge(4,5,3)
d.addEdge(2,3,9)
d.addEdge(5,2,7)
d.addEdge(5,3,4)

dist = singleSourceShortest(d, 0)
print (dist)

# Following will only work if you have installed
# pygraph [https://github.com/pmatiello/python-graph.git]
# once downloaded install, viz. "python3.4 setup.py install"
#
try:
    from pygraph.classes.digraph import digraph
    from pygraph.algorithms.minmax import shortest_path

    g = digraph()
    g.add_nodes([0,1,2,3,4,5])

    g.add_edge((0, 1), wt=6)
    g.add_edge((0, 3), wt=18)

    g.add_edge((0,2), wt=8)
    g.add_edge((1,4), wt=11)
    g.add_edge((4,5), wt=3)
    g.add_edge((2,3), wt=9)
    g.add_edge((5,2), wt=7)
    g.add_edge((5,3), wt=4)

    x = shortest_path(g, 0)
    print (x[1])

except Exception:
    print ()
    print ("To complete this example, you need to install pygraph.")
    print ("   https://github.com/pmatiello/python-graph.git")
    
