"""
    Adjacency Matrix Graph representation
    
    Rudimentary graph structure maintains dict of vertices. In this
    dict, each key is a vertex and each value is another dict which
    contains the neighbors and their weights. Assume that size of graph
    is known in advance and doesn't change. Assume all vertices are
    integers in range 0..size-1

    Because of Python's lack of a true multidimensional array, the
    efficiency of the traditional Matrix-based representation will
    only be evident when constructing graphs, because its addEdge
    method will outperform the addEdge of an Adjacency List
    representation. Worse, the neighbors() invocation in the
    Adjacency List representation outperforms the Matrix representation.

    Author: George Heineman
"""
class DirectedGraphAM:
    def __init__(self, size):
        self.size = size
        self.vertices = {}

    def __len__(self):
        """Return number of nodes in the graph."""
        return self.size

    def addEdge(self, u, v, weight):
        """Add edge (u,v) of given weight to graph."""
        if not u in self.vertices:
            self.vertices[u] = {}

        self.vertices[u][v] = weight

    def neighbors(self, u):
        """Yield all neighbors of u as tuple (v,weight)."""
        if u in self.vertices:
            for v in self.vertices[u]:
                yield (v, self.vertices[u][v])

    def __repr__(self):
        """Representation of graph."""
        rep = 'graph:['
        for u in range(self.size):
            if u in self.vertices:
                rep += str(u) + ":"
                for v in self.vertices[u]:
                    rep += '(' + str(v) + ", " + str(self.vertices[u][v]) + '),'
        return rep + ']'
