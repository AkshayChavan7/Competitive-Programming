#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        nums[:] = nums[n-(k%n):] + nums[:n-(k%n)]
        
# @lc code=end

