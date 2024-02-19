#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#

# @lc code=start
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = [] # ([pos, speed], timeToCollide)
        result = [-1] * len(cars)
        for i in range(len(cars)-1, -1, -1):
            if stack:
                # keep popping until we get the next item in stack which has higher speed and lower timeToCollide than current car OR until it becomes empty
                while stack and not (cars[i][1] > stack[-1][0][1] and ((stack[-1][0][0] - cars[i][0])/(cars[i][1] - stack[-1][0][1])) < stack[-1][1]):
                    stack.pop()
                
                # if there exists atleast one item on stack, then we need to calculate the timeToCollide
                if stack:
                    timeToCollide = (stack[-1][0][0] - cars[i][0])/(cars[i][1] - stack[-1][0][1])
                    result[i] = timeToCollide
                else: # if stack becomes empty then we set the timeToCollide to infinity
                    result[i] = -1
                    timeToCollide = float('inf')
                
                stack.append((cars[i], timeToCollide))
            else:
                # if stack is empty then simply push
                stack.append((cars[i], float('inf')))
                result[i] = -1
        return result
        
# @lc code=end

