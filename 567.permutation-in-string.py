#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap1 = defaultdict(lambda: 0)
        freqMap2 = defaultdict(lambda: 0)

        left, right = 0, 0
        for ch in s1:
            freqMap1[ch]+=1

        while right < len(s2):
            if right - left < len(s1):
                freqMap2[s2[right]]+=1
                right+=1
                if freqMap2 == freqMap1: return True
            else:
                if freqMap2[s2[left]] >=2 : 
                    freqMap2[s2[left]]-=1
                else:
                    freqMap2.pop(s2[left])

                left+=1
        return freqMap1 == freqMap2
# @lc code=end

