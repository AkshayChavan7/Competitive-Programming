#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # generate frequency count list for both strings
        l1, l2 = ([0]*26, [0]*26)
        ordA = ord('a')
        for i in range(len(s)):
            l1[ord(s[i])-ordA]+=1
            l2[ord(t[i])-ordA]+=1
        

        return l1==l2
        
# @lc code=end

