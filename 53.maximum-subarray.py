#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        for n in nums:
            if currentSum<0:
                currentSum = n
            else:
                currentSum += n
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
        
# @lc code=end

