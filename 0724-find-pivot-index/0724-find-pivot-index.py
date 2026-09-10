class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ps=[0]*n
        ps[0]=nums[0]
        res=-1
        if n==1:
            return 0
        for i in range(n):
            ps[i]=nums[i]+ps[i-1]
        if ps[n-1]-nums[0]==0:
            return 0
        for i in range(1,n-1):
            if ps[i-1]==ps[n-1]-ps[i]:
                res= i
                break
        if ps[n-2]==0 and res==-1:
            res= n-1
        return res