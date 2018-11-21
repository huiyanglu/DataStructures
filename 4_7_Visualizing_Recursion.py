import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle,lineLen): #画一个螺旋
    if lineLen > 0:
        myTurtle.forward(lineLen) # 直行lineLen长度
        myTurtle.right(60) # 方向向右转的角度
        drawSpiral(myTurtle,lineLen-5) #调用函数，长度减小5

print(drawSpiral(myTurtle,100))
myWin.exitonclick() #程序运行结束screen不会消失，停留在最后状态