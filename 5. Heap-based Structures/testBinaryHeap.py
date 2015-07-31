"""
    Test cases for BinaryHeap

    Author: George Heineman
"""
import unittest
from binaryHeap import BinaryHeap
import random

class TestBinaryHeap(unittest.TestCase):
    
    def setUp(self):
        # create BinaryHeap with initial 4 elements, and src is 2. Use
        # 999 for infinity
        self.bh = BinaryHeap(15,2,999)

    def tearDown(self):
        self.bh = None

    def test_basic(self):
        self.assertEqual(2, self.bh.pop())

    def test_decreaseKey(self):
        self.bh.decreaseKey(0, 19)
        self.bh.decreaseKey(1, 7)
        self.bh.decreaseKey(3,22)
        self.assertEqual(2, self.bh.pop())
        self.assertEqual(1, self.bh.pop())
        self.assertEqual(0, self.bh.pop())
        self.assertEqual(3, self.bh.pop())

    def test_decreaseKeyMany(self):
        self.bh = BinaryHeap(1000,0,999)
        for _ in range(999, 0, -1):
            self.bh.decreaseKey(_, _)

        for _ in range(1000):
            self.assertEqual(_, self.bh.pop())

    def test_multipleDecreaseKey(self):
        self.bh = BinaryHeap(50,0,999)
        for n in range(1, 50):
            for p in range(1, n):
                self.bh.decreaseKey(n, p)

        result = []
        for _ in range(50):
            result.append(self.bh.pop())
            
        self.assertEqual(list(range(50)), sorted(result))
                       
    def test_decreaseKeyRandom(self):
        self.bh = BinaryHeap(1000,0,999)
        for _ in range(999, 0, -1):
            self.bh.decreaseKey(_, random.randint(1,999))

        result = []
        for _ in range(1000):
            result.append(self.bh.pop())
        self.assertEqual(list(range(1000)), sorted(result))

                       
if __name__ == '__main__':
    unittest.main()
