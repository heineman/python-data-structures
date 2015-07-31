"""
    Test cases for both PrefixTree implementations

    Author: George Heineman
"""

import unittest

from prefixTreeDict import PrefixTree
from prefixTreeLinkedList import PrefixTreeLinkedList

import random

letters = 'abcdefghijklmnopqrstuvwxyz'
def randomString(k):
    """Generate Random String."""
    word = ''
    for _ in range(k):
        word += letters[random.randint(0,k-1)]
    return word

class TestPrefixTrees(unittest.TestCase):
    
    def setUp(self):
        self.treeD = PrefixTree()
        self.treeLL = PrefixTreeLinkedList()
        
    def tearDown(self):
        self.treeD = None
        self.treeLL = None
        
    def test_basic(self):
        """Basic test."""
        words = [randomString(6) for _ in range(999)]

        # make sure unique, just in case...
        uniq = []
        for _ in words:
            if _ not in self.treeD:
                uniq.append(_)
            self.treeD.add(_)
            self.treeLL.add(_)

        for _ in uniq:
            self.assertTrue(_ in self.treeD)
            self.assertTrue(_ in self.treeLL)

        random.shuffle(uniq)
        for _ in uniq:
            self.assertTrue(self.treeD.remove(_))
            self.assertTrue(self.treeLL.remove(_))

        self.assertEqual(0, len(self.treeD))
        self.assertEqual(0, len(self.treeLL))

if __name__ == '__main__':
    unittest.main()
