class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        m=nums[n//2]
        return sum(abs(m-nums[i]) for i in range(n))