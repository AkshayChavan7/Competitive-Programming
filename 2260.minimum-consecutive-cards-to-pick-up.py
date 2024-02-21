#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        scannedCards = {}
        minPicks = float('inf')
        for i, card in enumerate(cards):
            if card in scannedCards.keys():
                minPicks = min(minPicks, i - scannedCards[card] + 1)
            scannedCards[card] = i
        return -1 if minPicks == float('inf') else minPicks
        
# @lc code=end

