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