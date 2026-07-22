class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res=[]
        for i in range(n):
            nums1.pop()
        i=0
        while nums1!=[] and nums2!=[]:
            if nums1[0]>nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))
            i+=1
        if nums1==[]:
            res= res+nums2
        else:
            res=res+nums1
        nums1[:]=res
        