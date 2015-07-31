"""
    Test cases for MovingAverage

    Author: George Heineman
"""

import unittest

from movingAverage import MovingAverage
import random

SIZE = 5

class TestMovingAverage(unittest.TestCase):
    
    def setUp(self):
        self.ma = MovingAverage(SIZE)
        
    def tearDown(self):
        self.ma = None
        
    def test_basic(self):
        """Basic test."""
        self.assertTrue(self.ma.isEmpty())
        self.assertFalse(self.ma.isFull())
        self.assertEqual(0, len(self.ma))
        self.assertEqual(0, self.ma.getAverage())

    def test_fill(self):
        """Fill up the buffer."""
        total = 0
        for _ in range(SIZE):
            total += _
            self.ma.add(_)

        self.assertFalse(self.ma.isEmpty())
        self.assertTrue(self.ma.isFull())
        self.assertEqual(5, len(self.ma))
        self.assertEqual(total/SIZE, self.ma.getAverage())

    def test_overFill(self):
        """Validate can deal with overfill."""
        high = 15
        for _ in range(high):
            self.ma.add(_)

        self.assertFalse(self.ma.isEmpty())
        self.assertTrue(self.ma.isFull())
        self.assertEqual(5, len(self.ma))

        # check all are still present
        total = 0
        for _ in range(high-1, high - SIZE-1, -1):
            total += _
            self.assertTrue(_ in self.ma)
        self.assertAlmostEqual(total/SIZE, self.ma.getAverage(), places=5)

    def test_fillWithRemove(self):
        """Validate can deal with removals."""
        high = 15
        for _ in range(high):
            self.ma.add(_)
            self.ma.remove()

        self.assertTrue(self.ma.isEmpty())
        self.assertFalse(self.ma.isFull())
        self.assertEqual(0, len(self.ma))
        self.assertEqual(0, self.ma.getAverage())


    def test_randomUsage(self):
        """Try random behavior."""
        for _ in range(1000):
            if random.random() < 0.75:
                self.ma.add(random.random())
            elif not self.ma.isEmpty():
                self.ma.remove()

            total = 0
            count = 0
            for _ in self.ma:
                total += _
                count += 1
            if count == 0:
                self.assertEqual(0, self.ma.getAverage())
            else:
                self.assertAlmostEqual(total/count, self.ma.getAverage(), places=5)
                

if __name__ == '__main__':
    unittest.main()
