"""
    Demonstration of Linked Lists in Python.

    Author: George Heineman
"""
class LinkedNode:
    def __init__(self, value, tail = None):
        """Node in a Linked List."""
        self.value = value
        self.next  = tail

    def checkInfinite(self):
        """Check whether infinite loop via next."""
        p1 = p2 = self
        while p1 != None and p2 != None:
            if p2.next == None: return False

            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2: return True
        return False

class LinkedList:
    def __init__(self, *start):
        """Demonstrate linked lists in Python."""
        self.head  = None
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Prepend element into list."""
        self.head = LinkedNode(value, self.head)

    def pop(self):
        """Remove first value in list."""
        if self.head is None:
            raise Exception ("Linked list is empty.")
        val = self.head.value
        self.head = self.head.next
        return val

    def remove(self, value):
        """Remove value from list."""
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last == None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            n = n.next
        return False
        
    def __iter__(self):
        """Iterator of values in the list."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of linked list."""
        if self.head is None:
            return 'link:[]'

        return 'link:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        """Count values in list."""
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count

