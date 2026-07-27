class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True

            if nums[r]==nums[m]==nums[r]:
                l +=1
                r -=1
                continue
            #Left Sorted
            if nums[l]<=nums[m]:
                if target>nums[m] or target<nums[m]:
                    l=m+1
                else:
                    r=m-1

            #Right Side
            else:
                if target<nums[m] or target>nums[r]:
                    r=m+1
                else:
                    l=m-1

            
        return False