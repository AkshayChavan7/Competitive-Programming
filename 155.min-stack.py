#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    
    def __init__(self):
        self.stck = [(None, None)] * 10000
        self.tp = -1
        self.prevMin = float('inf')

        

    def push(self, val: int) -> None:
        self.prevMin = min(self.prevMin, val)
        self.tp+=1
        self.stck[self.tp] = (val, self.prevMin)    

    def pop(self) -> None:
        if self.tp!=-1:
            self.tp-=1
            top, self.prevMin = self.stck[self.tp]
            if self.tp == -1:
                self.prevMin = float('inf')
        

    def top(self) -> int:
        top, mn = self.stck[self.tp]
        return top

    def getMin(self) -> int:
        return self.prevMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

