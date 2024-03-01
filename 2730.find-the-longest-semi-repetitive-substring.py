#
# @lc app=leetcode id=2730 lang=python3
#
# [2730] Find the Longest Semi-Repetitive Substring
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ptr, start, newStart = 1, 0, 0
        maxLen = 0
        isRepeat = False
        while ptr < len(s):
            if s[ptr] == s[ptr-1]:
                if not isRepeat:
                    isRepeat = True
                    newStart = ptr
                else:
                    print(ptr, start)
                    maxLen = max(maxLen, ptr - start)
                    start = newStart
                    newStart = ptr
            ptr+=1
        maxLen = max(maxLen, ptr - start)
        return maxLen
        
# @lc code=end

