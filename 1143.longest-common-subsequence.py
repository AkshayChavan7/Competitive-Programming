#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
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
# @lc code=end

