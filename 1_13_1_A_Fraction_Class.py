# write some methods to implement *, /, and - .
# Also implement comparison operators > and <

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    #__init__方法是类实例创建之后调用
    # 对当前对象的实例的一些初始化, 没有返回值
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    # convert an object into a string
    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    # show() will allow the Fraction object to print itself as a string.
    def show(self):
        print(self.num,'/',self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __sub__(self,otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    # 小于
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    # 大于
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

x = Fraction(1,2)
y = Fraction(2,5)
print(x<y)