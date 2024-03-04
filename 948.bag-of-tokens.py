#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        l, r = 0, len(tokens)-1

        while l<=r:
            if power<tokens[l]:
                if score>0 and r-l > 1:
                    score -=1
                    power+=tokens[r]
                    r-=1
                else:
                    return score
            else:
                score+=1
                power-=tokens[l]
                l+=1
        return score
        
# @lc code=end

