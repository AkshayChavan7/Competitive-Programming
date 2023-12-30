#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeChars(s):
            stack = []
            for ch in s:
                if ch == '#' and stack:
                    stack.pop()
                elif ch!='#':
                    stack.append(ch)
            return stack
        return removeChars(s) == removeChars(t)
        
# @lc code=end

