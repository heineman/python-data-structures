Module 6 Graph-based Structures

Note

  binaryHeap.py and dijkstra.py are copies of files from (Heap-based Structures, module 5)

Amendment

  An Adjacency Matrix representation of a Graph was also developed using numpy. However,
  its performance comes nowhere close to the one provided that uses dictionaries.
  Ultimately, Python cannot effectively use a matrix-based representation because it
  doesn't have a true multi-dimensional array.


Change Log

2015.07.31    Original implementation in dijkstra.py used G.nodes() to get nodes. 
              Since we restrict to specific range, changed to range(len(G)).
              This was done primarily to allow us to use this class
              unchanged in the next module (6. Graph Representation)
