#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        minSum = float('inf')
        for num in nums:
            sum+=num
            minSum = min(sum, minSum)
        
        if minSum>=1:
            return 1
        return abs(minSum)+1
        
# @lc code=end

