"""
    KD Tree Implementation.
    
    If Add modifies the set, then return True, otherwise return False.
    Optional data can be associated with the nodes in the KD Tree.

    Author: George Heineman
"""

from region import maxRegion, X, Y

HORIZONTAL = 0
VERTICAL   = 1

class KDNode:

    def __init__(self, pt, orient, data = None, region = maxRegion):
        """Create empty KDNode."""
        self.point  = pt
        self.data   = data
        self.orient = orient
        self.above  = None
        self.below  = None
        self.region = region

    def createChild(self, pt, below, data = None):
        """Create child node (either above or below) given node with pt and data."""

        r = self.region.copy()
        if self.orient == VERTICAL:
            if below:
                r.x_max = self.point[X]
            else:
                r.x_min = self.point[X]
        else:
            if below:
                r.y_max = self.point[Y]
            else:
                r.y_min = self.point[Y]

        return KDNode(pt, 1-self.orient, data, r)

    def distance(self, pt):
        """Compute distance from self to pt."""
        if pt:
            return ((self.point[X] - pt[X])**2 + (self.point[Y] - pt[Y])**2) ** 0.5

    def isBelow(self, pt):
        """Is point below current node."""
        if self.orient == VERTICAL:
            return pt[X] < self.point[X]
        return pt[Y] < self.point[Y]

    def add(self, pt, data):
        """Add point to the KD Tree rooted at this node. Return True if updated structure."""

        if self.point == pt:
            return False

        if self.isBelow(pt):
            if self.below:
                return self.below.add(pt, data)
            else:
                self.below = self.createChild(pt, True, data)
        else:
            if self.above:
                return self.above.add(pt, data)
            else:
                self.above = self.createChild(pt, False, data)

        return True
    
    def range(self, region):
        """
        Yield (node,status) in KD Tree contained within region. When status is True, then all descendant
        nodes are part of the region, otherwise just the selected point.
        """
        if region.containsRegion(self.region):
            yield (self, True)
        else:
            if region.containsPoint(self.point):
                yield (self, False)
                
            if self.below:
                if (self.orient == VERTICAL and region.x_min <= self.point[X]) or    \
                   (self.orient == HORIZONTAL and region.y_min <= self.point[Y]):
                    for pair in self.below.range(region):
                        yield pair
            if self.above:
                if (self.orient == VERTICAL and self.point[X] <= region.x_max) or    \
                   (self.orient == HORIZONTAL and self.point[Y] <= region.y_max):
                    for pair in self.above.range(region):
                        yield pair
    
    def inorder(self):
        """In order traversal of tree rooted at given node that yields KDNode objects."""
        if self.below:
            for n in self.below.inorder():
                yield n

        yield self

        if self.above:
            for n in self.above.inorder():
                yield n

class KDTree:

    def __init__(self):
        """Create empty KD Tree."""
        self.root = None

    def add(self, pt, data = None):
        """Add Point to KD Tree."""

        if self.root:
            return self.root.add(pt, data)
        else:
            self.root = KDNode(pt, VERTICAL, data)
            return True

    def find(self, pt):
        """Find node in KD Tree with given point."""

        n = self.root
        while n:
            if n.point == pt:
                return n

            if n.isBelow(pt):
                n = n.below
            else:
                n = n.above
    
        return n

    def range(self, region):
        """Yield (node,status) in KD Tree contained within region."""
        if self.root is None:
            return None
    
        return self.root.range(region)

    def __iter__(self):
        """In order traversal of elements in the KD tree."""
        if self.root:
            for e in self.root.inorder():
                yield e

"""
Change Log
----------
2015.07.31    Added KDTree.find method for testing

"""
