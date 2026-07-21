class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count=defaultdict(int)
        s2Count=defaultdict(int)

        for ch in s1:
           s1Count[ch] +=1
        
        L=0
        for R in range(len(s2)):
            s2Count[s2[R]] +=1

            if R-L+1>len(s1):
                s2Count[s2[L]]-=1
                if s2Count[s2[L]] == 0:
                    del s2Count[s2[L]]
                L+=1

            if s1Count ==s2Count:
                return True
                

        return False
                

