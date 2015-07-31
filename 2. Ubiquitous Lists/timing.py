"""
    Demonstrate efficiency gains from Circular Buffer with same interface

    Author: George Heineman
"""
from circBuffer import CircularBuffer
from naiveBuffer import NaiveBuffer
import timeit

print ('N\tCircBuf  \tNaiveBuf')
trials = [2**k for k in range(10,15)]
for t in trials:
    mc = timeit.timeit(stmt='for _ in range(1000):\n\tcb.add(_)', setup='from circBuffer import CircularBuffer\ncb = CircularBuffer(' + str(t) + ')', number=1000)

    mb = timeit.timeit(stmt='for _ in range(1000):\n\tnb.add(_)', setup='from naiveBuffer import NaiveBuffer\nnb = NaiveBuffer(' + str(t) + ')', number=1000)
    print ('{0:d}\t{1:f}\t{2:f}'.format(t, mc, mb))

"""
Sample Output:

N	CircBuf  	NaiveBuf
1024	1.431026	1.213710
2048	1.420268	1.524364
4096	1.425255	2.155592
8192	1.429783	4.392674
16384	1.434091	7.873656
"""
