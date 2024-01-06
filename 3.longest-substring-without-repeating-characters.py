#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        scanned = set()
        maxCount = 0

        while right < len(s):
            while s[right] in scanned:
               scanned.remove(s[left])
               left += 1
            scanned.add(s[right])
            maxCount = max(maxCount, right - left + 1)
            right+=1
        return maxCount
        
# @lc code=end

