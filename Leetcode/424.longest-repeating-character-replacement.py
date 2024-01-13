#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(lambda: 0)
        left, right = 0, 0
        maxFreq, maxWindowSize = 1, 0

        freqMap[s[right]]+=1
        while right < len(s):
            if (right - left + 1) - maxFreq <= k:
                maxWindowSize = max(maxWindowSize, right - left + 1)
                right+=1
                if right < len(s): 
                    freqMap[s[right]]+=1
                    maxFreq = max(maxFreq, freqMap[s[right]])
            else:
                freqMap[s[left]]-=1
                left+=1
        return maxWindowSize
        
# @lc code=end

