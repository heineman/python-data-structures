"""
    Implementation of a moving average by extending CircularBuffer.

    Author: George Heineman
"""
from circBuffer import CircularBuffer

class MovingAverage(CircularBuffer):
    
    def __init__(self, size):
        """Store buffer in given storage."""
        CircularBuffer.__init__(self, size)
        self.total = 0

    def getAverage(self):
        """Returns moving average (zero if no elements)."""
        if self.count == 0:
            return 0
        return self.total/self.count
    
    def remove(self):
        """Removes oldest value from non-empty buffer."""
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed

    def add(self, value):
        """Adds value to buffer, overwrite as needed."""
        if self.isFull():
            self.total -= self.buffer[self.low]
        
        self.total += value
        CircularBuffer.add(self,value)

    def __repr__(self):
        """String representation of moving average."""
        if self.isEmpty():
            return 'ma:[]'

        return 'ma:[' + ','.join(map(str,self)) + ']:' + str(self.getAverage())

"""
Change Log
----------
2015.07.30     simplified add() function by eliminating delta
"""
