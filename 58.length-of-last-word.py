#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        count = 0
        while n>=0:
            if s[n] == ' ' and count!=0:
                return count
            elif s[n] != ' ':
                count+=1
            n-=1
        return count
        
# @lc code=end

