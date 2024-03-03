#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        totalNodes, i = 0, 0
        while ptr!=None:
            ptr=ptr.next
            totalNodes+=1
        ptr = head

        while i<(totalNodes - n - 1):
            ptr = ptr.next
            i+=1
        if totalNodes - n - 1>=0:
            ptr.next = ptr.next.next
        else:
            head = ptr.next
            
        return head
        
# @lc code=end

