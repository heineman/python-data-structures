"""
    Test cases for AVL Implementation of Binary Tree.

    Author: George Heineman
"""
import unittest

from avl import BinaryTree
import random

class TestAVL(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinaryTree()
        
    def tearDown(self):
        self.bst = None
        
    def test_minTrial(self):
        num = 1000
        values = list(range(num))
        random.shuffle(values)
        
        for _ in values:
            self.bst.add(_)

        # always remove MIN for maximum rotations
        for _ in range(num):
            t = min(self.bst)
            self.bst.remove(t)
            self.assertFalse(t in self.bst)
            self.assertTrue(self.bst.assertAVLProperty())

    def test_maxTrial(self):
        num = 1000
        values = list(range(num))
        random.shuffle(values)
        
        for _ in values:
            self.bst.add(_)

        # always remove Max for maximum rotations
        for _ in range(num):
            t = max(self.bst)
            self.bst.remove(t)
            self.assertFalse(t in self.bst)
            self.assertTrue(self.bst.assertAVLProperty())

if __name__ == '__main__':
    unittest.main()
