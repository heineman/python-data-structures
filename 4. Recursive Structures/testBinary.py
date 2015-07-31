"""
    Test cases for Binary Tree that allows duplicates

    Author: George Heineman
"""
import unittest

from binary import BinaryTree
import random


class TestBinaryWithDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinaryTree()
        
    def tearDown(self):
        self.bst = None

    def test_duplicate(self):
        self.bst.add(88)
        self.bst.add(88)
        self.assertTrue(88 in self.bst)
        self.bst.remove(88)
        self.assertTrue(88 in self.bst)
        self.bst.remove(88)
        self.assertFalse(88 in self.bst)

    def test_range(self):
        match = [1,5,2,6,3,7,9,8]
        for _ in match:
            self.bst.add(_)

        self.assertEqual(1, self.bst.getMin())
        self.assertEqual(9, self.bst.getMax())

    def test_iter(self):
        match = [1,5,2,6,3,7,9,8]
        for _ in match:
            self.bst.add(_)

        compare = list(iter(self.bst))
        self.assertEqual(sorted(match), compare)
        
    def test_trial(self):
        num = 1000
        values = list(range(num))
        random.shuffle(values)
        for _ in values:
            self.bst.add(_)

        for _ in range(num):
            t = min(self.bst)
            self.bst.remove(t)
            self.assertFalse(t in self.bst)

                       
if __name__ == '__main__':
    unittest.main()
