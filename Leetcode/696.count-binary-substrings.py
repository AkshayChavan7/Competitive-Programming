#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        countList = []
        prevCh = ''
        currCnt = 0
        
        for ch in s:
            if ch==prevCh:
                currCnt+=1
            else:
                if currCnt != 0:
                    countList.append(currCnt)
                currCnt = 1
                prevCh = ch
        
        if currCnt != 0:
            countList.append(currCnt)

        finalCount = 0    
        for i in range(len(countList)-1):
            finalCount+=min(countList[i], countList[i+1])
        return finalCount
        
# @lc code=end

