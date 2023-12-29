#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i>0 and nums[i-1] == n:
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                total = n + nums[l] + nums[r]
                if total == 0:
                    result.append([n, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif total > 0:
                    r-=1
                else:
                    l+=1

        return result
    

    # FIRST ATTEMPT SOLUTION
    
    # def twoSum(self, nums, target)->List[int]:
    #     l, r = 0, len(nums) - 1
    #     pairs = []
    #     while l<r:
    #         total = nums[l] + nums[r]
    #         if total == target:
    #             pairs.append([nums[l], nums[r]])
    #         if total<target:
    #             l+=1
    #         else:
    #             r-=1
    #     return pairs
            
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     r = dict()
    #     nums = sorted(nums)
    #     for i in range(len(nums)-2):
    #         temp = self.twoSum(nums[i+1:], -nums[i])
    #         for t in temp:
    #             res= [nums[i]]+t
    #             r[tuple(res)]=res

    #     return r.values()
        
# @lc code=end

