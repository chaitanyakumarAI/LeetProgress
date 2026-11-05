class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n=len(arr2)
        res=0
        for val in arr1:
            l=0
            r=n-1
            flag=True
            while l<=r:
                mid=(l+r)//2
                if abs(arr2[mid]-val)<=d:
                    flag=False
                    break
                if arr2[mid]<val:
                    l=mid+1
                else:
                    r=mid-1
            if flag:
                res+=1
        return res
