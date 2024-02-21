#
# @lc app=leetcode id=2080 lang=python3
#
# [2080] Range Frequency Queries
#

# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.myMap = defaultdict(list)
        for i in range(len(arr)):
            self.myMap[arr[i]].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        leftInd = bisect.bisect_left(self.myMap[value], left)
        rightInd = bisect.bisect_right(self.myMap[value], right)
        return rightInd - leftInd
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

