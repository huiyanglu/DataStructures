def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1) #左边
        quickSortHelper(alist,splitpoint+1,last) #右边

def findPivotValue(alist,first,last):
    firstNum = alist[first]
    lastNum = alist[last]
    middleNum = alist[(last-first)//2]
    lst = [firstNum,lastNum,middleNum]
    lst.pop(lst.index(min(lst)))
    lst.pop(lst.index(max(lst)))
    return lst[0]

def partition(alist,first,last):
    #pivotvalue = alist[first] #取第一个数为pivot value
    pivotvalue = findPivotValue(alist,first,last) #用median of three方法

    leftmark = first+1 #从第二个数开始
    rightmark = last #最后一个数

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark #返回split value

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)