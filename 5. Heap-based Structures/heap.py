"""
    Show how to implement Heap
"""

class Heap:
    def __init__(self, values = None):
        """Construct list from values"""
        if values is None:
            self.ar = []
        else:
            self.ar = list(values)
        self.n = len(self.ar)
        
        start = self.n//2 - 1
        for i in range(start, -1, -1):
            self.heapify (i)

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
        val = self.ar[0]
        self.n -= 1
        self.ar[0] = self.ar[self.n]
        self.heapify(0)
        return val

    def add(self, value):
        """Add value to heap and repair heap."""
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1
        
        # Correct structure to root
        while i > 0:
            parent = (i-1) // 2
            if self.ar[i] < self.ar[parent]:
                self.ar[i],self.ar[parent] = self.ar[parent],self.ar[i]
                i = parent
            else:
                break
        
    def heapify(self, i):
        """Heapify sub-array [i, end)."""
        left = 2*i+1
        right = 2*i+2

        # Find smallest element of A[i], A[left], and A[right]
        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i

        if right < self.n and self.ar[right] < self.ar[smallest]:
            smallest = right

        # If smallest is not already the parent then swap and propagate
        if smallest != i:
            self.ar[i],self.ar[smallest] = self.ar[smallest],self.ar[i]
            self.heapify (smallest)

    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str,self.ar[:self.n])) + ']'
