class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        current_sum=0
        for wg in w:
            current_sum +=wg
            self.prefix.append(current_sum)

        self.total=current_sum

    def pickIndex(self) -> int:
        target=self.total *random.random()
        l=0
        r=len(self.prefix)

        while l<r:
            mid=(l+r)//2
            if self.prefix[mid]<target:
                l=mid+1
            else:
                r=mid
        return l


        #return bisect.bisect_right(self.prefix,target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()