"""
    Example Single Source Shortest Path. These are drawn from
    "Algorithms in a Nutshell (1ed)", pp. 154 and 155

    Author: George Heineman    
"""
from dijkstra import *
from graph import DirectedGraph

d = DirectedGraph()
d.addEdge(0,1,2)
d.addEdge(0,4,4)
d.addEdge(1,2,3)
d.addEdge(2,4,1)
d.addEdge(2,3,5)
d.addEdge(3,0,8)
d.addEdge(4,3,7)

print (d)

dist = singleSourceShortest(d, 0)

print (dist)

d = DirectedGraph()
d.addEdge(0,1,6)
d.addEdge(0,3,18)
d.addEdge(0,2,8)
d.addEdge(1,4,11)
d.addEdge(4,5,3)
d.addEdge(2,3,9)
d.addEdge(5,2,7)
d.addEdge(5,3,4)

print (d)

dist = singleSourceShortest(d, 0)

print (dist)
