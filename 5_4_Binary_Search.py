def binarySearch(alist,item):
    first = 0 #索引
    last = len(alist)-1 #索引
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint + 1
    return found

def binarySearch_rec(alist,item): # binary search with recursion
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch_rec(alist[:midpoint],item)
            else:
                return binarySearch_rec(alist[midpoint+1:],item)

testlist = [0,1,4,8,13,17,19,32]
print(binarySearch_rec(testlist,4))
