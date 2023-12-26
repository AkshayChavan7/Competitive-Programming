#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1 # facing North
        x, y = 0, 0

        for instruction in instructions:
            if instruction == 'G':
                x, y = x+dirX, y+dirY
            elif instruction == 'L':
                dirX, dirY = -1*dirY, dirX
            else:
                dirX, dirY = dirY, -1*dirX
        
        # if position is unchaned OR direction has changed then there is a possible circle
        return (x,y) == (0,0) or (dirX, dirY) != (0,1)
    


    # FIRST ATTEMPT SOLUTION
    # def isRobotBounded(self, instructions: str) -> bool:
    #     pos = [0,0]
    #     direction = 'N'
    #     directions = ['N', 'E', 'S', 'W']
    #     for t in range(4):
    #         for i in range(len(instructions)):
    #             if instructions[i] == 'G':
    #                 if direction == 'N':
    #                     pos[1]+=1
    #                 elif direction == 'W':
    #                     pos[0]-=1
    #                 elif direction == 'S':
    #                     pos[1]-=1
    #                 elif direction == 'E':
    #                     pos[0]+=1
    #             elif instructions[i] == 'L':
    #                 index = directions.index(direction)
    #                 direction = directions[(index+3)%4]
    #             elif instructions[i] == 'R':
    #                 index = directions.index(direction)
    #                 direction = directions[(index+1)%4]
    #             if pos == [0,0] and i == len(instructions)-1:
    #                 return True
    #     return False
        
# @lc code=end

