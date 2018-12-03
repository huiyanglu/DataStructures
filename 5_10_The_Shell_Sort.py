def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print('After increments of size',sublistcount,'The list is',alist)

        sublistcount = sublistcount // 2
    return alist

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentValue = alist[i] #当前位置和数据
        position = i

        while position >= gap and alist[position-gap]>currentValue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentValue
    return alist

alist =  [54,26,93,17,77,31,44,55,20]
print(shellSort(alist))