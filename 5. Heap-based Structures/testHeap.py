"""
    Test cases for Heap

    Author: George Heineman
"""
import unittest

from heap import Heap
import random

class TestHeap(unittest.TestCase):
    
    def setUp(self):
        self.heap = Heap()
        
    def tearDown(self):
        self.heap = None

    def test_basic(self):
        self.assertTrue(self.heap.isEmpty())
        self.assertEqual(0, len(self.heap))

    def test_start(self):
        values = list(range(10,0,-1))
        self.heap = Heap(values)
        
        result = []
        while not self.heap.isEmpty():
            result.append(self.heap.pop())

        self.assertEqual(list(range(1,11)), result)

    def test_small(self):
        values = [9, 1, 8, 7, 2, 3, 6, 4, 5]
        for _ in values:
            self.heap.add(_)

        result = []
        while not self.heap.isEmpty():
            result.append(self.heap.pop())

        self.assertEqual(sorted(values), result)

                       
if __name__ == '__main__':
    unittest.main()
