class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prem=[0]*(n)
        prem[0]=nums[0]
        sufm=[0]*(n)
        for i in range(1,n):
            prem[i]=max(prem[i-1],nums[i])
        sufm[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sufm[i]=min(sufm[i+1],nums[i])
        for i in range(n):
            if prem[i]-sufm[i]<=k:
                return i
        return -1
        