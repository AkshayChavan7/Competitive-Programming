class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffMap = {0: -1} # key = difference, value = position
        maxLen = 0
        zeroCount, oneCount = 0, 0
        for i in range(len(nums)):
            if nums[i]==0: zeroCount+=1
            else: oneCount+=1
            diff = zeroCount - oneCount
            if diff in diffMap:
                maxLen = max(maxLen, i - diffMap[diff])
            else:
                diffMap[diff] = i
        return maxLen