class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preReq[crs].append(pre)

        visitset=set()

        def dfs(crs):
            if crs in visitset:
                return False
            if preReq[crs]==[]:
                return True
            visitset.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visitset.remove(crs)
            preReq[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True