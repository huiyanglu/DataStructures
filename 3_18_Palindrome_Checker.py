from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size()>1 and stillEqual: #如果只剩最中间的数，size=1，则循环退出
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first!=last:
            stillEqual = False

    return stillEqual

print(palchecker('abcba'))