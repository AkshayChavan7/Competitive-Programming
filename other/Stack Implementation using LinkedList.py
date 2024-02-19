class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class MyStack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, n):
        newNode = Node(data=n)
        if self.top == None:
            self.top = newNode
        else:
            self.top.next = newNode
            newNode.prev = self.top
            self.top = self.top.next
        self.size+=1
    
    def pop(self):
        if self.size == 1:
            del self.top
            self.top = Node()
            self.top.prev = None
            self.top.next = None
            self.size-=1
        elif self.size > 1:
            self.top = self.top.prev
            del self.top.next
            self.top.next = None
            self.size-=1
        else:
            print("Stack is empty!")
    
    def getTop(self):
        if self.size>0:
            return self.top.data
        print("Stack is empty!")
    
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


myStack = MyStack()
print(myStack.getSize())
myStack.push(10)
myStack.push(20)
print(myStack.getSize())
print(myStack.getTop())
myStack.pop()
print(myStack.getTop())
myStack.pop()
print(myStack.getTop())
print(myStack.isEmpty())
        
        
