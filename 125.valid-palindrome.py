#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        def isLetterOrNumber(ch):
            return (ord(ch)>=ord('a') and ord(ch)<=ord('z')) or (ord(ch) >= ord('0') and ord(ch) <= ord('9'))
        

        while left < right:
            if not isLetterOrNumber(s[left]):
                left+=1
                continue
            if not isLetterOrNumber(s[right]):
                right-=1
                continue

            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
        
        
# @lc code=end

