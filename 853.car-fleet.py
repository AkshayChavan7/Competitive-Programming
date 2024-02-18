#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, speed] for pos, speed in zip(position, speed)]
        prevMaxTime = float('-inf')
        counter = 0
        for pos, speed in sorted(pair, reverse = True):
            time = (target - pos)/speed
            if (target - pos)/speed > prevMaxTime:
                prevMaxTime = time
                counter += 1
        return counter
        
# @lc code=end

