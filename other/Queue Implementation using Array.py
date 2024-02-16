class MyQueue:
    def __init__(self, size):
        self.queue = [0] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.currentSize = 0
    
    def push(self, n):
        if self.currentSize < self.size:
            self.queue[self.rear % self.size] = n
            self.rear += 1
            self.currentSize += 1
        else:
            print("Queue is full")
    
    def pop(self):
        if self.currentSize != 0:
            # res = self.queue[self.front]
            self.front+=1
            self.currentSize -=1
            # return res
        else:
            print("Queue is empty")
    
    def getSize(self):
        return self.currentSize
    

    def empty(self):
        return self.currentSize == 0
    
    def top(self):
        return self.queue[self.front]


q = MyQueue(5)
q.push(3)
q.push(2)
q.push(1)
q.push(8)
q.push(6)
q.push(7)
print("top: ", q.top())
q.pop()
print("size: ", q.getSize())
q.push(7)
print("top: ", q.top())
