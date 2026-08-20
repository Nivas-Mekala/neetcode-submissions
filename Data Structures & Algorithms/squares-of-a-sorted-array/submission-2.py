class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            left=nums[l]*nums[l]
            right=nums[r]*nums[r]
            if (left>right):
                res[i]=left
                l+=1
            else:
                res[i]=right
                r-=1
        return res