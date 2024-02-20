#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=[i for i in str(n)]
        l = len(n)
        for i in range(l-1, 0, -1):
            if int(n[i]) > int(n[i-1]):
                for j in range(l-1, i-1, -1):
                    if n[j] > n[i-1]:
                        temp = n[j]
                        n[j] = n[i-1]
                        n[i-1] = temp
                        # after swap just reverse digits from i position to the end
                        res = int(''.join(n[:i]+list(reversed(n[i:]))))
                        return -1 if res > 2147483647 else res
        return -1
        
# @lc code=end

