
# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        
        (i,n) = (0,len(nums))
        minSize = n
        subArray = []
        while i<n:
            # print(i)
            subArray.append(nums[i])
            while sum(subArray)>=target:
                # print("sum(subArray)>=target",sum(subArray)>=target)
                if minSize>len(subArray):
                    minSize = len(subArray)
                subArray = subArray[1:]   #remove first element
                # print(subArray)
            i+=1
        return minSize
        
