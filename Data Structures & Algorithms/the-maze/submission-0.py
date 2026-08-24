class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m=len(maze)
        n=len(maze[0])
        visit=set()

        def dfs(r,c):
            if (r,c)in visit:
                return False
            if r==destination[0] and c==destination[1]:
                return True
            visit.add((r,c))
            dire=[(0,1),(1,0),(0,-1),(-1,0)]

            for dr,dc in dire:
                nr,nc=r,c
                while 0<=nr+dr<m and 0<=nc+dc<n and maze[nr+dr][nc+dc]!=1:
                    nr +=dr
                    nc +=dc

                if dfs(nr,nc):
                    return True
            return False

        return dfs(start[0],start[1])








