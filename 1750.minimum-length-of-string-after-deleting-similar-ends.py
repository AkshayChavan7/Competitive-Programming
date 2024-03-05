#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                ch = s[left]
                while left<=right and s[left] == ch: left+=1
                ch = s[right]
                while left<=right and s[right] == ch: right-=1
            else: break
        return right-left+1
        
# @lc code=end

