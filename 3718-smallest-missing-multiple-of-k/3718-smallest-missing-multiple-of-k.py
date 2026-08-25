class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        snums=set(nums)
        i=1
        while True:
            if i*k not in snums:
                return i*k
            i+=1
            