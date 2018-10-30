# Self check
# find the minimum number in a list
# The first function should compare each number to every other number on the list O(n2).
# The second function should be linear O(n)

import time
from random import randrange

def findMinOn(alist): # 复杂度O(n)
    overallmin = alist[0]
    for i in range(0,len(alist)):
        if alist[i]<overallmin:
            overallmin = alist[i]
            i+=1
    return overallmin

def findMinOn2(alist): # 复杂度O(n^2)
    overallmin2 = alist[0]
    for i in alist:
        issmallest2 = True
        for j in alist:
            if i>j:
                issmallest2 = False
        if issmallest2:
            overallmin2 = i
    return overallmin2

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start1 = time.time()
    print(findMinOn(alist)) #复杂度O(n)
    end1 = time.time()
    print('Size: %d time of O(n): %f' %(listSize,end1-start1))

    start2 = time.time()
    print(findMinOn2(alist))  # 复杂度O(n)
    end2 = time.time()
    print('Size: %d time of O(n^2): %f' % (listSize, end2 - start2))

