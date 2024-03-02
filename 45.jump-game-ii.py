#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
          current, next = 1, 1 
          count, i = 0, 0
          
          while current>0 and i<len(nums)-1:
              current-=1
              next-=1
              if nums[i]>next:
                  next = nums[i]
              i+=1
              if current == 0:
                  current = next
                  count+=1
          return count
        
        
# @lc code=end

