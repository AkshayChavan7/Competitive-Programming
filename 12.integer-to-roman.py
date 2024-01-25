#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        symMap = {1000:'M', 900:'CM', 500:'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40:'XL', 10: 'X', 9:'IX', 5: 'V', 4: 'IV', 1: 'I' }
        result = ''
        
        while num > 0:
            if num in symMap:
                result += symMap[num]
                num = 0
            else:
                for key in symMap.keys():
                    if key < num:
                        num = num - key
                        result += symMap[key]
                        break
        return result
        
# @lc code=end

