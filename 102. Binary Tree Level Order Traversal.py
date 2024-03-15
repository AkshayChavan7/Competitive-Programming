# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        prevLevel = 0
        queue = deque()
        queue.append((root, -1))
        result = []
        while len(queue)>0:
            current, level = queue.popleft()
            if level!=prevLevel:
                result.append([current.val])
            else:
                result[-1].append(current.val)
            prevLevel = level
            if current.left: queue.append((current.left, level + 1))
            if current.right: queue.append((current.right, level + 1))
        return result