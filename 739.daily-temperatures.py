#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # stack[-1] is the stack top
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temp, i))
        return result
        
        
# @lc code=end

