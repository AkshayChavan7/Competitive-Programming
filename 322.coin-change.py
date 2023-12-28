#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def minCoins(self, coins, amount, memo={}):
        if amount in memo: return memo[amount]
        if amount == 0: return 0
        if amount < 0: return None

        counts = []
        for coin in coins:
            res = self.minCoins(coins, amount-coin, memo)
            if res != None:
                memo[amount] = res+1
                counts.append(memo[amount])
        
        if len(counts) == 0:
            memo[amount] = None
        else:
            memo[amount] = min(counts)
    
        return memo[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        result = self.minCoins(coins, amount, memo)
        return -1 if result == None else result
        
# @lc code=end

