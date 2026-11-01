class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m=min(nums)
        n=len(nums)
        return sum(nums)-m*n