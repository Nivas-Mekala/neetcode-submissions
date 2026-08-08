class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        area=0
        maxArea=0

        def dfs(r,c):
            if(r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0 or (r,c)in visit):
                return 0
            visit.add((r,c))
            count=1
            count +=dfs(r+1,c)
            count +=dfs(r-1,c)
            count +=dfs(r,c+1)
            count +=dfs(r,c-1)
            return count


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visit:
                    area=dfs(r,c)
                    maxArea=max(area,maxArea)

        return maxArea
