#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum, l, r = (0, 0, 0)
        n = len(nums)
        minLen = n+1

        while r<n or sum >= target:
            if sum < target and r < n:
                sum+=nums[r]
                r+=1
            else:
                minLen = min(minLen, r - l)
                sum-=nums[l]
                l+=1
        if minLen == n+1:
            return 0
        return minLen
        
# @lc code=end

