#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = (0, len(height)-1)
        leftMax, rightMax, trappedWater = (0,0,0)
        while l <= r:
            if height[l]<= height[r]:
                trappedWater+= max(leftMax - height[l], 0)
                if height[l] > leftMax:
                    leftMax = height[l]
                l+=1
            else:
                trappedWater+= max(rightMax - height[r], 0)
                if height[r] > rightMax:
                    rightMax = height[r]
                r-=1
        return trappedWater
        
        
# @lc code=end

