def recMC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList:
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,change - i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

#print(recMC([1,5,10],20,[0]*21))

def dfMakeChange(coinValueList,change,minCoins):
    for cents in range(0,change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j]+1<coinCount: #如果比最小个数还要小
                coinCount = minCoins[cents-j]+1 # 加上一个j大小的硬币
        minCoins[cents] = coinCount #硬币个数统计
    return minCoins[change]

print(dfMakeChange([1,2,5,10],22,[0]*23))