#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        uniquePermutations = []
        nums.sort()
        def permutations(nums, result=[]):
            if len(nums) == 0:
                uniquePermutations.append(result)
            
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                permutations(nums[0:i]+nums[i+1:], result+[nums[i]])
        
        permutations(nums)
        return uniquePermutations
        
# @lc code=end

