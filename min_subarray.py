# DRW Coding Asssessment
# https://leetcode.com/discuss/interview-question/1512016/drw-2022-new-grad-swe-codility-oa
'''
Return the length of the minimum-length subarray containing all distinct elements from a given integer array

Ex 1: [1, 2, 3, 3, 4, 4, 3, 2, 1, 1] (Answer: 4)
Ex 2: [1, 2, 3, 3, 4, 4, 2, 1, 1] (Answer: 5)
'''
def minSubArray(a):
    dist = list(set(a))
    start, i, minLen = 0, 0, len(a)
    l = 0
    while i<len(a):
        # print(a[i], dist)
        if a[i] in dist:
                dist.remove(a[i])
                l+=1
                if l==len(list(set(a))) and len(dist) == 0:
                    return l
                if l==minLen and len(dist)==0:
                    start+=1
                    i = start
                    dist = list(set(a))
                    # print('dist reset', dist)
                    minLen = l
                    l = 0
                    continue
                elif len(dist)==0:
                    if minLen>l:
                        minLen = l
                    l = 0
                    start+=1
                    i = start
                    dist = list(set(a))
                    # print('dist reset2', minLen, dist)
                    continue
        else:
            l+=1        
        i+=1
    return minLen



a1 = [1, 2, 3, 3, 4, 4, 3, 2, 1, 1]
a2 =  [1, 2, 3, 3, 4, 4, 2, 1, 1]
a3 = [1 ,1]
a4 = [1]
a5 = [1,2,3,4,4,5,5,5,6,2,3,4,4,5,1,3,4,5,2,6,1,1,1,2]
a6 = [1,2,3,4,5,6,1,3,4,2,3,2,3,5,6,6,5,3,3,2,3,4,2,1]
a7 = [1,3,4,2,3,2,3,5,6,6,5,3,3,2,3,4,2,1,1,2,2,3,4,5,6]
a8 = []
print(minSubArray(a7))
