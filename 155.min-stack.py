#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stck = []
        self.tp = -1
        self.prevMin = float('inf')

    def push(self, val: int) -> None:
        self.prevMin = min(self.prevMin, val)
        self.stck.append((val, self.prevMin))
        self.tp+=1
     
    def pop(self) -> None:
        if self.tp!=-1:
            self.tp-=1
            top, self.prevMin = self.stck[self.tp]
            self.stck.pop()
            if self.tp == -1:
                self.prevMin = float('inf')  

    def top(self) -> int:
        top, mn = self.stck[self.tp]
        return top

    def getMin(self) -> int:
        if self.prevMin==float('inf'): return null
        print("getMIn", self.prevMin)
        return self.prevMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

