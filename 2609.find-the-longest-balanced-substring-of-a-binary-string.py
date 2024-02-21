#
# @lc app=leetcode id=2609 lang=python3
#
# [2609] Find the Longest Balanced Substring of a Binary String
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)-1):
            if s[i] == '0' and s[i+1] == '1':
                count = 0
                l = i
                r = i+1
                while l>=0 and r<=len(s)-1:
                    if s[l] == '0' and s[r] == '1':
                        count+=2
                    else:
                        break
                    l-=1
                    r+=1
                maxLen = max(maxLen, count)
        return maxLen
        
# @lc code=end

