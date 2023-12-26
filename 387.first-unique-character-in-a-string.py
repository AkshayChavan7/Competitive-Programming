#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqList = [0]*26
        A = ord('a')
        for ch in s:
            freqList[ord(ch) - A]+=1
        for i in range(len(s)):
            if freqList[ord(s[i])-A] == 1:
                return i
        return -1
        

    # ALTERNATE APPROACH
    # def firstUniqChar(self, s: str) -> int:
    #     i =0 
    #     n = len(s)
    #     scanned = []
    #     while i < n:
    #         j = i+1
    #         while j < n:
    #             if s[i] == s[j]:
    #                 break
    #             j+=1
    #         if j == n:
    #             return i
    #         scanned.append(s[i])
    #         print(scanned)
    #         while i < n and s[i] in scanned:
    #             i+=1
    #     return -1
        
# @lc code=end

