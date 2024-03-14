class Solution:

    def getAtmostSumSubarrayCount(self, nums, goal):
        if goal<0: return 0
        sum, count, i, j = 0, 0, 0, 0
        while j<len(nums):
            sum+=nums[j]
            while sum>goal:
                sum-=nums[i]
                i+=1
            count+=(j-i+1)
            j+=1
            
        return count


    # exactly(K) = atMost(K) - atMost(K-1)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count1 = self.getAtmostSumSubarrayCount(nums, goal)
        count2 = self.getAtmostSumSubarrayCount(nums, goal-1)
        return count1-count2
