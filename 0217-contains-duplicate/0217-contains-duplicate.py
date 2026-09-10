class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        snums=(set(nums))
        if len(snums)!=len(nums):
            return True
        return False