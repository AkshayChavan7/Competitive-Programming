#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        maxCount = 0
        
        for n in nums:
            if n-1 not in nums: # check if it's start of the sequence
                currentCount = 0
                while n+currentCount in nums: # while next element in the sequence exists, keep on incrementing the count
                    currentCount+=1
                maxCount = max(maxCount, currentCount)
        return maxCount
        
# @lc code=end

