class Solution:
    # approach 1
    def pivotInteger(self, n: int) -> int:
        sum = n*(n+1)/2
        x = int(math.sqrt(sum))
        if x*x == sum: return x 
        else: return -1

    # approach 2
    # def pivotInteger(self, n: int) -> int:
    #     getSum = lambda x: x*(x+1)/2
    #     nSum = getSum(n)
    #     for i in range(n, 0, -1):
    #         preSum = getSum(i)
    #         postSum = nSum - preSum + i
    #         if preSum == postSum:
    #             return i
    #     return -1

    # approach 3
    # def pivotInteger(self, n: int) -> int:
    #     getSum = lambda x: x*(x+1)/2
    #     nums = [i for i in range(n, 0, -1)]
    #     currentSum = 0
    #     for num in nums:
    #         currentSum+=num
    #         if currentSum == getSum(num):
    #             return num
    #     return -1