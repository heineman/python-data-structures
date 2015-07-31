"""
    Show recursive solution for sum of values in Linked List.

    This was example from module 4. Recursive Structures

    Author: George Heineman
"""
from linkedList import LinkedList

def sumList(n):
  # Base case
  if n is None:
    return 0

  # Action and Recursive Step
  return n.value + sumList(n.next)

if __name__ == '__main__':
    myList = LinkedList()
    myList.prepend(11)
    myList.prepend(10)
    myList.prepend(8)

    print ("Sum (", sumList(myList.head), ") should be 29.")
