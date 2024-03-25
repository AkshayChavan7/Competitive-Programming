class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            currentVal = abs(nums[i])-1
            if  nums[currentVal]<1:
                res.append(currentVal+1)
            else:
                nums[currentVal]*=(-1)
        return res