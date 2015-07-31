"""
    Demonstration of Prefix Tree of all lowercase words using
    dict objects for storage.

    Author: George Heineman
"""

# anything other than 'a' .. 'z'
WordKey = '\n'

def traverse(d, prefix):
    """Recursively generate all words in the Prefix Tree."""
    for k in d:
        if k == WordKey:
            yield prefix
        else:
            for _ in traverse(d[k], prefix + k):
                yield _
    
class PrefixTree:
    def __init__(self, *start):
        """Demonstrate prefix tree in Python give strings."""
        self.head  = {}
        self.count = 0
        self.numDictionaries = 1
        for _ in start:
            self.add(_.lower())

    def add(self, value):
        """Add value to prefix tree."""
        d = self.head
        while len(value) > 0:
            if value[0] not in d:
                d[value[0]] = {}
                self.numDictionaries += 1

            d = d[value[0]]
            value = value[1:]

        if WordKey in d:
            return False
        d[WordKey] = True
        self.count += 1
        return True

    def remove(self, value):
        """Remove value from prefix tree."""
        d = self.head
        while len(value) > 0:
            if value[0] not in d:
                return False

            d = d[value[0]]
            value = value[1:]

        if WordKey not in d:
            return False
        del d[WordKey]
        self.count -= 1
        return True

    def __contains__(self, value):
        """Determine if value is contained in the prefix tree."""
        d = self.head
        while len(value) > 0:
            if value[0] not in d:
                return False

            d = d[value[0]]
            value = value[1:]

        return WordKey in d
    
    def __iter__(self):
        """Iterate over all values."""
        for _ in traverse(self.head, ''):
            yield _

    def __repr__(self):
        """Representation of prefix tree."""
        return 'prefix: {0:d} entries in {1:d} dicts'.format(
           self.count, self.numDictionaries)

    def __len__(self):
        """Count values in tree."""
        return self.count
                                                             
"""
Change Log
----------
2015.07.30     Added __len__ method to PrefixTree
"""
