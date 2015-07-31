"""
    Adjacency List Graph representation
    
    Rudimentary graph structure maintains vector of neighbors for
    each vertex. Assume that size of graph is known in advance and
    doesn't change. Assume all vertices are integers in range 0..size-1

    Author: George Heineman
"""

class DirectedGraphAL:
    def __init__(self, size):
        self.size = size
        self.vertices = [None]*size

    def __len__(self):
        """Return number of nodes in the graph."""
        return self.size

    def addEdge(self, u, v, weight):
        """Add edge (u,v) of given weight to graph."""
        if self.vertices[u] is None:
            self.vertices[u] = []

        # if v already present, remove 
        for e in self.vertices[u]:
            if e[0] == v:
                self.vertices[u].remove(e)
                break

        # add (v, weight) tuple to list
        self.vertices[u].append((v, weight))

    def neighbors(self, u):
        """Yield all neighbors of u as tuple (v,weight)."""
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield (e)

    def __repr__(self):
        """Representation of graph."""
        rep = 'graph:['
        for u in range(self.size):
            if self.vertices[u]:
                rep += str(u) + ":"
                rep += ','.join(map(str,self.vertices[u]))
                rep += ';'
        return rep + ']'
