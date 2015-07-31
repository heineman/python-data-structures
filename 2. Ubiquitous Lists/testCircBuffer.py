"""
    Test cases for CircularBuffer

    Author: George Heineman
"""

import unittest

from circBuffer import CircularBuffer
import random

SIZE = 5

class TestCircBuffer(unittest.TestCase):
    
    def setUp(self):
        self.cb = CircularBuffer(SIZE)
        
    def tearDown(self):
        self.cb = None
        
    def test_basic(self):
        """Basic test."""
        self.assertTrue(self.cb.isEmpty())
        self.assertFalse(self.cb.isFull())
        self.assertEqual(0, len(self.cb))

    def test_fill(self):
        """Fill up the buffer."""
        for _ in range(SIZE):
            self.cb.add(_)

        self.assertFalse(self.cb.isEmpty())
        self.assertTrue(self.cb.isFull())
        self.assertEqual(5, len(self.cb))

        
    def test_overFill(self):
        """Validate can deal with overfill."""
        high = 15
        for _ in range(high):
            self.cb.add(_)

        self.assertFalse(self.cb.isEmpty())
        self.assertTrue(self.cb.isFull())
        self.assertEqual(5, len(self.cb))

        # check all are still present
        for _ in range(high-1, high - SIZE-1, -1):
            self.assertTrue(_ in self.cb)

    def test_fillWithRemove(self):
        """Validate can deal with removals."""
        high = 15
        for _ in range(high):
            self.cb.add(_)
            self.cb.remove()

        self.assertTrue(self.cb.isEmpty())
        self.assertFalse(self.cb.isFull())
        self.assertEqual(0, len(self.cb))

    def test_randomUsage(self):
        """Try random behavior."""
        for _ in range(1000):
            if random.random() < 0.75:
                self.cb.add(random.random())
            elif not self.cb.isEmpty():
                self.cb.remove()
                
if __name__ == '__main__':
    unittest.main()
