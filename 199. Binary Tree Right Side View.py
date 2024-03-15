# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Single Pass Solution
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque()
        queue.append((root, 0))
        previous = (root, -1)
        result = []
        while len(queue)>0:
            current, level = queue.popleft()
            if previous[1] != level: 
                result.append(current.val)
            previous = (current, level)
            if current.right: queue.append((current.right, level+1))
            if current.left: queue.append((current.left, level+1))
        return result
    
    # Two Pass Solution
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root: return []
    #     queue = deque()
    #     queue.append((root, 0))
    #     tree = []
    #     while len(queue)>0:
    #         current, level = queue.popleft()
    #         tree.append((current, level))
    #         if current.left: queue.append((current.left, level+1))
    #         if current.right: queue.append((current.right, level+1))
        
    #     result = []
    #     for i in range(len(tree)-1):
    #         if tree[i][1]!=tree[i+1][1]:
    #             result.append(tree[i][0].val)
    #     result.append(tree[-1][0].val)
    #     return result


