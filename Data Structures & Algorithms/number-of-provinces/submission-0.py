class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visit=set()
        res=0

        def dfs(city):
            for neigh in range(n):
                if isConnected[city][neigh]==1 and neigh not in visit:
                    visit.add(neigh)
                    dfs(neigh)

        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res+=1
        return res