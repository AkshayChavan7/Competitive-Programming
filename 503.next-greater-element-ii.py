#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)-1, 0-len(nums), -1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            
            stack.append(nums[i])

        return result
        
# @lc code=end

