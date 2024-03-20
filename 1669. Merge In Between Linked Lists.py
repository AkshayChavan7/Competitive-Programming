# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        start = None
        cnt = 0
        while cnt!=b+1:
            if cnt == a-1: start = ptr
            ptr = ptr.next
            cnt+=1
        
        start.next = list2
        while list2.next!=None:
            list2 = list2.next
        list2.next = ptr

        return list1