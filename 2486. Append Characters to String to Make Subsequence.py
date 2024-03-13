class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        l1, l2 = len(s), len(t)

        while i<l1 and j<l2:
            if s[i] == t[j]: j+=1
            i+=1
        return l2-j