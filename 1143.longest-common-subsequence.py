#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    # top-down approach using memoization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        def solve(text1, text2, i=0, j=0, memo={}):
            if (i, j) in memo: return memo[(i, j)]
            if i>=l1 or j>=l2: return 0

            if text1[i] == text2[j]:
                memo[(i, j)] = 1+solve(text1, text2,i+1, j+1, memo)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(solve(text1, text2,i+1,j, memo), solve(text1, text2,i,j+1, memo))
                return memo[(i, j)]
        
        return solve(text1, text2)
    
    # bottom-up approach using tabulization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        t=[[0 for _ in range(n + 1)] for _ in range(m + 1)]
        print(t)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]: t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[m][n]
# @lc code=end

