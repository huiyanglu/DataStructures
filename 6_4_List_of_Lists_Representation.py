def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def buildTree(r):
    insertLeft(r,'b')
    insertRight(r,'c')

    insertLeft(getRightChild(r),'e')
    insertRight(getRightChild(r),'f')
    insertRight(getLeftChild(r),'d')
    return r

ttree = buildTree(BinaryTree('a'))
print(ttree)