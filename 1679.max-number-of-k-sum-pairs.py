#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    # approach 1
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = defaultdict(lambda: 0)
        count = 0
        for n in nums:
            if k - n in map and map[k-n]>0:
                count+=1
                map[k-n]-=1
            else:
                map[n]+=1
        return count
    # approach 2
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l<r:
            total = nums[l] + nums[r] 
            if total == k:
                l+=1
                r-=1
                count+=1
            elif total > k:
                r-=1
            else:
                l+=1
        return count
        
# @lc code=end

