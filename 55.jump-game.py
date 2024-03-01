#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, maxReach = 0, nums[0]
        
        while i <= maxReach:
            if maxReach >= len(nums)-1: return True
            maxReach = max(maxReach, i + nums[i])
            i+=1
        
        return False
        
# @lc code=end

