#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def __init__(self):
        self.memo = {}

    def isPalindrome(self, s, i, j):
        if (i, j) in self.memo: return self.memo[(i,j)]
        if i>=j:
            self.memo[(i, j)] = True
            return True
        if s[i]!=s[j]: 
            self.memo[(i, j)] = False
            return False
        self.memo[(i, j)] = self.isPalindrome(s, i+1, j-1)
        return self.memo[(i, j)]

    def longestPalindrome(self, s: str) -> str:
        maxLen = -1
        startInd = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.isPalindrome(s, i, j):
                    if j-i+1 > maxLen:
                        maxLen = j-i+1
                        startInd = i
        return s[startInd:startInd+maxLen]
        
# @lc code=end

