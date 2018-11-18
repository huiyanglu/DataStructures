class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): #checks to see if the head of the list is a reference to None
        return self.head == None # will only be true if there are no nodes in the linked list.

    def add(self,item): #在开头加
        temp = Node(item) #creates a new node and places the item as its data.
        temp.setNext(self.head) #changes the next reference of the new node to refer to the old first node of the list.
        #Now that the rest of the list has been properly attached to the new node
        self.head = temp #modify the head of the list to refer to the new node.

    def size(self): #traversal
        current = self.head #initialized to the head of the list
        count = 0
        while current!=None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head #the traversal is initialized to start at the head of the list
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current #previous先动，current后动
                current = current.getNext()
                # This process is often referred to as
                # “inch-worming” as previous must catch up to
                # current before current moves ahead.
        if previous == None: #如果要删掉开头第一个数
            self.head = current.getNext() #直接连到下一个数
        else: #如果不是第一个数 则正常操作删除
            previous.setNext(current.getNext())

    def append(self,item): # O(n) 尝试改成O(1)
        temp = Node(item)
        current = self.head
        if self.isEmpty():
            self.head = temp
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)

mylist = UnorderedList()

mylist.append(55)
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)



print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
