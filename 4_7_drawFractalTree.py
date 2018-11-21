import turtle
import random

def tree(branchLen,t):
    deg = random.randint(15,45) # the angle is selected at random in some range
    sub = random.randint(5,15) # subtract a random amount in some range
    if branchLen > 5:
        if branchLen < 20:
            t.color('green')
            t.pensize(2)
        else:
            t.color('brown')
        t.forward(branchLen)
        t.right(deg)
        tree(branchLen-sub,t)
        t.left(deg*2)
        tree(branchLen-sub,t)
        if branchLen < 20:
            t.color('green')
            t.pensize(2)
        else:
            t.color('brown')
        t.right(deg)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    t.pensize(3)
    tree(75,t)
    myWin.exitonclick()

main()