"""
    Highly specialized data structure. When constructing initially,
    assume you know the source vertex, src, and that all vertices
    in G must be drawn from the range 0..n-1 and src must also be
    from same range.

    add() should not be called externally, since one structure has been
    set up, all vertices are present and thus only decreaseKey should
    be called.

    Author: George Heineman
"""

class Element:
    def __init__(self, ident, priority):
        self.ident    = ident
        self.priority = priority

    def __repr__(self):
        return '[id=' + str(self.ident) + ', p=' + str(self.priority) + ']'

class BinaryHeap:
    def __init__(self, size, src, infinity):
        """
        Optimized construction of initial state of BinaryHeap
        Assuming src is the source vertex, using infinity as
        maximum value. Note self.ar[0] is Element with zero priority
        """
        self.ar  = [None] * size
        self.pos = [None] * size
        for ident in range(size):
            self.ar[ident]  = Element(ident, infinity)
            self.pos[ident] = ident
        self.n = size

        # swap src with first one so it is root of heap
        self.pos[0],self.pos[src] = self.pos[src],self.pos[0]

        # root of heap has distance zero (aka, priority)
        self.ar[src] = self.ar[0]
        self.ar[0] = Element(src, 0)
        
    def isEmpty(self):
        """Determine if heap is empty."""
        return self.n == 0

    def __len__(self):
        """Return size of heap."""
        return self.n

    def pop(self):
        """Return smallest value and repair heap."""
        if self.n == 0:
            raise ValueError("Heap is empty.")
        val = self.ar[0].ident
        self.pos[val] = None
        
        self.n -= 1
        last = self.ar[self.n]
        
        self.ar[0] = last
        pIdx = 0
        child = pIdx*2+1
        while child < self.n:
            # select smaller of two children
            sm = self.ar[child]
            if child < self.n:
                if sm.priority > self.ar[child+1].priority:
                    child += 1
                    sm = self.ar[child]

            # are we in right spot?
            if last.priority <= sm.priority:
                break

            # swap and move up
            self.ar[pIdx] = sm
            self.pos[sm.ident] = pIdx

            pIdx = child
            child = 2*pIdx+1

        # insert into spot vacated by moved element or last one
        self.ar[pIdx] = last
        self.pos[last.ident] = pIdx
        return val

    def add(self, ident, priority):
        """Add entry with integer ident (0 < ident < self.n) and priority."""
        i = self.n
        self.n += 1
        
        # Correct structure to root
        while i > 0:
            pIdx  = (i-1) // 2
            p     = self.ar[pIdx]
            if priority > p.priority:
                break
            
            self.ar[i] = p
            self.pos[p.ident] = i
            i = pIdx

        self.ar[i]= Element(ident, priority)
        self.pos[ident] = i

    def decreaseKey(self, ident, newPriority):
        """
        Caller must ensure priority is indeed smaller than existing.
        """
        size = self.n

        self.n = self.pos[ident]
        self.add(ident, newPriority)
        
        self.n = size
    
        
    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str,self.ar[:self.n])) + '], ' + str(self.pos)

"""
Change Log:
-----------
2015.07.31      Clarified documentation to not call add() externally
"""
