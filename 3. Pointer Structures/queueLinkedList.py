"""
    Demonstration of Queue using Linked Lists.

    Author: George Heineman
"""
from linkedList import LinkedNode

class QueueLinkedList:
    def __init__(self, *start):
        """Demonstrate queue using linked list in Python."""
        self.head = None
        self.tail = None
        for _ in start:
            self.add(_)

    def append(self, value):
        """Add value to end of queue."""
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def isEmpty(self):
        """Determine if queue is empty."""
        return self.head == None

    def pop(self):
        """Remove first value from queue."""
        if self.head is None:
            raise Exception ("Queue is empty.")
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def __iter__(self):
        """Iterator of values in queue."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of queue."""
        if self.head is None:
            return 'queue:[]'

        return 'queue:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        """Count values in queue."""
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count

