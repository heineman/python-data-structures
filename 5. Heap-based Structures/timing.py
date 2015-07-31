"""
    Demonstrate efficiency gains from heapq over our Heap implementation

    Author: George Heineman
"""
from heap import Heap
import heapq
import timeit
import random

def launch(t):
    """Create random list."""
    mylist = list(range(0,t))
    random.seed(1)
    random.shuffle(mylist)
    return mylist


def timingPq(pq, t):
    """Pop twice and push random one until empty."""
    while len(pq) > 0:
        heapq.heappop(pq)
        if len(pq) == 0:
            return
        heapq.heappop(pq)
        rnd = random.randint(1,t)
        heapq.heappush(pq, rnd)

def timingHeap(heap, t):
    """Pop twice and push random one until empty."""
    while len(heap) > 0:
        heap.pop()
        if len(heap) == 0:
            return
        heap.pop()
        rnd = random.randint(1,t)
        heap.add(rnd)
        

print ('N\tHeap\theapq\tHeap-c\theapq-c')
trials = [2**k for k in range(7,12)]
for t in trials:
    mpqb = min(timeit.Timer('import heapq\npq=[]\nfor _ in val:\n\theapq.heappush(pq, _)',
       setup='from __main__ import launch\nval = launch(' + str(t) + ')').repeat(5,1000))

    mheapb = min(timeit.Timer('from heap import Heap\nheap=Heap()\nfor _ in val:\n\theap.add(_)',
       setup='from __main__ import launch\nval = launch(' + str(t) + ')').repeat(5,1000))
    
    mpq = min(timeit.Timer(stmt='from __main__ import timingPq\ntimingPq(val,' + str(t) + ')',
       setup='from __main__ import launch\nval = launch(' + str(t) + ')').repeat(5,1000))
    
    mheap = min(timeit.Timer(stmt='from __main__ import timingHeap\ntimingHeap(heap,' + str(t) + ')',
       setup='from __main__ import launch\nfrom heap import Heap\nheap = Heap(launch(' + str(t) + '))').repeat(5,1000))    
    print ('{0:d}\t{1:.4f}\t{2:.4f}\t{3:.4f}\t{4:.4f}'.format(t, mheap, mpq, mheapb, mpqb))


"""
Sample Output:

N	Heap	heapq	Heap-c	heapq-c
128	0.0064	0.0031	0.3363	0.0334
256	0.0108	0.0036	0.6992	0.0656
512	0.0208	0.0049	1.3887	0.1311
1024	0.0438	0.0072	2.8255	0.2578
2048	0.0891	0.0121	5.7107	0.5161
4096	0.1900	0.0219	11.2772	1.0171
"""
