class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        st=float('inf')
        for i in range(n):
            ma=max(nums[0:i+1])
            mi=min(nums[i:n])
            if ma-mi<=k:
                return i
        return -1