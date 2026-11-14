class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ps=[0]*(n+1)
        for i in range(1,n+1):
            ps[i]=ps[i-1]+nums[i-1]
        ms=float('inf')
        for i in range(l,r+1):
            for j in range(n-i+1):
                if min(ms,ps[i+j]-ps[j])>0:
                    ms=min(ms,ps[i+j]-ps[j])
        if ms==float('inf'):
            return -1
        return ms