#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.pricesStack = [] # (price, index)
        self.currentIndex = 0

    def next(self, price: int) -> int:
        self.currentIndex+=1
        while self.pricesStack and self.pricesStack[-1][0] <= price:
            self.pricesStack.pop()
        
        self.pricesStack.append((price, self.currentIndex))
        
        if len(self.pricesStack)>1:
            return self.currentIndex - self.pricesStack[-2][1] # currentIndex - topIndex
        else : # pricesStack is empty
            return self.currentIndex
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

