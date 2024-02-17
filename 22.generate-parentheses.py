#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursiveParenthesis(n, op = 0, cl=0, current=""): # 'op' means opening bracket count and 'cl' means closing bracket count
            if op>n or cl>n or cl>op: return
            if len(current) == 2*n: result.append(current)

            recursiveParenthesis(n, op+1, cl, current+"(")
            recursiveParenthesis(n, op, cl+1, current+")")
        
        recursiveParenthesis(n)
        return result
        
# @lc code=end

