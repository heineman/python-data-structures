"""
    Test cases for NaiveBuffer

    Author: George Heineman
"""

import unittest

from naiveBuffer import NaiveBuffer
import random

SIZE = 5

class TestNaiveBuffer(unittest.TestCase):
    
    def setUp(self):
        self.nb = NaiveBuffer(SIZE)
        
    def tearDown(self):
        self.nb = None
        
    def test_basic(self):
        """Basic test."""
        self.assertTrue(self.nb.isEmpty())
        self.assertFalse(self.nb.isFull())
        self.assertEqual(0, len(self.nb))

    def test_fill(self):
        """Fill up the buffer."""
        for _ in range(SIZE):
            self.nb.add(_)

        self.assertFalse(self.nb.isEmpty())
        self.assertTrue(self.nb.isFull())
        self.assertEqual(5, len(self.nb))

        
    def test_overFill(self):
        """Validate can deal with overfill."""
        high = 15
        for _ in range(high):
            self.nb.add(_)

        self.assertFalse(self.nb.isEmpty())
        self.assertTrue(self.nb.isFull())
        self.assertEqual(5, len(self.nb))

        # check all are still present
        for _ in range(high-1, high - SIZE-1, -1):
            self.assertTrue(_ in self.nb)

    def test_fillWithRemove(self):
        """Validate can deal with removals."""
        high = 15
        for _ in range(high):
            self.nb.add(_)
            self.nb.remove()

        self.assertTrue(self.nb.isEmpty())
        self.assertFalse(self.nb.isFull())
        self.assertEqual(0, len(self.nb))

    def test_randomUsage(self):
        """Try random behavior."""
        for _ in range(1000):
            if random.random() < 0.75:
                self.nb.add(random.random())
            elif not self.nb.isEmpty():
                self.nb.remove()
                
if __name__ == '__main__':
    unittest.main()
