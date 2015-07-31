"""
    Dijkstra's Single Source Shortest Path Algorithm

    Uses ability to increase priority of existing element.
    In a BinaryHeap, all values are inserted initially, then
    thereafter, only removals and reprioritizations occur.

    Author: George Heineman
"""

from binaryHeap import BinaryHeap
import sys

def singleSourceShortest(G, src):
    """
    Given graph G return dictionary of shortest paths to other vertices
    from vertex src. All vertices in G must be drawn from the range 0..n-1
    and src must also be from same range.
    """
    # Initialize dist[] matrix to be Infinity for all but src
    infinity = sys.maxsize
    n = 0
    dist = {}
    for v in range(len(G)):
        n += 1
        dist[v] = infinity

    dist[src] = 0

    # optimized construction for BinaryHeap
    pq = BinaryHeap(n, src, infinity)

    while not pq.isEmpty():
        u = pq.pop()
        for v,weight in G.neighbors(u):
            newLen = dist[u] + weight
            if newLen < dist[v]:
                pq.decreaseKey(v, newLen)
                dist[v] = newLen

    
    return dist

"""
Change Log:
-----------
2015.07.31    Original implementation used G.nodes() to get nodes. Since
              we restrict to specific range, changed to range(len(G)).
              This was done primarily to allow us to use this class
              unchanged in the next module (6. Graph Representation)
"""
