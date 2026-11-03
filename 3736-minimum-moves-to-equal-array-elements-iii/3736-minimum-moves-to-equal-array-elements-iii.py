class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return abs(sum(nums)-len(nums)*max(nums))     