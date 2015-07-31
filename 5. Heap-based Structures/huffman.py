"""
    Huffman code for collection of strings.
    Uses heapq for structure

    Author: George Heineman
"""
import heapq

class Node:
    def __init__(self, prob, symbol = None):
        """Create node for given symbol and probability."""
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob

    # Need comparator method at a minimum to work with heapq
    def __lt__(self, other):
        return self.prob < other.prob
    
    def encode(self, encoding):
        """Return bit encoding in traversal."""
        if self.left is None and self.right is None:
            yield (self.symbol, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v

class Huffman:
    def __init__(self, initial):
        """Construct encoding given initial corpus."""
        self.initial = initial
        
        # Count frequencies
        freq = {}
        for _ in initial:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1

        # Construct priority queue
        pq = []
        for symbol in freq:
            pq.append(Node(freq[symbol], symbol))
        heapq.heapify(pq)

        # special case: what if only one symbol?
        if len(pq) == 1:
            self.root = Node(1)
            self.root.left = pq[0]
            self.encoding = {symbol: '0'}
            return

        # Huffman Encoding Algorithm
        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            n3 = Node(n1.prob + n2.prob)
            n3.left = n1
            n3.right = n2
            heapq.heappush(pq, n3)

        # Record
        self.root = pq[0]
        self.encoding = {}
        for sym,code in pq[0].encode(''):
            self.encoding[sym]=code

    def __repr__(self):
        """Show encoding"""
        return 'huffman:' + str(self.encoding)

    def encode(self, s):
        """Return bit string for encoding."""
        bits = ''
        for _ in s:
            if not _ in self.encoding:
                raise ValueError("'" + _ + "' is not encoded character")
            bits += self.encoding[_]
        return bits

    def decode(self, bits):
        """Decode ASCII bit string for simplicity."""
        node = self.root
        s = ''
        for _ in bits:
            if _ == '0':
                node = node.left
            else:
                node = node.right

            if node.symbol:
                s += node.symbol
                node = self.root

        return s

"""
Change Log:
-----------
2015.07.31      Fixed init() method in Huffman class to handle special
                case when all letters in initial string are the same.

"""
