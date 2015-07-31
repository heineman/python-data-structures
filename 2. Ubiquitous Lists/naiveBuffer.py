"""
    Implementation of a naive buffer of limited storage size.

    Author: George Heineman
"""
class NaiveBuffer:
    
    def __init__(self, size):
        """Store buffer in given storage."""
        self.buffer = []
        self.size = size

    def __len__(self):
        """Return number of elements"""
        return len(self.buffer)

    def isEmpty(self):
        """Determines if buffer is empty."""
        return len(self.buffer) == 0

    def isFull(self):
        """Determines if buffer is full."""
        return len(self.buffer) == self.size
        
    def count(self):
        """Returns number of elements in buffer."""
        return len(self.buffer)
        
    def add(self, value):
        """Adds value to non-full buffer."""
        if len(self.buffer) == self.size:
            del self.buffer[0]
        self.buffer.append(value)
    
    def remove(self):
        """Removes oldest value from non-empty buffer."""
        value = self.buffer[0]
        del self.buffer[0]
        return value
    
    def __iter__(self):
        """Return elements in the circular buffer in order using iterator."""
        for _ in self.buffer:
            yield _

    def __repr__(self):
        """String representation of circular buffer."""
        return str(self.buffer)
        
