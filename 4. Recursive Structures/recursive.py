"""
    Exploring recursion.

    Author: George Heineman
"""

def search(aList, target):
    for _ in aList:
        if target == _:
            return True
    return False

def searchRecursive(aList, target):
    if len(aList) == 0:
        return False

    if aList[0] == target:
        return True
    else:
        return searchRecursive(aList[1:], target)

