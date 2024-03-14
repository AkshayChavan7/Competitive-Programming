class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

'''
                a
              /   \
            b      c
          /  \       \
         d    e       f
'''

# Depth First Traversal - Iterative
def DFS(root:Node):
    if root == None: return
    stack = [root]

    while len(stack)>0:
        current = stack.pop()
        print(current.val)
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

print('Iterative DFS output =>')
DFS(a)

# Time: O(n)
# Space: O(n)

# Depth First Traversal - Recursive
def DFS_recursive(root:Node):
    if not root: return
    print(root.val)
    DFS_recursive(root.left)
    DFS_recursive(root.right)

print('Recursive DFS output =>')
DFS_recursive(a)

# Time: O(n)
# Space: O(n)

# Depth First Traversal - Recursive 
# Instead of printing the values, we will store them in a list
# and return that as a result
def DFS_recursive2(root:Node):
    if not root: return []
    leftValues = DFS_recursive2(root.left) # [b, d, e]
    rightValues = DFS_recursive2(root.right) # [c, f]
    return [root.val] + leftValues + rightValues

print('Recursive DFS output as list =>')
print(DFS_recursive2(a))

def BFS_recursive(root: Node):
    def myBFS(root:Node):
      if not root: return []

      result = []
      if root.left: result.append(root.left.val)
      if root.right: result.append(root.right.val)
      leftValues = myBFS(root.left) # [d,e]
      rightValues = myBFS(root.right) # [f]
      result+=(leftValues+rightValues)
      return result
    return [root.val]+myBFS(root)
print('Recursive BFS output as list =>')
print(BFS_recursive(a))

# Iterative BFS using Stack
def BFS(root: Node):
    if not root: return []
    result = []
    stack = [root]
    while len(stack)>0:
        current = stack.pop()
        if current: 
            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)
            if current.left: 
                result.append(current.left.val)
            if current.right: 
                result.append(current.right.val)
    return [root.val] + result
print('Iterative BFS output as list =>')
print(BFS(a))

# Iterative BFS using Queue
from collections import deque
def BFS_queue(root: Node):
    if not root: return []
    queue = deque()
    queue.append(root)
    result = []
    while len(queue)>0:
        current = queue.popleft()
        result.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return result
print('Iterative BFS output as list =>')
print(BFS_queue(a))

# Time Complexity: O(n)
# Space Complexity: O(n)


# Tree Includes Problems
'''
                a
              /   \
            b      c
          /  \       \
         d    e       f

Target: e
'''

# recursive
def DFS(root: Node, key):
    if not root: return False
    if root.val == key: return True
    return DFS(root.left, key) or DFS(root.right, key)
print('Recursive DFS output => ')
print(DFS(a, 'e')) # True
print(DFS(a, 'z')) # False
print(DFS(a, 'f')) # True
print(DFS(None, 'a')) # False

# iterative

def DFS_iterative(root: Node, key):
    if not root: return False
    stack = [root]
    while len(stack)>0:
        current = stack.pop()
        if current.val == key: return True
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return False
print('Iterative DFS output => ')
print(DFS_iterative(a, 'e')) # True
print(DFS_iterative(a, 'z')) # False
print(DFS_iterative(a, 'f')) # True
print(DFS_iterative(None, 'a')) # False

# Breadth First Search
def BFS(root: Node, key):
    if not root: return False
    queue = deque()
    queue.append(root)

    while len(queue)>0:
        current = queue.popleft()
        if current.val == key: return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

print('Iterative BFS output => ')
print(BFS(a, 'e')) # True
print(BFS(a, 'z')) # False
print(BFS(a, 'f')) # True
print(BFS(None, 'a')) # False