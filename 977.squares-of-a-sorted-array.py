#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left, right, ptr = 0, n-1, n-1

        while ptr>=0:
            if abs(nums[left]) < abs(nums[right]):
                result[ptr] = nums[right]*nums[right]
                right-=1
            else:
                result[ptr] = nums[left]*nums[left]
                left+=1
            ptr-=1
        return result
        
# @lc code=end

