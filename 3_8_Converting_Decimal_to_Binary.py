from pythonds.basic.stack import Stack

def divideBy2(decNumber,base):
    digits = "0123456789ABCDEF"
    rem = Stack()
    while decNumber > 0: #while判断何时退出循环
        each = decNumber % base
        rem.push(each)
        decNumber = decNumber//base

    rst = ''
    while not rem.isEmpty():
        rst = rst + digits[rem.pop()]
    return rst
