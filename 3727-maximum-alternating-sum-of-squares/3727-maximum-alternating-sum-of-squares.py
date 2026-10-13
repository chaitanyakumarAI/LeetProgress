class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
        na=sorted(nums)
        ans=0
        for i in range(n):
            if i<n//2:
                ans-=pow(na[i],2)
            else:
                ans+=pow(na[i],2)
        return ans