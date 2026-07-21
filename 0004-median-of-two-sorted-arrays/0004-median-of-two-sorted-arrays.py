class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        m,n=len(nums1),len(nums2)
        while nums1!=[] and nums2!=[]:
            if nums1[0]>nums2[0]:
                res.append(nums2.pop(0))
            else:
                res.append(nums1.pop(0))
        if nums1==[]:
            res= res+nums2
        else:
            res=res+nums1
        if (m+n)%2==1:
            return res[(m+n)//2]
        return (res[(m+n)//2]+res[((m+n)//2)-1])/2