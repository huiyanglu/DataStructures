from pythonds.basic.queue import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None #目前是否有任务
        self.timeRemaining = 0 #剩余打印时间

    def tick(self):
        if self.currentTask != None: #如果当前有任务
            self.timeRemaining = self.timeRemaining - 1 #时间-1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None: #有任务 busy是True
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue() #打印任务队列
    waitingtimes = [] #等待时间列表

    for currentSecond in range(numSeconds):

      if newPrintTask():#如果==180
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()): #打印机不忙且队列不为空
        nexttask = printQueue.dequeue() #下一个任务从队列中移除
        waitingtimes.append(nexttask.waitTime(currentSecond)) #nexttask完成需要的时间
        labprinter.startNext(nexttask) #打印机开始工作

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes) #求平均时间
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
