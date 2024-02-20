#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greaterElementsMap = {}
        for i in range(len(nums2) -1, -1, -1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                greaterElementsMap[nums2[i]] = stack[-1]
            else:
                greaterElementsMap[nums2[i]] = -1
            stack.append(nums2[i])

        result = []
        for n in nums1:
            result.append(greaterElementsMap[n])
        return result
        
# @lc code=end

