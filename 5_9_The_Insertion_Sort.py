def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index] #当前数值
        position = index #当前索引

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentValue
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))