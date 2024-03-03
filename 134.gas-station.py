#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, totalSurplus = 0, 0, 0
        for i in range(len(gas)):
            totalSurplus += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if total<0:
                total = 0
                start = i+1
        return start if totalSurplus>=0 else -1
        
# @lc code=end

