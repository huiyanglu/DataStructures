def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

def listsum_rec(numList): # recursion
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum_rec([1,3,5,7,9]))


