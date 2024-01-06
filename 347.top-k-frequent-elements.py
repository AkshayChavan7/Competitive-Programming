#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(lambda: 0)
        buckets = [[] for i in range(len(nums)+1)]
        result = []
        for n in nums:
            frequencyMap[n]+=1
        
        for key, v in frequencyMap.items():
            buckets[v].append(key)
        
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
# @lc code=end

