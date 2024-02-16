#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(self, a, b): return a+b
    def subtract(self, a, b): return a-b
    def multiply(self, a, b): return a*b
    def divide(self, a, b): 
        res = a/b
        if res>0:
            return floor(res)
        else:
            return ceil(res)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        ops = {"+": self.add, "-": self.subtract, "*": self.multiply, "/": self.divide}
        
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(ops[token](num1, num2))
            else:
                stack.append(int(token))
        
        return stack.pop()
        
# @lc code=end

