"""
    Test cases for Stack

    Author: George Heineman
"""

import unittest

from stack import Stack
import random

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.st = Stack()
        
    def tearDown(self):
        self.st = None
        
    def test_basic(self):
        """Basic test."""
        self.assertTrue(self.st.isEmpty())
        self.st.push(99)
        self.assertFalse(self.st.isEmpty())
        self.assertEqual(99,self.st.pop())
        self.assertTrue(self.st.isEmpty())
        
    def test_stackBehavior(self):
        """Ensure behaves like a stack."""
        self.assertTrue(self.st.isEmpty())
        self.st.push(99)
        self.st.push(50)
        self.st.push(25)
        self.assertEqual(25,self.st.pop())
        self.assertEqual(50,self.st.pop())
        self.assertEqual(99,self.st.pop())
        self.assertTrue(self.st.isEmpty())
                
if __name__ == '__main__':
    unittest.main()
