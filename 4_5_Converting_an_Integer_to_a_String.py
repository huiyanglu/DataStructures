def toString(num,base):
    convString = '0123456789ABCDEF'
    if num < base:
        return convString[num]
    else:
        return toString(num//base,base)+convString[num % base]

"""
Write a function that takes a string as a parameter 
and returns a new string that is the reverse of the old string.

"""
from pythonds.basic.stack import Stack

def reverse(strng):
    lst = Stack()
    rst = []
    i = 0
    while lst.size() < len(strng):
        lst.push(strng[i])
        i+=1
    while len(rst) < len(strng):
        rst.append(lst.pop())
    return ''.join(rst)

"""
1.takes a string as a parameter and returns True 
 if the string is a palindrome, False otherwise.
2.remove the spaces and punctuation before checking
3.madam i’m adam is a palindrome.
4.test

testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)

"""
import re

def removeWhite(strng):
    return ''.join(re.findall(r'[A-Za-z]', strng))

def isPal(strng):
    strng_lower = removeWhite(strng).lower()
    l = len(strng_lower)
    for i in range(0,l//2):
        if strng_lower[i]!=strng_lower[l-i-1]:
            return False
        else:
            i+=1
    return True

print(isPal('Ablet  Elba'))
print(reverse('hello'))
print(toString(117,10))