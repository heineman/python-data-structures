"""
    Demonstrate O(n) behavior of simple for loop.

    Author: George Heineman
"""
import random
import timeit

print ('N\tSum Time')
for trial in [2**_ for _ in range(1,9)]:
    numbers = [random.randint(1,9) for _ in range(trial)]
    m = timeit.timeit(stmt='sum = 0\nfor d in numbers:\n\tsum = sum + d',
                  setup='import random\nnumbers = ' + str(numbers))
    print ('{0:d}\t{1:f}'.format(trial, m))


"""
Sample Output:

N	Sum Time
2	0.266628
4	0.386807
8	0.647032
16	1.156006
32	2.163258
64	4.586453
128	9.979934
256	20.174862
"""
