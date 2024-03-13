class Solution:
    def customSortString(self, order: str, s: str) -> str:
        matched = []
        freqMap = defaultdict(lambda: 0)

        for ch in s: freqMap[ch]+=1

        for ch in order:
            if ch in freqMap: 
                matched.append(ch*freqMap[ch])
                freqMap.pop(ch, None)
        
        return "".join(matched) + "".join([k*v for k,v in freqMap.items()])


    def customSortString(self, order: str, s: str) -> str:
        orderSet = set(order)
        n = len(s)
        matched= defaultdict(lambda: list()) 
        other = ""
        for i in range(n-1, -1, -1):
            if s[i] not in orderSet:
                other = s[i]+other
            else:
                matched[s[i]].append(s[i])
        
        sortedMatched = ""
        
        for ch in order:
            if ch in matched:
                sortedMatched+=("".join(matched[ch]))
        
        return sortedMatched+other