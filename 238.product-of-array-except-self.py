#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        for i in range(len(nums)-1):
            output.append(output[i]*nums[i])
        
        postfixProduct = 1
        for i in range(len(nums)-1, 0, -1):
            postfixProduct *= nums[i]
            output[i-1]*=postfixProduct 

        return output
        
# @lc code=end

