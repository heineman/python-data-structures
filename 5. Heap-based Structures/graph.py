"""
    Rudimentary graph structure maintains dict of vertices. In this
    dict, each key is a vertex and each value is another dict which
    contains the neighbors and their weights.

    Author: George Heineman
"""
class DirectedGraph:
    def __init__(self):
        self.vertices = {}

    def nodes(self):
        """Return iterator of nodes."""
        for _ in self.vertices:
            yield _

    def addEdge(self, u, v, weight):
        """Add edge (u,v) of given weight to graph."""
        if u not in self.vertices:
            neighbors = {}
            self.vertices[u] = neighbors
        else:
            neighbors = self.vertices[u]

        neighbors[v] = weight

        # Be sure to opportunistically add v if not present
        if v not in self.vertices:
            self.vertices[v] = {}

    def addNode(self, u):
        """Add node to graph independent of edges."""
        if u in self.vertices:
            return
        self.vertices[u] = {}

    def neighbors(self, u):
        """Yield all neighbors of u as tuple (v,weight)."""
        if not u in self.vertices:
            return
        for v in self.vertices[u]:
            yield (v, self.vertices[u][v])

    def __repr__(self):
        """Representation of graph."""
        rep = 'graph:['
        for u in self.vertices:
            rep += str(u) + ':'
            for v in self.vertices[u]:
                rep += str(v) + '@' + str(self.vertices[u][v]) + ' '
            rep += ','
        return rep + ']'
    
