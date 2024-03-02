#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.setList = []
    
    def insert(self, val: int) -> bool:
        if val in self.map: return False
        
        self.map[val] = len(self.setList)
        self.setList.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        
        indexToRemove = self.map[val]
        lastItem = self.setList[-1]
        self.setList[indexToRemove] = lastItem
        self.setList.pop()
        self.map[lastItem] = indexToRemove
        self.map.pop(val)
        return True
        

    def getRandom(self) -> int:
        index = round(random.random() * len(self.setList)-1)
        return self.setList[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

