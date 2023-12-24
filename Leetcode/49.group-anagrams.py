#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        strMap = dict()
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in strMap:
                strMap[s_sorted].append(s)
            else:
                strMap[s_sorted] = [s]
        return list(strMap.values())
        
# @lc code=end

