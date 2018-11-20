from pythonds.basic.stack import Stack

def toStr(num,base):
    lst = Stack()
    convertString = "0123456789ABCDEF"
    rst = []
    while num > 0:
        if num < base:
            lst.push(convertString[num])
        else:
            lst.push(convertString[num % base])
        num = num // base
    while not lst.isEmpty():
        rst.append(lst.pop())
    return ''.join(rst)

print(toStr(1453,16))