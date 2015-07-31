"""
    Test cases for LinkedList data structure

    Author: George Heineman
"""

import unittest

from linkedList import LinkedList, LinkedNode
import random

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.link = LinkedList()
        
    def tearDown(self):
        self.link = None
        
    def test_basic(self):
        """Basic test."""
        self.assertEqual(0, len(self.link))
        self.link.prepend(99)
        self.assertEqual(1, len(self.link))
        self.link.prepend(30)
        self.assertEqual(30, self.link.pop())
        self.assertEqual(99, self.link.pop())

    def test_stack(self):
        """Basic test."""
        self.assertEqual(0, len(self.link))
        self.link.prepend(99)
        self.assertEqual(1, len(self.link))
        self.link.prepend(30)
        self.assertFalse(self.link.remove(19))
        self.assertTrue(self.link.remove(30))
        self.assertEqual(1, len(self.link))
        self.assertFalse(self.link.remove(30))
        self.assertEqual(1, len(self.link))
        self.assertTrue(self.link.remove(99))
        self.assertEqual(0, len(self.link))

    def test_iterators(self):
        """Iterators"""
        self.link.prepend(99)
        self.assertEqual(1, len(self.link))
        self.link.prepend(30)
        self.assertTrue(30 in self.link)
        self.assertFalse(15 in self.link)

    def test_infinite(self):
        """Test infinite check."""
        node0 = LinkedNode(0)
        node1 = LinkedNode(10)
        node2 = LinkedNode(20)
        node3 = LinkedNode(30)

        node1.next = node2
        node2.next = node3

        self.assertFalse(node1.checkInfinite())
        
        node3.next = node2    # WARNING CYCLE
        self.assertTrue(node1.checkInfinite())

        node0.next = node1
        self.assertTrue(node0.checkInfinite())
                
if __name__ == '__main__':
    unittest.main()
