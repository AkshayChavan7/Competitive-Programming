#
# @lc app=leetcode id=2645 lang=python3
#
# [2645] Minimum Additions to Make Valid String
#

# @lc code=start
class Solution:
    # 2nd attempt - optimal solution
    def addMinimum(self, word: str) -> int:
        result = 0
        prev = 'z'
        for ch in word:
            if ch <= prev: result+=2
            else: result-=1
            prev = ch
        return result
    
    # first attempt solution 
    # def addMinimum(self, word: str) -> int:
    #     replacement = {"abc": 0, "ab":1, "bc": 1, "ac": 1, "a": 2, "b":2, "c":2 }
    #     result = 0
    #     n = len(word)
    #     while n>0:
    #         for s in replacement.keys():
    #             index = word.find(s)
    #             if index!=-1:
    #                 n-=len(s)
    #                 word = word[0:index]+"-"+word[index+len(s):]
    #                 result+=replacement[s]
    #                 break
    #     return result
        
# @lc code=end

