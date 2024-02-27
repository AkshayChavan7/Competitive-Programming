#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # lower half of the sorted array
        self.minHeap = [] # upper half of the sorted array

        

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)

        # if all elements in maxHeap are not smaller than all elements in meanHeap
        if self.minHeap and self.maxHeap and (-self.maxHeap[0]) > self.minHeap[0]:
            heappush(self.minHeap, -heappop(self.maxHeap))
      
        # check if difference in size of min heap and max heap is within allowable limit
        sizeDiff = len(self.maxHeap) - len(self.minHeap)
        if sizeDiff>1: # maxHeap has 1+ extra elements
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif sizeDiff < 0: # minHeap has extra elements
            heappush(self.maxHeap, -heappop(self.minHeap))

        

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap))%2==0: # even size
            return (self.minHeap[0] - self.maxHeap[0])/2
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

