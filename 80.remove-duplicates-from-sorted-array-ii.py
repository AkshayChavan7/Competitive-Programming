#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.append(float('inf'))
        nums.append(float('inf'))

        ptr = 0
        for i in range(len(nums)-2):
            if nums[i] != nums[i+2]:
                nums[ptr] = nums[i]
                ptr+=1
        return ptr
        
# @lc code=end

