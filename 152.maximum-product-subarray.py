#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        prefixProduct, suffixProduct = 1, 1
        n = len(nums)
        for i in range(n):
            prefixProduct *= nums[i]
            suffixProduct *= nums[n-i-1]
            
            maxProduct = max(maxProduct, max(prefixProduct, suffixProduct))

            if nums[i] == 0: prefixProduct = 1
            if nums[n-i-1] == 0: suffixProduct = 1

        return maxProduct
        
# @lc code=end

