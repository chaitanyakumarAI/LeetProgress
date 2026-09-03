class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        onum = [x for x in nums1 if x % 2 == 1]
        enum = [x for x in nums1 if x % 2 == 0]
        if not onum or not enum:
            return True
            
        min_odd = min(onum)
        min_even = min(enum)
        if min_odd<min_even:
            return True
        else:
            return False