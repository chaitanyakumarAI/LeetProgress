class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        snums=set(nums)
        count=0
        for num in nums:
            if num+diff in snums and num+(diff)*2 in snums:
                count+=1
        return count