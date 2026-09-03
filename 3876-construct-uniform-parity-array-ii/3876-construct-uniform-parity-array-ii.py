class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=min(nums1)
        if m%2==1 or all(nums1[i]%2==0 for i in range(len(nums1))):
            return True
        else:
            return False