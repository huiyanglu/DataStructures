from pythonds.basic.stack import Stack

def revstring(mystr):
    s = Stack()
    ss = ''
    for i in mystr:
        s.push(i)
    while not s.isEmpty():
        ss += s.pop()
    return ss

print(revstring('apple'))