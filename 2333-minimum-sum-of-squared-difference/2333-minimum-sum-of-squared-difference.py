class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k1+=k2
        n=len(nums1)
        diff=[0]*n
        for i in range(n):
            diff[i]=abs(nums1[i]-nums2[i])
        max_diff=max(diff)
        if max_diff==0 or sum(diff)<=k1:
            return 0
        count=[0]*(max_diff+1)
        for d in diff:
            count[d]+=1
        for i in range(max_diff,0,-1):
            if count[i]==0:
                continue
            if k1>count[i]:
                count[i-1]+=count[i]
                k1-=count[i]
                count[i]=0
                continue
            else:
                count[i]-=k1
                count[i-1]+=k1
                k1=0
                break
        res=0
        for i,c in enumerate(count):
            if c>0:
                res+=(c*i)*i
        return res


