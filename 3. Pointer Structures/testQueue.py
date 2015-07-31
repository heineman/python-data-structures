"""
    Test cases for Queue implemented by LinkedList

    Author: George Heineman
"""

import unittest

from queueLinkedList import QueueLinkedList
import random

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.queue = QueueLinkedList()
        
    def tearDown(self):
        self.queue = None
        
    def test_basic(self):
        """Basic test."""
        self.assertEqual(0, len(self.queue))
        self.assertTrue(self.queue.isEmpty())
        self.queue.append(99)
        self.assertEqual(1, len(self.queue))
        self.queue.append(30)
        self.assertEqual(99, self.queue.pop())
        self.assertEqual(30, self.queue.pop())

    def test_queue(self):
        """Three Elements."""
        self.assertEqual(0, len(self.queue))
        self.assertTrue(self.queue.isEmpty())
        self.queue.append(99)
        self.assertEqual(1, len(self.queue))
        self.queue.append(30)
        self.assertEqual(2, len(self.queue))
        self.assertEqual(99, self.queue.pop())
        self.assertEqual(1, len(self.queue))
        self.queue.append(15)
        self.assertEqual(2, len(self.queue))
        self.assertEqual(30, self.queue.pop())
        self.assertEqual(15, self.queue.pop())

    def test_iterators(self):
        """Iterators"""
        self.queue.append(99)
        self.assertEqual(1, len(self.queue))
        self.queue.append(30)
        self.assertTrue(30 in self.queue)
        self.assertFalse(15 in self.queue)
        

if __name__ == '__main__':
    unittest.main()
