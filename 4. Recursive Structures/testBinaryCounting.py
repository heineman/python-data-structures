"""
    Test binary Counting with random trees.

    Author: George Heineman
"""
import unittest

from projectBinaryCounting import CountingBinaryTree
import random

def inorder(self):
    """In order traversal generator of tree rooted at given node."""
    if self.left:
        for v in inorder(self.left):
            yield v

    yield self

    if self.right:
        for v in inorder(self.right):
            yield v

class TestCounting(unittest.TestCase):
    
    def setUp(self):
        self.bst = CountingBinaryTree()
        
    def tearDown(self):
        self.bst = None

    def test_allLeft(self):
        for _ in range(100,0,-1):
            self.bst.add(_)

        while len(list(iter(self.bst))) > 0:
            for n in inorder(self.bst.root):
                self.assertEqual (n.numLeft, n.countLeftChildren())
            self.bst.remove(self.bst.root.value)
        
    def test_allRight(self):
        for _ in range(2):
            self.bst.add(_)

        while len(list(iter(self.bst))) > 0:
            for n in inorder(self.bst.root):
                self.assertEqual (n.numLeft, n.countLeftChildren())
            self.bst.remove(self.bst.root.value)
        
    def test_trial(self):
        """Try trial 50 times to be sure."""
        for trial in range(50):
            self.bst = CountingBinaryTree()
            num = 100
            values = list(range(num))
            random.shuffle(values)
            for _ in values:
                self.bst.add(_)

            for n in inorder(self.bst.root):
                self.assertEqual (n.numLeft, n.countLeftChildren())

            removal = list(values)
            random.shuffle(removal)
            for t in removal:
                self.bst.remove(t)
                self.assertFalse(t in self.bst)
                if self.bst.root:
                    for n in inorder(self.bst.root):
                        self.assertEqual (n.numLeft, n.countLeftChildren())

                       
if __name__ == '__main__':
    unittest.main()

