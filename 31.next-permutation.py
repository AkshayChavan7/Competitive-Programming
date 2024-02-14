#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for l in range(len(nums)-2, -1, -1):
            temp = nums[l:]
            for i in range(len(temp)-1, 0, -1):
                if temp[i]>temp[0]:
                    # swap
                    t = temp[0]
                    temp[0] = temp[i]
                    temp[i] = t

                    nums[:] = [n for n in nums[:l]+[temp[0]]+sorted(temp[1:])]
                    return

        nums.sort()
        
# @lc code=end

