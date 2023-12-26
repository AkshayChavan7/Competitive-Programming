class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        count, finalCount = 0, 0
        s,e = 0, 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            finalCount = max(finalCount, count)
        return finalCount