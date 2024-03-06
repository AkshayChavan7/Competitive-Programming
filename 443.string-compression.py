#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        countList = []
        currChar, currCount = chars[0], 1
        for i in range(1, n):
            if chars[i]!=currChar:
                countList.append([currChar, str(currCount)])
                currChar = chars[i]
                currCount = 1
            else:
                currCount+=1
        countList.append([currChar, str(currCount)])
        
        i = 0
        for char, count in countList:
            chars[i] = char
            i+=1
            if int(count)>1:
                for dig in count:
                    chars[i] = dig
                    i+=1        
        return i
        
# @lc code=end

