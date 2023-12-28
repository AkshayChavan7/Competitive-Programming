# Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(lambda: float('inf'))

        for i in range(len(nums)):
            k = target - nums[i]
            if d[k] != float('inf'):
                return [d[k], i]
            d[nums[i]] = i