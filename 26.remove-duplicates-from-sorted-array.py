#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        nums.append(float('inf'))
        for i in range(len(nums)-1):
            if nums[i]!=nums[(i+1)]:
                nums[ptr] = nums[i]
                ptr+=1
        return ptr
        
# @lc code=end

