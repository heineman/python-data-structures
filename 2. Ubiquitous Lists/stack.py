"""
    Stack using list as storage.

    Author: George Heineman
"""
class Stack:
    def __init__(self):
        """Demonstrate using list as storage for a Stack."""
        self.stack = []

    def isEmpty(self):
        """Determines whether stack is empty. O(1) performance"""
        return len(self.stack) == 0

    def push(self, v):
        """Push v onto the stack. O(1) performance."""
        self.stack.append(v)

    def pop(self):
        """Remove topmost element and return it. O(1) performance."""
        if self.isEmpty():
            raise Exception('Stack is empty.')
        return self.stack.pop()

    def __repr__(self):
        """show representation."""
        return "stack:" + str(self.stack)
