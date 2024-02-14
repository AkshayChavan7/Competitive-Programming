#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def myPermute(nums, current=[], result = []):
            if len(nums) == 0:
                result.append(current)
            
            for i in range(len(nums)):
                myPermute(nums[0:i]+nums[i+1:], current+[nums[i]],  result)
            return result
        return myPermute(nums)
        
# @lc code=end

