class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        r=n-1
        if n==1:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        if nums[0]>nums[1]:
            return 0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return mid