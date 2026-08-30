class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or n==0:
            return n
        w1=0
        w2=0
        w3=0
        ma,mi=max(nums),min(nums)
        i1,i2=nums.index(ma),nums.index(mi)
        w1=max(i1,i2)+1
        w2=max(n-i1,n-i2)
        w3=min(n-i1+i2+1,n-i2+i1+1)
        return min(w1,w2,w3)
            