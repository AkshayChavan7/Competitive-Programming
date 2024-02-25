#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def solve(self, s, i, j, memo):
        if (i,j) in memo: return memo[(i,j)]
        if i==j: return 1
        if i>j: return 0
        if s[i] == s[j]: 
            memo[(i,j)] = 2+self.solve(s, i+1, j-1, memo)
            return memo[(i,j)]

        memo[(i,j)] = max(self.solve(s, i+1, j, memo), self.solve(s, i, j-1, memo))
        return memo[(i,j)]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.solve(s, 0, len(s)-1, memo)
        
# @lc code=end

