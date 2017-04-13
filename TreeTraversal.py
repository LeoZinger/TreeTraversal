#TreeTraversal
#import Queue
#q = Queue.Queue()
#for i in range(5):
#    q.put(i)

class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def InOrderTraverse(node):
        if (node):
            InOrderTraverse(node.left)
            print(node.value)
            InOrderTraverse(node.right)

def PreOrderTraverse(node):
    if (node):
        print(node.value)
        InOrderTraverse(node.left)
        InOrderTraverse(node.right)


def PostOrderTraverse(node):
    if (node):
        InOrderTraverse(node.left)
        InOrderTraverse(node.right)
        print(node.value)

myTree = Node(5)
myTree.left = Node(3)
myTree.right = Node(7)
myTree.left.left = Node(2)
myTree.left.left.left = Node(1)
myTree.left.right = Node(4)
myTree.right.left = Node(6)
myTree.right.right = Node(8)

print("Running InOrderTraverse:")
InOrderTraverse(myTree)

print("Running PreOrderTraverse:")
PreOrderTraverse(myTree)

print("Running PostOrderTraverse:")
PostOrderTraverse(myTree)
