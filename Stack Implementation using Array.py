class MyStack:
    def __init__(self, size):
        self.size =  size
        self.top = -1
        self.st = [0] * size
    
    def push(self, n):
        if self.top < self.size - 1:
            self.top += 1
            self.st[self.top] = n
        else:
            print("Stack is already full")
    
    def pop(self):
        if self.top !=- 1:
            self.top-=1
        else:
            print("Stack is already empty")
    
    def topp(self):
        return self.st[self.top]

    def size(self):
        return self.top+1

    def empty(self):
        return self.top == -1


myStack = MyStack(5)
print("Size:", myStack.size)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(90)
print(myStack.topp())
myStack.pop()
print(myStack.topp())
print("isEMpty", myStack.empty())
myStack.push(100)
myStack.push(110)
print("top", myStack.topp())



        